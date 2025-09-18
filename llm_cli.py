import argparse
import json
import requests
import yaml
import re
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def load_agents():
    try:
        with open("agents.yaml", "r") as f:
            return yaml.safe_load(f)["agents"]
    except FileNotFoundError:
        console.print("[bold red]Error: agents.yaml not found.[/bold red]")
        return None
    except Exception as e:
        console.print(f"[bold red]Error loading agents.yaml: {e}[/bold red]")
        return None

def run_shell_command(command):
    console.print(f"[bold yellow]Executing command:[/bold yellow] {command}")
    try:
        import subprocess
        process = subprocess.run(command, shell=True, capture_output=True, text=True)
        stdout = process.stdout
        stderr = process.stderr
        output = ""
        if stdout:
            output += f"stdout:\n{stdout}"
        if stderr:
            output += f"stderr:\n{stderr}"
        if not output:
            output = "Command executed successfully with no output."
        return output
    except Exception as e:
        return f"Error executing command: {e}"

def query_lmstudio(messages, model, host, port):
    url = f"http://{host}:{port}/v1/chat/completions"
    data = {
        "model": model,
        "messages": messages,
        "stream": False
    }
    try:
        with requests.post(url, json=data) as response:
            if response.status_code != 200:
                console.print(f"[bold red]Error from LM Studio API: {response.status_code}[/bold red]")
                console.print(f"Response body: {response.text}")
                return None
            return response.json()
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error connecting to LM Studio: {e}[/bold red]")
        return None

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
            return {
                "tool_name": "run_shell_command",
                "command": content
            }
    return None

def main():
    agents = load_agents()
    if not agents:
        return

    agent_names = [agent["name"] for agent in agents]
    parser = argparse.ArgumentParser(description="An agentic CLI to interact with local LLM servers.")
    parser.add_argument("agent_name", choices=agent_names, help="The name of the agent to run.")
    parser.add_argument("--host", default="192.168.0.104", help="The host of the LM Studio server.")
    parser.add_argument("--port", type=int, default=1234, help="The port of the LM Studio server.")
    args = parser.parse_args()

    agent = next((agent for agent in agents if agent["name"] == args.agent_name), None)
    if not agent:
        console.print(f"[bold red]Agent '{args.agent_name}' not found.[/bold red]")
        return

    agent_id = f"[bold blue]{agent['name']}-{agent['model']}-{args.host}[/bold blue]"
    console.print(f"[bold green]Starting chat with agent...[/bold green]")
    console.print(f"Agent ID: {agent_id}")
    console.print("Type 'exit' to end the conversation.")

    messages = [{"role": "system", "content": agent["system_prompt"]}]
    prompt_prefix = f"{agent_id} | [bold cyan]You: [/bold cyan]"

    while True:
        try:
            user_input = console.input(prompt_prefix)
            if user_input.lower() == 'exit':
                break

            messages.append({"role": "user", "content": user_input})

            with console.status("[bold green]Agent is thinking...", spinner="dots"):
                response = query_lmstudio(messages, agent["model"], args.host, args.port)

            if not response:
                messages.pop()
                continue

            response_text = response.get("choices", [{}])[0].get("message", {}).get("content", "")
            messages.append({"role": "assistant", "content": response_text})

            tool_code = parse_tool_call(response_text)

            if tool_code:
                console.print(Markdown(f"**Agent wants to run a tool:**"))
                console.print(tool_code)
                
                if tool_code.get("tool_name") == "run_shell_command":
                    command = tool_code.get("command")
                    if console.input("Run this command? (y/n): ").lower() == 'y':
                        tool_output = run_shell_command(command)
                        console.print(f"[bold yellow]Tool Output:[/bold yellow]\n{tool_output}")
                        messages.append({"role": "tool", "content": tool_output})
                    else:
                        console.print("Command cancelled.")
                        messages.append({"role": "tool", "content": "User cancelled the command."})
                else:
                    console.print(f"[bold red]Unknown tool: {tool_code.get('tool_name')}[/bold red]")
            else:
                console.print(Markdown(f"**Agent:**\n{response_text}"))

        except KeyboardInterrupt:
            break
    console.print("\n[bold green]Conversation ended.[/bold green]")

if __name__ == "__main__":
    main()
