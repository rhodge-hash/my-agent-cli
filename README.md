<div align="center">
  <a href="https://github.com/rhodge-hash/my-agent-cli">
    <img src="https://raw.githubusercontent.com/rhodge-hash/my-agent-cli/main/AgentApp.png?raw=true" alt="My-Agent CLI Logo" width="300" height="200">
  </a>
  
  <h1>🤖 My-Agent CLI</h1>
  <p>
    <b>A powerful, extensible TUI for interacting with local Large Language Models (LLMs) and automating software tasks.</b>
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
      <img src="https://img.shields.io/badge/license-Unlicense-blue?style=flat-square" alt="License">
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

**My-Agent CLI** is an interactive Text-based User Interface (TUI) application that helps developers interact with locally hosted Large Language Models (LLMs) and automate developer workflows safely. It provides a guided environment where LLM agents can propose actions (like shell commands) and request user confirmation before executing them.

---

## ✨ Features

- ⚡ Interactive TUI — Fast, responsive terminal UI built with Textual.
- 🤖 Local LLM Integration — Connects to local LLM servers (e.g., LM Studio, Ollama).
- 🛠️ Smart Tool Use — Agents propose shell commands and wait for user approval before execution.
- 🗂️ Agent Profiles — Define agents and switch between them using agents.yaml.
- 🧠 Contextual Conversations — Maintains chat history and command context for better continuity.
- 🔌 Extensible — Add tools, agents, and UI components easily.
- 📝 Conversation & Audit Logging — Tracks actions, responses, and executed commands.

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

Create or edit agents.yaml to define your agents and the model identifiers your local LLM server exposes.

```yaml
agents:
  - name: shell_master
    model: liquid/lfm2-1.2b # Match the model identifier in your LLM server
    system_prompt: |
      You are a shell command master. Your goal is to accomplish the user's task by proposing shell commands and explaining them. Always ask for confirmation before executing commands.
```
> Note: The model name must exactly match the identifier used by your LLM server.

---

## 🖥️ Usage

Start the app after ensuring your LLM server is running with a model loaded:

```bash
python agent_tui.py
```

- Type prompts in the input box and press Enter.
- The agent will propose actions (e.g., shell commands) and show a confirmation prompt before executing anything.
- Exit with Ctrl+P.

---

## 🧩 Extending the Agent

- Add agents by editing agents.yaml.
- Add tools by implementing functions (see tools section in the code) and updating parse_tool_call to recognize your tool's JSON.
- Write clear system prompts to teach agents how and when to use tools.

---

## 🗺️ Roadmap

- [ ] Agent Selection UI
- [ ] Dynamic Configuration
- [ ] More Tools (e.g., write_file, git_commit)
- [ ] User Confirmation Dialogs with improved UX
- [ ] Better error handling and retries

See open issues for more details: https://github.com/rhodge-hash/my-agent-cli/issues

---

## 🤝 Contributing

Contributions are welcome. Please open issues or pull requests. A suggested workflow:

- Fork the repo
- Create a feature branch (git checkout -b feature/AmazingFeature)
- Commit changes and open a pull request

Include tests or manual steps to verify behavior when possible.

### Top Contributors

[![Contributors](https://contrib.rocks/image?repo=rhodge-hash/my-agent-cli)](https://github.com/rhodge-hash/my-agent-cli/graphs/contributors)

---

## 📄 License

This project is licensed under the Unlicense. See the LICENSE file for details.

---

## 📬 Contact

**Roy Hodge Jr.**
GitHub: @rhodge-hash (https://github.com/rhodge-hash)
Email: roy@example.com

Project: https://github.com/rhodge-hash/my-agent-cli

<p align="center"><a href="#top">⬆️ Back to top</a></p>
