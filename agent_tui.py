import json
import requests
import yaml
import re
import subprocess

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Input, Static


# --- Helper Functions (adapted from previous script) ---

def load_agents():
    try:
        with open("agents.yaml", "r") as f:
            return yaml.safe_load(f)["agents"]
    except FileNotFoundError:
        return None

def query_lmstudio(messages, model, host, port):
    url = f"http://{host}:{port}/v1/chat/completions"
    data = {"model": model, "messages": messages, "stream": False}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def parse_tool_call(response_text):
    match = re.search(r'<tool_code>(.*?)</tool_code>', response_text, re.DOTALL)
    if match:
        content = match.group(1).strip()
        try:
            data = json.loads(content)
            if isinstance(data, dict) and data.get("tool_name") == "run_shell_command":
                return data
        except json.JSONDecodeError:
            pass
        if "\n" not in content and "{" not in content:
            return {"tool_name": "run_shell_command", "command": content}
    return None

def run_shell_command(command):
    try:
        process = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = f"stdout:\n{process.stdout}\nstderr:\n{process.stderr}"
        return output.strip()
    except Exception as e:
        return f"Error executing command: {e}"

# --- TUI Widgets ---

class ChatLog(Static):
    """A widget to display the chat history."""

class AgentApp(App):
    """A Textual app for interacting with agents."""

    CSS_PATH = "agent_tui.tcss"
    BINDINGS = [("ctrl+c", "quit", "Quit")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.host = "192.168.0.104" # Hardcoded for now
        self.port = 1234 # Hardcoded for now

    def compose(self) -> ComposeResult:
        self.agent = load_agents()[0] # Load the first agent by default
        self.messages = [{"role": "system", "content": self.agent["system_prompt"]}]
        
        agent_id_str = f"[bold blue]{self.agent['name']}[/bold blue] ([italic]{self.agent['model']}[/italic] @ [green]{self.host}:{self.port}[/green])"

        yield Header(name=f"Agent TUI - {self.agent['name']}")
        yield Container(
            Static(f"[bold white]Active Agent:[/bold white] {agent_id_str}", classes="status_message"),
            ChatLog(id="chat_log"),
            id="app_body"
        )
        yield Input(placeholder="Enter your prompt...", id="prompt_input")
        yield Footer()

    async def on_mount(self) -> None:
        self.query_one(Input).focus()

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        prompt = event.value
        if not prompt:
            return

        log = self.query_one(ChatLog)
        log.mount(Static(f"[bold cyan]🧑 You:[/bold cyan] {prompt}", classes="user_message"))
        self.messages.append({"role": "user", "content": prompt})
        self.query_one("#prompt_input").clear()
        self.query_one("#prompt_input").disabled = True
        log.mount(Static("🤔 Agent is thinking...", classes="status_message", id="status"))
        self.run_worker(self.get_agent_response, thread=True)

    def get_agent_response(self) -> None:
        response = query_lmstudio(
            self.messages,
            self.agent["model"],
            self.host,
            self.port
        )
        self.call_from_thread(self.process_response, response)

    def process_response(self, response) -> None:
        log = self.query_one(ChatLog)
        log.query_one("#status").remove()

        if response.get("error"):
            log.mount(Static(f"[bold red]❌ Error:[/bold red] {response['error']}", classes="tool_message"))
            self.query_one("#prompt_input").disabled = False
            return

        response_text = response.get("choices", [{}])[0].get("message", {}).get("content", "")
        self.messages.append({"role": "assistant", "content": response_text})
        log.mount(Static(f"[bold green]🤖 Agent:[/bold green]\n{response_text}", classes="agent_message"))

        tool_code = parse_tool_call(response_text)
        if tool_code and tool_code.get("tool_name") == "run_shell_command":
            command = tool_code.get("command")
            # For safety, ask for confirmation in the UI
            log.mount(Static(f"[bold yellow]🛠️ Agent wants to run command:[/bold yellow] {command}", classes="tool_message"))
            # For now, auto-confirm for simplicity in TUI, but this should be a dialog
            tool_output = run_shell_command(command)
            log.mount(Static(f"[bold yellow]✅ Tool Output:[/bold yellow]\n{tool_output}", classes="tool_message"))
            self.messages.append({"role": "tool", "content": tool_output})
            self.run_worker(self.get_agent_response, thread=True) # Let the agent react to the tool output
        else:
            self.query_one("#prompt_input").disabled = False

if __name__ == "__main__":
    app = AgentApp()
    app.run()