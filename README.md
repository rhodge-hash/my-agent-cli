# Agent TUI

A Text-based User Interface (TUI) application for interacting with local Large Language Models (LLMs) as agents, with a focus on tool-use capabilities for automating software engineering tasks. This project serves as a foundation for building autonomous agents that can perform actions like executing shell commands, creating code, and managing Git operations.

## Features

*   **Interactive TUI:** Built with [Textual](https://textual.textualize.io/), providing a responsive and engaging terminal experience.
*   **Local LLM Integration:** Connects to local LLM servers like LM Studio (and can be extended for Ollama).
*   **Agent Configuration:** Define agents with custom system prompts and assigned models using a simple `agents.yaml` file.
*   **Tool Use:** Agents can suggest and execute shell commands, with user confirmation for safety.
*   **Conversation History:** Maintains a full conversation history, allowing agents to have context.
*   **Visual Feedback:** Clear indicators for agent activity (thinking spinner) and styled messages for user, agent, and tool outputs.
*   **Extensible:** Designed to be easily extended with new agents, tools, and UI components.

## Screenshots

_Please add your screenshots here to showcase the application._

![Screenshot 1](path/to/your/screenshot1.png)
![Screenshot 2](path/to/your/screenshot2.png)

## Setup

### Prerequisites

*   **Python 3.8+**
*   **Local LLM Server:**
    *   **LM Studio:** Download and run LM Studio. Load a compatible chat model (e.g., a Mistral 7B Instruct variant) and ensure the local server is running. Note the host (e.g., `192.168.0.104`) and port (e.g., `1234`).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/agent-tui.git
    cd agent-tui
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

### `agents.yaml`

This file defines your agents. Each agent has a `name`, the `model` it uses, and a `system_prompt` that dictates its personality and capabilities.

```yaml
agents:
  - name: shell_master
    model: liquid/lfm2-1.2b # Replace with your loaded LM Studio model
    system_prompt: |
      You are a shell command master. Your goal is to accomplish the user's task by executing shell commands.

      Think step-by-step. Reason about the task and then decide which command to run.

      When you need to execute a command, you MUST use the following format and only this format. Do not add any explanation or other text.

      ### Example
      User: List all files in the current directory, including hidden ones.
      Assistant: <tool_code>
      {
        "tool_name": "run_shell_command",
        "command": "ls -a"
      }
      </tool_code>
```

*   **`model`**: **Crucially, this must exactly match the model identifier loaded in your LM Studio (or Ollama) server.**
*   **`system_prompt`**: This is where you define the agent's role and instruct it on how to use tools. The example shows how to instruct the agent to use the `run_shell_command` tool.

## Usage

1.  **Ensure your LM Studio (or Ollama) server is running** with the desired model loaded.
2.  **Run the TUI application:**
    ```bash
    python agent_tui.py
    ```
3.  **Interact with the agent:** Type your prompts in the input box at the bottom of the terminal and press Enter.
4.  **Tool Confirmation:** If the agent suggests a shell command, the application will execute it and feed the output back to the agent. (Currently, this is auto-confirmed for simplicity in the TUI, but can be extended with a user confirmation dialog).
5.  **Quit:** Press `Ctrl+C` to exit the application.

## Extending the Agent

### Adding New Agents

Simply add new entries to your `agents.yaml` file.

### Adding New Tools

To add new capabilities (e.g., `write_file`, `read_file`, `git_commit`), you would:

1.  **Implement the tool's function** in `agent_tui.py` (similar to `run_shell_command`).
2.  **Update the `parse_tool_call` function** to recognize the new tool's JSON format.
3.  **Instruct the agent** in its `system_prompt` on how and when to use the new tool.

## Future Enhancements

*   **Agent Selection UI:** A sidebar or modal to easily switch between configured agents.
*   **Dynamic Configuration:** In-app editing of agent prompts and settings.
*   **More Tools:** Implement `write_file`, `read_file`, `git_add`, `git_commit`, etc.
*   **User Confirmation Dialogs:** For tool execution.
*   **Ollama Integration:** Make the LLM server configurable within the TUI.
*   **Error Handling:** More robust error messages and recovery.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
