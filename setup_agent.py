import os
import sys
import platform
import subprocess
import shutil

# --- Configuration ---
MODEL = "qwen2.5-coder"
AGENT_NAME = "ask-ollama"

def log(style, msg):
    styles = {
        "info": "\033[1;34m[INFO]\033[0m",
        "success": "\033[1;32m[SUCCESS]\033[0m",
        "error": "\033[1;31m[ERROR]\033[0m"
    }
    # Fallback for Windows CMD which sometimes struggles with ANSI
    if platform.system() == "Windows":
        print(f"[{style.upper()}] {msg}")
    else:
        print(f"{styles.get(style, '')} {msg}")

def run_cmd(cmd):
    try:
        subprocess.run(cmd, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        log("error", f"Command failed: {cmd}")
        sys.exit(1)

def install_ollama():
    system = platform.system()
    if shutil.which("ollama"):
        log("success", "Ollama is already installed.")
        return

    log("info", f"Ollama not found. Attempting install for {system}...")
    
    if system == "Linux":
        run_cmd("curl -fsSL https://ollama.com/install.sh | sh")
    elif system == "Darwin":  # macOS
        log("info", "Please download the macOS installer from https://ollama.com/download")
    elif system == "Windows":
        log("info", "Please download the Windows installer from https://ollama.com/download")
        log("info", "After installing, restart this script.")
        sys.exit(0)

def create_helper():
    system = platform.system()
    # Define directory for the script
    if system == "Windows":
        bin_dir = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "WindowsApps")
        script_path = os.path.join(bin_dir, f"{AGENT_NAME}.py")
        batch_path = os.path.join(bin_dir, f"{AGENT_NAME}.bat")
    else:
        bin_dir = os.path.expanduser("~/.local/bin")
        os.makedirs(bin_dir, exist_ok=True)
        script_path = os.path.join(bin_dir, AGENT_NAME)

    log("info", f"Creating helper at {script_path}...")

    # The actual Python logic for the agent
    content = f"""#!/usr/bin/env python3
import sys
import subprocess

def main():
    prompt = " ".join(sys.argv[1:])
    if not prompt:
        print("Usage: {AGENT_NAME} 'your prompt here'")
        return
    try:
        subprocess.run(["ollama", "run", "{MODEL}", prompt])
    except KeyboardInterrupt:
        print("\\nInterrupted by user.")
    except Exception as e:
        print(f"Error: {{e}}")

if __name__ == '__main__':
    main()
"""

    with open(script_path, "w", encoding="utf-8") as f:
        f.write(content)

    if system != "Windows":
        os.chmod(script_path, 0o755)
        log("success", f"Created {AGENT_NAME}. Ensure {bin_dir} is in your PATH.")
    else:
        # Create a batch file so Windows can run it as a command
        with open(batch_path, "w") as f:
            f.write(f'@python "{script_path}" %*')
        log("success", f"Created {AGENT_NAME}. Command should work in CMD/PowerShell.")

def main():
    log("info", "Starting Local Ollama Coding Agent Setup...")
    
    # 1. Check/Install Ollama
    install_ollama()
    
    # 2. Pull Model
    log("info", f"Pulling {MODEL}...")
    run_cmd(f"ollama pull {MODEL}")
    
    # 3. Create CLI Helper
    create_helper()
    
    log("success", "Setup finished!")

if __name__ == "__main__":
    main()