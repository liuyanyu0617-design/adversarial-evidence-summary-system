# Adversarial Evidence Summary & Dialogue Analysis System

An automated, intelligent text processing and analysis pipeline powered by Large Language Models (LLMs) and structured AI Agents. This repository demonstrates how to ingest unstructured, multi-party dialogues, normalize domains-specific slangs, and securely extract objective event chains and chronological facts without human intervention.

## 🌟 Core Features

- **Robust Text Normalization**: Advanced regex-based cleaning and context-aware conversion of ambiguous phraseologies and slangs into standard academic/analytical metadata.
- **Multi-Agent Orchestration Framework**: Deploys specialized system prompts mimicking professional computational linguistics agents for highly rigorous fact-extraction pipelines.
- **Structured JSON Schema Outputs**: Guarantees deterministic outputs from probabilistic LLMs, ensuring perfect integration with downstream database systems or timeline visualization tools.
- **Privacy & Security First**: Designed from the ground up to operate without hardcoded credentials, leveraging robust environment variables and data anonymization practices.

## 🛠️ Project Structure

```bash
adversarial-evidence-summary-system/
├── src/
│   ├── data_normalization.py    # Text cleansing and preprocessing layer
│   ├── text_analyzer_agent.py   # OpenAI-powered core analytical Agent
│   └── __init__.py
├── requirements.txt             # Project software dependencies
└── README.md                    # System documentation# adversarial-evidence-summary-system
An automated text processing and analysis system based on LLMs and AI agents.
