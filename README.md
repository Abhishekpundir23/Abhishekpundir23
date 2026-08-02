<div align="center">

# Hi, I'm Abhishek Pundir 👋

### AI Software Engineer · Coding-Agent Evaluation · Developer Tooling

I build reliable systems at the boundary between **AI-generated code** and **production software**.

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=111827" alt="React" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
</p>

</div>

## About me

I'm a software engineer focused on making AI-assisted development **testable, reproducible, and safe to review**. I design and audit terminal-based coding benchmarks, build executable tests and verifiers, analyze agent trajectories, review model-generated patches, and turn ambiguous failures into concrete engineering findings.

Alongside evaluation work, I build practical Python and TypeScript developer tools and ship full-stack and mobile products. I care about deterministic behavior, edge cases, useful observability, strong CI, and keeping humans in control of consequential code changes.

## What I work on

- **Coding-agent evaluation** — benchmark design, task and verifier validation, trajectory analysis, failure attribution, and adversarial QA
- **Developer tooling** — structural regression testing, AST-based automation, CI workflows, and reviewable code transformation
- **AI engineering** — agent SDK integrations, tool-call tracing, evaluation harnesses, and human-in-the-loop workflows
- **Product engineering** — full-stack and mobile applications with TypeScript, React, Next.js, React Native, and SQLite

## Selected work

### [API Migrator](https://github.com/Abhishekpundir23/api-migrator)

An operator-reviewed prototype for handling breaking TypeScript SDK upgrades. It scans approved repositories, applies deterministic AST transformations, verifies changes in isolated workflows, and publishes a pull request only after explicit human approval. Unsafe, stale, or incomplete results fail closed.

`TypeScript` · `Node.js` · `Next.js` · `SQLite` · `Docker` · `GitHub App`

### [tracediff](https://github.com/Abhishekpundir23/tracediff)

A Python toolkit for structural regression testing of AI agents. It compares tool sequences, arguments, pass rates, cost, and repeated-run variance—not just final scores—and can gate changes in CI. It includes adapters for LangGraph, the OpenAI Agents SDK, and the Claude Agent SDK.

`Python` · `CLI` · `pytest` · `GitHub Actions` · `Agent SDKs`

### [Pulse Fitness Manager](https://github.com/Abhishekpundir23/pulse-fitness-manager)

A released, local-first Android application for gym operations, including memberships, payments, dues, attendance, expenses, PDF invoices, and validated backup and restore. Operational data remains on-device in SQLite without requiring a backend.

`React Native` · `TypeScript` · `Expo` · `SQLite` · `EAS Build` · [Latest release](https://github.com/Abhishekpundir23/pulse-fitness-manager/releases/latest)

## Toolbox

| Area | Technologies and practices |
| --- | --- |
| **Languages** | Python, TypeScript, JavaScript, SQL, C++ |
| **Applications** | Node.js, Next.js, React, React Native, Expo, REST APIs |
| **Engineering** | Docker, Linux, Git, GitHub Actions, CI/CD, SQLite, PostgreSQL, testing, AST codemods |
| **AI & agents** | OpenAI Codex, Claude Code, OpenAI Agents SDK, Claude Agent SDK, LangGraph, LangChain, MCP |

## How I approach engineering

- Make behavior observable and failures reproducible.
- Test invariants and state transitions, not only the happy path.
- Prefer evidence and executable checks over confident claims.
- Fail safely when verification is incomplete.
- Keep human approval in the loop for consequential changes.

## Current focus

I'm especially interested in **AI developer infrastructure**, **coding-agent reliability**, **software evaluation**, and tools that help engineering teams adopt AI without lowering their quality bar.

If you're working on a hard problem in that space, feel free to explore my repositories and connect with me here on GitHub.
