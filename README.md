# 🛡️ AuditorSquad

> **The multi-persona security, privacy, and AI threat assessment board for your code and system configurations.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-5A67D8.svg)](#quickstart)
[![AI Security](https://img.shields.io/badge/AI_Security-Omega-red.svg)](#meet-your-board-of-auditors)

AuditorSquad brings a panel of virtual security, privacy, and system architecture experts into your local development workflow. Instead of overwhelming you with unstructured text, AuditorSquad scans your code non-destructively and outputs an actionable, visual risk dashboard.

---

## 👥 Meet Your Board of Auditors

AuditorSquad passes your code sequentially through 5 specialized expert lenses:

* 🔴 **Auditor Alpha (Secrets & AppSec):** Identifies exposed API keys, SQL/Command injections, and unprotected endpoints.
* 🟡 **Auditor Beta (Compliance & Data Privacy):** Scans for PII leakage in logs, unencrypted sensitive data, and regulatory gaps (GDPR/HIPAA/PCI-DSS).
* 🔵 **Auditor Gamma (Architecture & Scale):** Flags single points of failure, missing rate limits, connection leaks, and scaling bottlenecks.
* 🟣 **Auditor Delta (Resilience & Supply Chain):** Detects unsafe dynamic evaluations (`eval`), unpinned dependencies, and unhandled exception paths.
* 🟢 **Auditor Omega (AI Safety & Prompt Injection):** Scans for LLM prompt injection risks, indirect data poisoning, and unsafe AI output execution sinks.

---

## ⚡ Quickstart

### 1. Import the Skill
Clone your repository locally or add `auditor-squad` to your AI workspace:
```bash
git clone https://github.com/kiranagentdev/auditor-squad.git