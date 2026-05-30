---
id: self-hosted-inference
title: Inferência AI Self-Hosted — Runtimes, Isolamento e Pesos
description: Padrões operacionais para servir modelos AI auto-alojados (vLLM, Ollama, TGI, llama.cpp, NVIDIA Triton) — isolamento de workload, gestão de pesos, protecção da inferência, hardening específico de containers AI.
sidebar_position: 12
tags: [ai, ml, inference, runtime, vllm, ollama, tgi, triton, gpu, hardening, self-hosted, weights]
---

# Inferência AI Self-Hosted — Runtimes, Isolamento e Pesos

## Porque tratamos a inferência *self-hosted* como caso próprio

Em 2026 muitas equipas operam misturas saudáveis de **modelos consumidos via *provider* externo** (Anthropic, OpenAI, Google) com **modelos servidos internamente** — seja porque os dados são sensíveis e não podem sair do perímetro, seja porque a economia muda quando o uso é elevado, seja porque a equipa quer controlo total sobre o ciclo de vida do modelo. *vLLM*, *Ollama*, *Text Generation Inference (TGI)*, *llama.cpp*, *NVIDIA Triton Inference Server* tornaram-se *runtimes* mainstream para esse uso.

O que muda em relação a uma aplicação web tradicional não é a categoria do problema — continua a ser *hardening* de runtime — mas três elementos concretos:

1. **Os pesos do modelo são um activo crítico** que vive *at-rest* na infraestrutura. Não é "configuração"; é o *núcleo do produto* materializado em bytes.
2. **O workload corre tipicamente em GPU** (ou acelerador equivalente). GPUs partilhadas têm uma postura de isolamento operacional ainda em maturação — vale a pena ser cauteloso.
3. **O *runtime* expõe APIs com semântica nova** — *chat completions*, *embeddings*, *tool use*, *streaming* via SSE/WebSocket. *Hardening* convencional cobre boa parte; restante exige adaptação.

Esta secção complementa [`ARC-014`](../../arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014), [`ARC-015`](../../arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) e o [§4 — *Hardening* de Containers](./hardening-containers) com a especialização para *inference runtimes*.

---

## Inventário de runtimes relevantes (2026)

| Runtime | Modelo de consumo | Uso típico |
|---|---|---|
| **vLLM** | API OpenAI-compatible; servidor Python | Servir LLMs em larga escala com *paged attention* |
| **Text Generation Inference (TGI)** | API HF-compatible; *gRPC* / HTTP | Servir modelos HuggingFace em produção |
| **Ollama** | API REST simples; gestão local de modelos | Workstations e ambientes *air-gapped*; uso *edge* |
| **llama.cpp** (server) | API REST minimalista | CPU-only ou GPU mínima; binário único |
| **NVIDIA Triton Inference Server** | gRPC/HTTP; multi-framework (TF, PyTorch, ONNX, TensorRT) | Inferência multi-modelo de classe enterprise |
| ***Custom* serving** (FastAPI + transformers) | API à medida | Casos com requisitos específicos não cobertos pelos acima |

Não fazemos prescrição entre runtimes — escolhem-se com base em escala, *hardware* disponível, requisitos de licença do modelo, e maturidade operacional da equipa. Os padrões abaixo aplicam-se a todos.

---

## Padrões operacionais

### 1. Os pesos do modelo são activo crítico

Os pesos do modelo — `.safetensors`, `.gguf`, `.bin`, `.onnx`, *checkpoints* — recebem **o mesmo tratamento que segredos em runtime**, com três especializações:

- **Encriptação *at-rest*** no *volume* / *object store* onde vivem; chaves geridas no cofre da organização (cross-link [Policy 18](/sbd-toe/assets/policies/policy-gestao-segredos)).
- **Integridade verificada antes de carregar** — hash SHA-256 do artefacto declarado no AI BOM ([`DEP-012`](../../dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012)) e validado no *startup* do runtime. Mitiga `AML.T0109` *Supply Chain Rug Pull* localmente: se alguém troca o ficheiro no *storage*, o runtime recusa carregar.
- **Controlo de acesso ao *artifact registry*** que serve os pesos — não toda a equipa precisa de *download* directo dos `.safetensors`. Limitar a *service accounts* dos runtimes + um conjunto restrito de operadores.

> 💡 Modelos comerciais *self-hosted* sob licença (ex.: licenças com restrições de uso) acrescentam a obrigação de **auditar quem fez *download*** — o *artifact registry* da organização tem de poder responder a "quem descarregou este modelo, quando, em que ambiente". A licença pode exigi-lo; mesmo quando não exija, é boa higiene.

### 2. Isolamento do workload de inferência

A inferência corre tipicamente em GPU, e GPUs partilhadas têm uma postura de isolamento que vale a pena considerar com cuidado:

- ***Hard isolation*** quando possível — pod com GPU dedicada via *NVIDIA GPU Operator* + *MIG (Multi-Instance GPU)* ou equivalente em hardware AMD/Intel. Dois *tenants* diferentes não partilham o mesmo SM/CU.
- ***Process-level isolation* quando *hard isolation* não é viável** — *MPS (Multi-Process Service)* + cgroup limits + namespaces. A defesa em profundidade aqui é importante, dado que *side-channels* em GPU partilhada são área de research activa (ex.: trabalhos sobre *cross-tenant timing* desde 2023). Não exigimos paranóia academica em produção, mas exigimos consciência operacional do risco.
- **Não misturar inferência sensível com workloads de utilizador no mesmo nó** — se o utilizador final consegue executar código no mesmo *host* onde corre a inferência (caso comum em plataformas de *notebooks* tipo *JupyterHub*), trata-se de adversário co-localizado. Separar.
- **Limites de recursos explícitos** — `--gpu-memory-utilization`, *quota* de VRAM, *quota* de batch size. Sem limites, um *prompt* malicioso com `max_tokens` extremo pode degradar o serviço (categoria DoS clássica especializada).

### 3. Hardening do container de inferência

Aplicamos os princípios do [§4 — *Hardening* de Containers](./hardening-containers) com as seguintes especializações:

- ***Read-only* filesystem** excepto para *paths* explicitamente exigidos pelo runtime (cache, profiling). vLLM e TGI suportam *read-only root*.
- ***Drop capabilities*** — `cap_drop: ALL`; adicionar **apenas** o necessário (nenhuma capability privilegiada deve ser exigida por um *inference runtime* moderno).
- **Utilizador *non-root*** — verificar que a imagem do runtime corre como UID não-root; várias imagens *upstream* ainda usam root por defeito (HF *transformers* histórico, algumas *Ollama base images*) — overriding necessário.
- ***Network policy* restritiva** — o pod de inferência aceita tráfego apenas do *gateway* / *load balancer* da aplicação consumidora; egress apenas para o *artifact registry* (pesos), telemetria (Cap. 12) e — quando aplicável — para o cofre de segredos. Sem egress *internet* arbitrário; em particular, **sem acesso a *registries* públicos em runtime** (a transferência de pesos faz-se no *startup*, não em *runtime*).
- **Imagem base curada** — preferir imagens oficiais do *vendor* do runtime; aplicar [§3 — Assinatura e Cadeia de Trust](./assinatura-cadeia-trust). Imagens de *third party* sem assinatura ficam em quarentena (uma quantidade não-trivial de imagens populares no Docker Hub para inferência AI já foi reportada com *artifacts* ou *malicious payloads* desde 2024).

### 4. APIs de inferência — *hardening* específico

O *runtime* expõe APIs com superficie nova. Para além do *hardening* HTTP convencional (TLS, *rate limiting*, *auth*), aplicamos:

- **Autenticação obrigatória** em todos os *endpoints*, mesmo em ambientes "internos". Vários runtimes (Ollama clássico, *llama.cpp server*) iniciam **sem autenticação** por defeito — uma escolha defensável para *workstation* mas catastrófica em rede partilhada. Configurar antes de expor.
- ***Rate limiting* baseado em consumo** — não apenas pedidos por segundo; também tokens por janela, tempo de inferência total. Cruzar com [`OPS-013`](../../monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013) (*token budget*).
- ***Streaming endpoints* (SSE / WebSocket)** — verificar gestão de conexões longas; impor *timeout* máximo; limitar conexões concorrentes por *principal*.
- **Limite de `max_tokens` no servidor** — não confiar apenas no cliente. Um *prompt* com `max_tokens=1000000` em modelo grande sem servidor a limitar é DoS pronto a usar.
- ***Prompt size limit*** — limite ao tamanho do `prompt` aceite. Para modelos com janela de contexto longa (≥ 200k tokens em 2026), *prompts* extremamente longos têm custo computacional não linear; servidor deve recusar acima de um limite operacional.
- **Audit do consumo por *principal*** — quem invocou, com que tamanho de prompt, com que `max_tokens`, em que *modelo / version*. Alimenta [`OPS-011..014`](../../monitorizacao-operacoes/addon/catalogo-requisitos-operacoes).

### 5. Versão do runtime *pinned*

O runtime (vLLM, TGI, etc.) é uma dependência de cadeia como qualquer outra — *pinning* explícito (cross-link [`DEP-003`](../../dependencias-sbom-sca/addon/catalogo-requisitos-dependencias)), SCA activo nas imagens base, *vulnerability scanning* corrente. Algumas dependências críticas em inference runtimes (`torch`, `transformers`, `vllm`, `cuda-toolkit`) têm CVEs com cadência relevante — entram no fluxo normal do Cap. 05.

---

## Cross-checks e dependências

- **Pesos como dependência de supply chain AI** — entram no AI BOM ([`DEP-011`/`DEP-012`](../../dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011)) com hash, *provider*, licença, versão *pinned*. Mudança de versão maior obriga a *eval suite* (Cap. 10 §C5) e *threat review* (Cap. 03 US-11).
- **Cluster de inferência como ambiente** — *workload identity* dedicada para o runtime ([`ARC-015`](../../arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) aplicado ao caso self-hosted); identidade do *runtime* distinta de identidades de aplicações consumidoras.
- **Operações** — telemetria do runtime entra em [`OPS-011..014`](../../monitorizacao-operacoes/addon/catalogo-requisitos-operacoes); *budget* operacional pode incluir GPU-hours (não só tokens) quando o custo é computacional próprio.

---

## Proporcionalidade por nível de risco

| Padrão | L1 | L2 | L3 |
|---|:--:|:--:|:--:|
| Pesos encriptados *at-rest* | Recomendado | Obrigatório | Obrigatório |
| Hash verificado no *startup* | Recomendado | Obrigatório | Obrigatório |
| Hard GPU isolation | Não exigido | Recomendado | Obrigatório quando workloads sensíveis partilham hardware |
| Container *read-only* + *drop capabilities* + *non-root* | Recomendado | Obrigatório | Obrigatório |
| Network policy restritiva | Recomendado | Obrigatório | Obrigatório |
| Autenticação em *runtime API* | Obrigatório (sempre — independentemente do nível) | Obrigatório | Obrigatório |
| *Rate limit* + *token budget* + `max_tokens` servidor | Recomendado | Obrigatório | Obrigatório |
| Auditoria de *download* de pesos | Recomendado | Recomendado | Obrigatório |
| Versão do runtime *pinned* + SCA activo | Obrigatório (mesma regra de qualquer dependência) | Obrigatório | Obrigatório |

---

## Anti-padrões frequentes

- ❌ **Runtime exposto sem autenticação porque "é rede interna"** — em arquitecturas modernas a "rede interna" inclui demasiados *principals* para se confiar nessa fronteira como única defesa.
- ❌ **Pesos no repositório Git** — `.safetensors` de 70 GB em LFS resolve um problema mas cria outro; preferir *artifact registry* dedicado com controlo de acesso e auditoria.
- ❌ **GPU partilhada entre *tenants* sem isolamento configurado** — *side-channels* em research activa; mesmo que improváveis na prática, a ausência de configuração explícita é gap de postura.
- ❌ **Imagem `latest` do runtime** — viola [`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) (cross-link com [`ARC-015`](../../arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)); inferência fica vulnerável a *upgrade* não anunciado.
- ❌ **`max_tokens` confiado apenas ao cliente** — servidor sem limite operacional é DoS pronto a explorar.
- ❌ ***Streaming endpoints* sem *timeout* máximo** — conexões longas consomem recursos GPU em modelos que mantêm KV cache; sem limite, atacante mantém canal aberto e bloqueia capacidade.

---

## Referências

- **vLLM** — *paged attention* + servidor de inferência (OpenAI-compatible)
- **Hugging Face TGI** — Text Generation Inference
- **Ollama** — runtime local + gestor de modelos
- **llama.cpp** — inferência CPU/GPU em C++
- **NVIDIA Triton Inference Server** — inferência multi-framework de classe enterprise
- **NVIDIA MIG (Multi-Instance GPU)** — *hard isolation* em GPUs Ampere/Hopper
- **NIST SP 800-190** — *Application Container Security Guide*
- **CIS Benchmarks — Docker, Kubernetes** — base para *hardening* de containers
- **MITRE ATLAS** `AML.T0109` (*AI Supply Chain Rug Pull*) — mitigado pela verificação local de hash dos pesos
- **OWASP LLM Top 10 (2025)** — LLM02 (*Sensitive Information Disclosure*), LLM04 (*Data and Model Poisoning*), LLM10 (*Unbounded Consumption*) — vectores cobertos pelos padrões acima

---

> 🧭 Em resumo: servir modelos AI *self-hosted* não é uma nova categoria de problema — é o problema clássico de *hardening* de runtime, com três especializações ineliminíveis: **pesos são activo crítico**, **GPU partilhada precisa de isolamento explícito**, e ***APIs de inferência têm semântica de consumo** que o *rate-limiting* HTTP convencional não cobre*.
