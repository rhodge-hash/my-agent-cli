<div align="center">
  <a href="https://github.com/rhodge-hash/my-agent-cli">
    <img src="https://raw.githubusercontent.com/rhodge-hash/my-agent-cli/main/AgentApp.png?raw=true" alt="My-Agent CLI Logo" width="300" height="200">
  </a>
  
  <h1>🤖 My-Agent CLI</h1>
  <p>
    <b>A powerful, extensible TUI for interacting with <br> local Large Language Models (LLMs) and automating software tasks.</b>
  </p>
  <p>
    <a href="https://github.com/rhodge-hash/my-agent-cli/stargazers">
      <img src="https://img.shields.io/github/stars/rhodge-hash/my-agent-cli?style=flat-square" alt="Stars">
    </a>
    <a href="https://github.com/rhodge-hash/my-agent-cli/network/members">
      <img src="https://img.shields.io/github/forks/rhodge-hash/my-agent-cli?style=flat-square" alt="Forks">
    </a>
    <a href="https://github.com/rhodge-hash/my-agent-cli/issues">
      <img src="https://img.shields.io/github/issues/rhodge-hash/my-agent-cli?style=flat-square" alt="Issues">
    </a>
    <a href="https://github.com/rhodge-hash/my-agent-cli/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/rhodge-hash/my-agent-cli?style=flat-square" alt="License">
    </a>
    <a href="https://github.com/rhodge-hash/my-agent-cli/graphs/contributors">
      <img src="https://img.shields.io/github/contributors/rhodge-hash/my-agent-cli?style=flat-square" alt="Contributors">
    </a>
  </p>
  <p>
    <a href="https://github.com/rhodge-hash/my-agent-cli/issues/new?labels=bug&template=bug-report---.md">🪲 Report Bug</a>
    ·
    <a href="https://github.com/rhodge-hash/my-agent-cli/issues/new?labels=enhancement&template=feature-request---.md">🚀 Request Feature</a>
  </p>
</div>

---

## 📽️ Quick Demo

<!-- If you have a demo GIF or video, place it here. Otherwise, leave as a placeholder. -->
<p align="center">
  <img src="https://raw.githubusercontent.com/rhodge-hash/my-agent-cli/main/demo.gif" alt="Demo" width="600"/>
</p>

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Usage](#usage)
- [Extending the Agent](#extending-the-agent)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📝 About

**My-Agent CLI** is an interactive Text-based User Interface (TUI) app for working with local Large Language Models. Designed for software engineers, it empowers LLM agents with tool-use capabilities to automate and accelerate real development workflows in your terminal.

---

## ✨ Features

- ⚡ **Interactive TUI** — Fast, responsive terminal UI built with [Textual](https://textual.textualize.io/).
- 🤖 **Local LLM Integration** — Connects to local LLM servers (e.g., LM Studio, Ollama).
- 🛠️ **Smart Tool Use** — Agents suggest & execute shell commands with user confirmation.
- 🗂️ **Agent Profiles** — Easily define and switch between custom agents in `agents.yaml`.
- 🧠 **Contextual Conversations** — Maintains chat history and command context.
- 🔌 **Extensible** — Add your own tools, agents, and UI components.
- 📝 **Conversation Logging** — Tracks agent actions and responses.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A local LLM server (e.g., LM Studio, Ollama) running a compatible chat model

### Installation

```bash
git clone https://github.com/rhodge-hash/my-agent-cli.git
cd my-agent-cli
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## ⚙️ Configuration

`agents.yaml` defines your agents and their associated models.

```yaml
agents:
  - name: shell_master
    model: liquid/lfm2-1.2b # Use the model name loaded in your LLM server
    system_prompt: |
      You are a shell command master. Your goal is to accomplish the user's task by executing shell commands.
      ...
```
> **Note:** The model name must _exactly_ match the identifier in your LLM server.

---

## 🖥️ Usage

> ⚠️ **Before starting:** Make sure your LM Studio or Ollama server is running with a model loaded.

To launch the app:
```bash
python agent_tui.py
```
- **Type your prompts** in the input box and hit Enter.
- **Tool Confirmation:** The app shows proposed shell commands for your approval before running.
- **Exit:** Press <kbd>Ctrl+P</kbd>.

---

## 🧩 Extending the Agent

- **Add New Agents:** Simply edit `agents.yaml` with your agent details.
- **Add New Tools:**  
  1. Implement the tool’s function in `agent_tui.py`.  
  2. Update `parse_tool_call` to recognize your tool’s JSON format.  
  3. Instruct your agent via its `system_prompt` on how to use the new tool.

---

## 🗺️ Roadmap

- [ ] Agent Selection UI
- [ ] Dynamic Configuration
- [ ] More Tools (e.g., `write_file`, `git_commit`)
- [ ] User Confirmation Dialogs
- [ ] Improved error handling

See [open issues](https://github.com/rhodge-hash/my-agent-cli/issues) for more.

---

## 🤝 Contributing

Contributions are welcome!  
If you have ideas or improvements, feel free to:
- Fork the repo
- Create a feature branch (`git checkout -b feature/AmazingFeature`)
- Commit your changes
- Push and open a Pull Request

Or open an [issue](https://github.com/rhodge-hash/my-agent-cli/issues) with your suggestion.

#### Top Contributors

[![Contributors](https://contrib.rocks/image?repo=rhodge-hash/my-agent-cli)](https://github.com/rhodge-hash/my-agent-cli/graphs/contributors)

---

## 📄 License

This project is licensed under the [Unlicense](LICENSE).

---

## 📬 Contact

**Roy Hodge Jr.**  
GitHub: [@rhodge-hash](https://github.com/rhodge-hash)  
Email: your_email@email.com

Project Link: [https://github.com/rhodge-hash/my-agent-cli](https://github.com/rhodge-hash/my-agent-cli)

---

<p align="center"><a href="#top">⬆️ Back to top</a></p>
