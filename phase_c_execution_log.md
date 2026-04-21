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
