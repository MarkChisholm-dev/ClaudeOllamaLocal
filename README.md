<div align="center">

# 🔐 ClaudeOllamaLocal

### **Your Private AI Coding Assistant - 100% Local, Zero Cloud**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)](https://fastapi.tiangolo.com)
[![Ollama](https://img.shields.io/badge/Ollama-000000?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJMMiAxMkwxMiAyMkwyMiAxMkwxMiAyWiIgZmlsbD0id2hpdGUiLz4KPC9zdmc+)](https://ollama.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)](https://www.docker.com/)

**🛡️ NDA-Ready** • **🔒 TPN-Compliant** • **🚫 Zero Telemetry** • **💻 Air-Gap Compatible**

[Quick Start](#-quick-start) • [Features](#-features) • [Docker Setup](#-docker-deployment) • [Compliance](#-nda--tpn-compliance)

---

</div>

## 🌟 Why ClaudeOllamaLocal?

**ClaudeOllamaLocal** is a truly private, self-hosted AI coding assistant that **never sends your data to the cloud**. Built for high-security environments handling sensitive IP, NDAs, and compliance requirements.

```
┌─────────────────────────────────────────┐
│   Your Code → Local AI → Your Machine  │
│        🚫 NO CLOUD • NO TRACKING       │
└─────────────────────────────────────────┘
```

Perfect for:
- 🏢 **Enterprise Development** - Protect proprietary code
- 🎬 **Media & Entertainment** - TPN security requirements
- ⚖️ **Legal & Healthcare** - Strict confidentiality mandates
- 🔐 **Security Research** - Air-gapped environments
- 🏠 **Privacy-Conscious Developers** - Own your data

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔒 **Privacy First**
- ✅ 100% local processing
- ✅ No cloud API calls
- ✅ No telemetry or tracking
- ✅ Ephemeral conversation memory
- ✅ Code never leaves your machine

</td>
<td width="50%">

### 🚀 **Developer Friendly**
- ✅ Beautiful web UI with syntax highlighting
- ✅ CLI tool for terminal workflows
- ✅ Markdown & code block rendering
- ✅ Docker & Docker Compose ready
- ✅ Cross-platform (Linux, macOS, Windows)

</td>
</tr>
<tr>
<td width="50%">

### 🛡️ **Compliance Ready**
- ✅ NDA-compliant deployment
- ✅ TPN security compatible
- ✅ Air-gap network support
- ✅ Fully auditable (GPL-3.0)
- ✅ No external dependencies

</td>
<td width="50%">

### ⚡ **Technology Stack**
- ✅ FastAPI backend
- ✅ Ollama LLM engine
- ✅ qwen2.5-coder model
- ✅ Modern JavaScript UI
- ✅ Highlight.js code rendering

</td>
</tr>
</table>

---

## 🚀 Quick Start

### **Method 1: Automated Setup (Recommended)**

```bash
# 1. Clone the repository
git clone https://github.com/MarkChisholm-dev/ClaudeOllamaLocal.git
cd ClaudeOllamaLocal

# 2. Run the setup script (installs Ollama, pulls model, creates CLI tool)
python setup_agent.py

# 3. Start the web interface
python main.py
```

🎉 **That's it!** Open [http://localhost:8000](http://localhost:8000) in your browser.

---

### **Method 2: Manual Setup**

<details>
<summary><b>📋 Click to expand manual installation steps</b></summary>

#### Prerequisites
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Ollama** ([Install Guide](https://ollama.com/download))

#### Steps

```bash
# 1. Clone repository
git clone https://github.com/MarkChisholm-dev/ClaudeOllamaLocal.git
cd ClaudeOllamaLocal

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Install and start Ollama (if not already installed)
# Linux
curl -fsSL https://ollama.com/install.sh | sh

# macOS/Windows: Download from https://ollama.com/download

# 4. Pull the AI model
ollama pull qwen2.5-coder

# 5. Start the FastAPI server
python main.py
```

Open [http://localhost:8000](http://localhost:8000) to use the web UI.

</details>

---

## 🐳 Docker Deployment

### **Docker Compose (Easiest)**

```bash
# 1. Ensure Ollama is running on your host
ollama serve --host 0.0.0.0

# 2. Build and start the container
docker compose up -d

# 3. Access the app
```
Visit [http://localhost:8000](http://localhost:8000)

### **Docker Networking Notes**

| Platform | Configuration |
|----------|---------------|
| **Linux** | Uses `network_mode: host` - container shares host network |
| **macOS/Windows** | Uses `host.docker.internal` automatically |

<details>
<summary><b>🐛 Troubleshooting Docker</b></summary>

#### **500 Internal Server Error**
- ✅ Ensure Ollama is running: `ollama serve --host 0.0.0.0`
- ✅ Check Ollama is listening on port `11434`
- ✅ Verify `network_mode: host` in docker-compose.yml (Linux only)

#### **Connection Refused**
- ✅ Confirm FastAPI container is running: `docker compose ps`
- ✅ Check Ollama accessibility from container
- ✅ Review logs: `docker compose logs`

#### **Linux Host Networking**
On Linux, `network_mode: host` means:
- Container uses host's network stack directly
- Port mappings are ignored
- Requires Docker privileges for host networking

</details>

---

## 🛡️ NDA & TPN Compliance

> **ClaudeOllamaLocal is designed for deployment in secure, isolated environments to meet NDA and TPN compliance requirements.**

### 🔐 **NDA Compliance**

| Requirement | Implementation |
|-------------|----------------|
| **No Third-Party Services** | ✅ All processing happens locally - no cloud APIs |
| **Zero Telemetry** | ✅ No analytics, tracking, or external reporting |
| **No Data Persistence** | ✅ Conversations stored only in RAM during runtime |
| **Full Auditability** | ✅ GPL-3.0 licensed - review all source code |
| **Data Isolation** | ✅ Your responsibility to deploy on compliant hardware |

### 🎬 **TPN (Trusted Partner Network) Compliance**

| Requirement | Implementation |
|-------------|----------------|
| **No External Connections** | ✅ No SaaS or remote inference APIs |
| **No Data Egress** | ✅ Application prevents outbound data transfer |
| **Air-Gap Compatible** | ✅ Works in isolated, high-security networks |
| **Open Source Stack** | ✅ All dependencies are open source (FastAPI, Ollama) |
| **Physical Security** | ✅ Depends on your deployment environment |

> **⚠️ IMPORTANT:** While this software is built for compliance, ultimate NDA/TPN certification depends on your operational procedures, IT environment, and organizational controls. Consult your legal and security teams.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    YOUR MACHINE                         │
│                                                           │
│  ┌──────────────┐      ┌──────────────┐      ┌────────┐ │
│  │   Web UI     │◄────►│  FastAPI     │◄────►│ Ollama │ │
│  │  (Browser)   │      │  (Backend)   │      │  (LLM) │ │
│  └──────────────┘      └──────────────┘      └────────┘ │
│       localhost:8000        Python               :11434  │
│                                                           │
│  🔒 All traffic stays LOCAL - No internet required       │
└─────────────────────────────────────────────────────────┘
```

**Components:**
- **Frontend:** Modern web UI with Markdown rendering & syntax highlighting
- **Backend:** FastAPI server handling requests (localhost only)
- **AI Engine:** Ollama running qwen2.5-coder LLM locally
- **CLI Tool:** `ask-ollama` command for terminal workflows

**Data Flow:**
1. User submits prompt via web UI or CLI
2. FastAPI backend processes request locally
3. Ollama generates response using local model
4. Response rendered in UI with code highlighting
5. Conversation kept in RAM only (ephemeral)

---

## 🎨 Screenshots

> _Add your screenshots here!_

```
Web UI: Beautiful chat interface with code highlighting
CLI: Terminal-based interaction for power users
```

---

## 💻 CLI Tool

The setup script creates a universal CLI tool for quick terminal access:

```bash
# After running setup_agent.py, use anywhere:
ask-ollama "explain this bash command: find . -name '*.py' -exec grep -l 'TODO' {} \;"

ask-ollama "write a Python function to reverse a linked list"

ask-ollama "review this code for security issues"
```

**Platform Support:**
- **Linux/macOS:** Installed to `~/.local/bin/ask-ollama`
- **Windows:** Installed to `%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\ask-ollama.bat`

---

## 📚 Usage Examples

### **Web Interface**

1. Start the server: `python main.py`
2. Open [http://localhost:8000](http://localhost:8000)
3. Type your coding question or paste code to review
4. Get instant AI-powered responses with syntax highlighting

### **CLI Interface**

```bash
# Get help with a command
ask-ollama "what does the rsync -avz flag do?"

# Code generation
ask-ollama "create a REST API endpoint in FastAPI for user authentication"

# Code review
ask-ollama "review this function for performance issues: $(cat myfile.py)"

# Debugging
ask-ollama "why does this SQL query return duplicates? SELECT * FROM users JOIN orders ON users.id = orders.user_id"
```

---

## ⚙️ Configuration

### **Environment Variables**

```bash
# Change Ollama host (default: localhost)
export OLLAMA_HOST=192.168.1.100

# Use different model
# Edit main.py and change MODEL = "qwen2.5-coder" to your preferred model
```

### **Available Models**

```bash
# List installed models
ollama list

# Pull different models
ollama pull codellama
ollama pull deepseek-coder
ollama pull mistral

# Update main.py to use your preferred model
```

---

## 🔧 Development

### **Project Structure**

```
ClaudeOllamaLocal/
├── main.py              # FastAPI backend server
├── setup_agent.py       # Automated installation script
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container image definition
├── docker-compose.yml   # Docker orchestration
├── templates/
│   └── index.html       # Web UI template
├── static/
│   ├── chat.js          # Frontend JavaScript
│   └── style.css        # UI styling
└── README.md            # This file
```

### **Running in Development**

```bash
# Install dependencies
pip install -r requirements.txt

# Run with auto-reload
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Backend Framework** | [FastAPI](https://fastapi.tiangolo.com/) | High-performance async web server |
| **LLM Engine** | [Ollama](https://ollama.com/) | Local LLM inference |
| **AI Model** | qwen2.5-coder | Code-optimized language model |
| **Frontend** | Vanilla JavaScript | Lightweight, fast UI |
| **Markdown Rendering** | [Marked.js](https://marked.js.org/) | Parse LLM markdown responses |
| **Syntax Highlighting** | [Highlight.js](https://highlightjs.org/) | Code block beautification |
| **Containerization** | Docker & Docker Compose | Portable deployment |

---

## ⚠️ Security Best Practices

### **For Production Deployment:**

🔒 **Network Isolation**
- Deploy on isolated networks or air-gapped systems
- Do NOT expose FastAPI (port 8000) or Ollama (port 11434) to public internet
- Use firewall rules to restrict access

🔒 **Access Control**
- Add authentication if exposing beyond localhost
- Use reverse proxy (nginx/Caddy) with SSL for remote access
- Implement rate limiting for /ask endpoint

🔒 **Audit & Monitoring**
- Review code before deployment (GPL-3.0 licensed, fully auditable)
- Monitor system logs for unusual activity
- Keep Ollama and Python dependencies updated

🔒 **Data Handling**
- Conversations stored in RAM only (not persisted to disk)
- Review your organization's data retention policies
- Consider encrypting Docker volumes if persistence is needed

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

**Guidelines:**
- Maintain privacy-first design
- Keep dependencies minimal and auditable
- Follow existing code style
- Update documentation for new features

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

**What this means:**
- ✅ Free to use, modify, and distribute
- ✅ Commercial use allowed
- ✅ Must disclose source code
- ✅ Changes must be licensed under GPL-3.0

---

## 🙏 Acknowledgments

- **[Ollama](https://ollama.com/)** - Making local LLMs accessible
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern Python web framework
- **[Qwen Team](https://github.com/QwenLM)** - qwen2.5-coder model
- **Privacy advocates** - Keeping developer tools surveillance-free

---

## ❓ FAQ

<details>
<summary><b>Does this work offline?</b></summary>

Yes! After initial setup (downloading Ollama and the AI model), ClaudeOllamaLocal works completely offline. No internet connection required.

</details>

<details>
<summary><b>How much disk space do I need?</b></summary>

- Ollama: ~200 MB
- qwen2.5-coder model: ~1.5-3 GB (depending on quantization)
- Python dependencies: ~50 MB

Total: ~2-3.5 GB

</details>

<details>
<summary><b>What hardware do I need?</b></summary>

**Minimum:**
- 8 GB RAM
- 4 CPU cores
- 5 GB disk space

**Recommended:**
- 16 GB RAM
- 8 CPU cores
- GPU (optional, for faster inference)

</details>

<details>
<summary><b>Can I use a different AI model?</b></summary>

Yes! Edit `main.py` and change `MODEL = "qwen2.5-coder"` to any Ollama-supported model:
- `codellama`
- `deepseek-coder`
- `mistral`
- `llama2`

Then run `ollama pull <model-name>`

</details>

<details>
<summary><b>Is this actually NDA/TPN compliant?</b></summary>

The software is **designed** for compliance, but ultimate certification depends on:
- Your deployment environment (hardware, networks)
- Organizational security policies
- Physical security controls
- Audit procedures

**Always consult your legal and security teams for official compliance verification.**

</details>

<details>
<summary><b>Can I access this from other devices on my network?</b></summary>

Yes, but **not recommended for sensitive work**. To allow network access:

1. Edit `main.py`, change `uvicorn.run()` to bind `0.0.0.0`
2. Add authentication/SSL via reverse proxy
3. Use firewall rules to restrict access

For maximum privacy, keep it localhost-only.

</details>

---

<div align="center">

## 🌟 Star this project if it helps you stay private!

### Built with ❤️ for privacy-conscious developers

**[Report Bug](https://github.com/MarkChisholm-dev/ClaudeOllamaLocal/issues)** • **[Request Feature](https://github.com/MarkChisholm-dev/ClaudeOllamaLocal/issues)**

---

**Disclaimer:** This project is not affiliated with Anthropic, Claude, or any cloud AI providers. It is an independent, open-source tool for local AI inference.

*Legal compliance claims are provided for informational purposes. Consult qualified legal/security professionals for official NDA and TPN certification.*

</div>
