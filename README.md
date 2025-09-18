<a id="readme-top"></a>

<br />
<div align="center">
<a href="https://github.com/rhodge-hash/my-agent-cli">
<img src="https://raw.githubusercontent.com/rhodge-hash/my-agent-cli/main/AgentApp.png?raw=true" alt="Logo" width="300" height="200">
</a>

<h3 align="center">My-Agent CLI</h3>

<p align="center">
A Text-based User Interface (TUI) application for interacting with local Large Language Models (LLMs) as agents, with a focus on tool-use capabilities for automating software engineering tasks.
<br />
<br />
<a href="https://github.com/rhodge-hash/my-agent-cli"><strong>Explore the Repo »</strong></a>
<br />
<br />
<a href="https://github.com/rhodge-hash/my-agent-cli/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
&middot;
<a href="https://github.com/rhodge-hash/my-agent-cli/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
</p>
</div>

<details>
<summary>Table of Contents</summary>
<ol>
<li>
<a href="#about-the-project">About The Project</a>
<ul>
<li><a href="#built-with">Built With</a></li>
</ul>
</li>
<li>
<a href="#getting-started">Getting Started</a>
<ul>
<li><a href="#prerequisites">Prerequisites</a></li>
<li><a href="#installation">Installation</a></li>
</ul>
</li>
<li><a href="#configuration">Configuration</a></li>
<li><a href="#usage">Usage</a></li>
<li><a href="#roadmap">Roadmap</a></li>
<li><a href="#extending-the-agent">Extending the Agent</a></li>
<li><a href="#contributing">Contributing</a></li>
<li><a href="#license">License</a></li>
<li><a href="#contact">Contact</a></li>
</ol>
</details>

About The Project

My-Agent CLI is a Text-based User Interface (TUI) for interacting with local Large Language Models (LLMs). The project focuses on giving these LLM agents tool-use capabilities to automate software engineering tasks. This tool serves as a foundation for building autonomous agents that can perform actions like executing shell commands and managing Git operations.

Key Features:

+    Interactive TUI: A responsive terminal experience built with Textual.

 +   Local LLM Integration: Connects to local LLM servers like LM Studio and Ollama.

  +   Tool Use: Agents can suggest and execute shell commands with user confirmation.
    - Agent Configuration: Define custom agents and their models using a simple agents.yaml file.
    - Conversation History: Maintains context for the agent's actions.
    - Extensible: Easily add new agents, tools, and UI components.

Built With:
    - Python
    - Textual
    - LM Studio
    
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Getting Started

Follow these steps to get a local copy up and running.

#### Prerequisites

    Python 3.8+
    Local LLM Server: Download and run a server like LM Studio/Ollama. Load a compatible chat model and ensure the local server is running.

### Installation

    Clone the repository:
```bash
git clone https://github.com/rhodge-hash/my-agent-cli.git
cd my-agent-cli
```
Create and activate a virtual environment:
```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
Install dependencies:
```
    pip install -r requirements.txt
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Configuration

agents.yaml

This file defines your agents. Each agent has a name, the model it uses, and a system_prompt that dictates its role and capabilities.
YAML

agents:
  - name: shell_master
    model: liquid/lfm2-1.2b # Replace with your loaded LM Studio model
    system_prompt: |
      You are a shell command master. Your goal is to accomplish the user's task by executing shell commands.
      ...

Note: The model name must exactly match the identifier loaded in your LLM server.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

:::info
    Ensure your LM Studio or Ollama server is running with a model loaded.
:::

 Run the application:
```
    python agent_tui.py
```
 Interact with the agent: Type your prompts in the input box and press Enter.
 Tool Confirmation: The application executes suggested shell commands and feeds the output back to the agent.
 Quit: Press Ctrl+P to exit the application.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Roadmap

    [ ] Agent Selection UI

    [ ] Dynamic Configuration

    [ ] More Tools (e.g., write_file, git_commit)

    [ ] User Confirmation Dialogs

    [ ] More robust error handling

See the open issues for a full list of proposed features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

Extending the Agent

Adding New Agents

Simply add new entries to your agents.yaml file.

Adding New Tools

    Implement the tool's function in agent_tui.py.

    Update the parse_tool_call function to recognize the new tool's JSON format.

    Instruct the agent in its system_prompt on how to use the new tool.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

    Fork the Project

    Create your Feature Branch (git checkout -b feature/AmazingFeature)

    Commit your Changes (git commit -m 'Add some AmazingFeature')

    Push to the Branch (git push origin feature/AmazingFeature)

    Open a Pull Request

#### Top contributors:

<a href="https://github.com/rhodge-hash/my-agent-cli/graphs/contributors">
<img src="https://contrib.rocks/image?repo=rhodge-hash/my-agent-cli" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### License

This project is licensed under the Unlicense. See the LICENSE file for more details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

Contact

Roy Hodge Jr. - @rhodge-hash - your_email@email.com

Project Link: https://github.com/rhodge-hash/my-agent-cli

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[]: #
[contributors-url]: https://www.google.com/search?q=%5Bhttps://github.com/rhodge-hash/my-agent-cli/graphs/contributors%5Dhttps://github.com/rhodge−hash/my−agent−cli/graphs/contributors
[]: #
[forks-url]: https://www.google.com/search?q=%5Bhttps://github.com/rhodge-hash/my-agent-cli/network/members%5Dhttps://github.com/rhodge−hash/my−agent−cli/network/members
[]: #
[stars-url]: https://www.google.com/search?q=%5Bhttps://github.com/rhodge-hash/my-agent-cli/stargazers%5Dhttps://github.com/rhodge−hash/my−agent−cli/stargazers
[]: #
[issues-url]: https://www.google.com/search?q=%5Bhttps://github.com/rhodge-hash/my-agent-cli/issues%5Dhttps://github.com/rhodge−hash/my−agent−cli/issues
[]: #
[license-url]: https://www.google.com/search?q=%5Bhttps://github.com/rhodge-hash/my-agent-cli/blob/main/LICENSE%5Dhttps://github.com/rhodge−hash/my−agent−cli/blob/main/LICENSE
[]: #
[linkedin-url]: https://www.google.com/search?q=%5Bhttps://linkedin.com/in/royhodgejr%5Dhttps://linkedin.com/in/royhodgejr
