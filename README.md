# 🤖 Ollama Local Coding Studio
[![Python CI](https://github.com/MarkChisholm-dev/ClaudeOllamaLocal/actions/workflows/python-app.yml/badge.svg)](https://github.com/MarkChisholm-dev/ClaudeOllamaLocal/actions/workflows/python-app.yml)

A lightweight, self-hosted web interface and CLI tool for interacting with local LLMs (optimized for `qwen2.5-coder`). Run your own private coding assistant on Windows, macOS, or Linux with zero data leaving your machine.

## ✨ Features

* **Modern Web UI**: Built with FastAPI, featuring Markdown rendering and code syntax highlighting (via Highlight.js).
* **Asynchronous Performance**: Uses `httpx` for non-blocking communication with the Ollama API.
* **Cross-Platform CLI**: A universal Python-based setup script that creates a global `ask-ollama` command.
* **Context Aware**: Maintains a sliding window of chat history for coherent conversations.
* **Zero Dependencies (External)**: Runs entirely on your local hardware using Ollama.

---

## 🚀 Quick Start

### 1. Prerequisites
* [Ollama](https://ollama.com/) installed and running.
* Python 3.8+ installed.

### 2. Automatic Setup (CLI + Model)
Run the universal setup script to pull the model and install the `ask-ollama` CLI helper:

```bash
python setup_agent.py
