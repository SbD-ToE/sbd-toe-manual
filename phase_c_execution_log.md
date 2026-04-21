# Phase C Execution Log

## Phase C — PAUSED 2026-04-21

Rolled back commit `0df17205` per programme-lead direction (quality gap vs P2 v1 baseline).
Awaiting revised Cartographer + Manual agent methodology.

Previous state: `ACO-IAT / asvs_v4_0_2` batch (25 items) added to `04-arquitetura-segura`.
Rollback: revert commit `5a0d355d`.

## Slice ACO-IAT — completed 2026-04-21T09:20:20+0100

- Items closed: 235
- Items skipped: 0 (breakdown: duplicate 0 / format-mismatch 0 / backtrace-unresolved 0 / tipo-b 0)
- Pilots processed: asvs_v4_0_2, asvs_v5_0_0, cis_controls_v8_1_2, hipaa_security_rule, mcp_official_security_foundations_2025, nist_sp800_53_rev5, owasp_mcp_third_party_servers_v1_0, pci_dss_v4_0_1, ssdf_sp800_218_v1_1
- Commits: 0df17205, 4f6d056c, 127a6d04, a50be466, 6808d91f, 56fe8287, c20969d3, c725aa44, 5b727b95
- Anomalies: Brief syntax was loose (`slices[]`/`pilots[]`), but runtime JSON is `slices.<SLICE>.items`; ASVS v5 required per-subanchor handling across ACO-IAT-001/002/003/004/005; no stop triggers hit.

## Slice ACO-IVF — completed 2026-04-21T13:52:32+0100

- Items closed: 67
- Items skipped: 0 (breakdown: duplicate 0 / format-mismatch 0 / backtrace-unresolved 0 / tipo-b 0)
- Pilots processed: asvs_v4_0_2, asvs_v5_0_0, cis_controls_v8_1_2, cwe_software_development_view_v4_19_1, hipaa_security_rule, mcp_official_security_foundations_2025, nist_sp800_53_rev5, owasp_mcp_secure_server_development_v1_0, owasp_mcp_third_party_servers_v1_0, owasp_mcp_top_10_v0_1_2025_beta, pci_dss_v4_0_1, ssdf_sp800_218_v1_1
- Commits: fc583e0f, 1d9b274a, 5665322e, 827fc8c4, 33b29227, b0ede6e6, 2ba167b2, 5fd9d79d, c2db518b, 664449b9, 88b055ba, 48fdc99d
- Anomalies: No stop triggers hit; ACO-IVF mapping stabilized on chapter-06 canon sources (`VAL-001–005`, `ERR-001–007`, and the operational secure-coding addon cluster for IVF-007).

## Slice ACO-SCBI — completed 2026-04-21T16:45:26+0100

- Items closed: 71
- Items skipped: 1 (breakdown: duplicate 1 / format-mismatch 0 / backtrace-unresolved 0 / tipo-b 0)
- Pilots processed: asvs_v4_0_2, cis_controls_v8_1_2, cwe_software_development_view_v4_19_1, hipaa_security_rule, nist_sp800_53_rev5, owasp_dsomm, owasp_mcp_secure_server_development_v1_0, owasp_mcp_third_party_servers_v1_0, owasp_mcp_top_10_v0_1_2025_beta, pci_dss_v4_0_1, slsa_spec_v1_0_build_track, ssdf_sp800_218_v1_1
- Commits: bc3ec531, f3015582, d38f8b16, bd21fb28, 3ccd74f8, f955cd19, ff6300cc, d6fb4648, b5d652c7, 97257580, e9641b01, b78ef448
- Anomalies: No stop triggers hit; one exact duplicate-preexisting manual row was detected for `SLSA-VERIFY-DEPENDENCIES` and skipped to avoid duplicating the same source item already published as `⚠️ Parcial`; Surface-2 items `CRA-ART-13`, `DORA-ART-28`, and `DORA-ART-30` remained out of scope for the manual agent per brief.

## Slice ACO-IAT v2 — completed 2026-04-21T21:36:06+0100

- Items closed: 200 of 233 manual_agent
- Upgrades (Cobertura calibration): 51 (`Reparação → ✅ Semântico`)
- Items skipped: 2 (`CIS-14.2`, `CIS-14.3` — chapter-fit mismatch; already covered by Cap. 13 `CIS-14`)
- Items held: 31 (`nist_sp800_53_rev5` — Cartographer v2.1 re-routing required)
- Pilots processed: asvs_v4_0_2, asvs_v5_0_0, cis_controls_v8_1_2, hipaa_security_rule, mcp_official_security_foundations_2025, nist_sp800_53_rev5 (held), owasp_mcp_third_party_servers_v1_0, pci_dss_v4_0_1, ssdf_sp800_218_v1_1
- Commits: a7434c99, ca37d9b0, 08577623, 7f4cff06, 6ad84a7c, 03769851, f30b8671, a8b1ded7
- Anomalies: `nist_sp800_53_rev5` triggered quality-gate §8 / escalation §11.4: all 31 manual_agent items were routed to `04-arquitetura-segura`, but semantic review showed chapter-fit failure at scale across policy-layer (`AC-1`, `IA-1`), device governance (`AC-19*`), UX/logon notices (`AC-8`, `AC-9*`), and personnel screening (`SA-21*`) controls; batch left untouched and held for Cartographer v2.1 supplier re-work. `CIS-14.2` and `CIS-14.3` were skipped because the training semantics are already published in `13-formacao-onboarding/canon/25-rastreabilidade.md`.

## Slice ACO-IVF v2.1 — completed 2026-04-21T23:59:00+0100

- Items closed: 61 of 62 manual_agent
- Upgrades (Cobertura calibration): 22 (`Reparação → ✅ Semântico`)
- Items skipped: 1 (`SSDF-PRACTICE-PW.5` — duplicate of the existing explicit SSDF PW.5 row already published in Cap. 06)
- Items held: 0
- Pilots processed: asvs_v4_0_2, asvs_v5_0_0, cis_controls_v8_1_2, cwe_software_development_view_v4_19_1, hipaa_security_rule, mcp_official_security_foundations_2025, nist_sp800_53_rev5, owasp_mcp_secure_server_development_v1_0, owasp_mcp_third_party_servers_v1_0, owasp_mcp_top_10_v0_1_2025_beta, pci_dss_v4_0_1, ssdf_sp800_218_v1_1
- Commits: df59bd9d, 71a98fbe, 1cb54cd8, 4ead4881, eb93f236, 5c8c9ab6, 5a2c36b8, 5ce475c7, f2402b57, 15b607e6, b7e7a6bc
- Anomalies: NIST 800-53 v2.1 re-routing was applied successfully inside the slice, distributing `SI-1` to Cap. 14, `SI-8*` to Cap. 12, and `SI-9`/`SI-16`/`SI-17` to Cap. 06 without triggering a new chapter-fit escalation. `SSDF-PRACTICE-PW.5` was skipped to avoid duplicating the already published explicit row `SSDF PW.5 | Create Source Code with Secure Coding Techniques` in `06-desenvolvimento-seguro/canon/25-rastreabilidade.md`. Surface-2 items `CIS-9.2`, `CIS-9.5`, and `OWASP-MCP-3P-MEMORY-POISONING` remained out of scope for the manual agent per brief.
