import os
import subprocess

def main():
    print("=== Terminal Agent (Type 'exit' to quit) ===")
    while True:
        try:
            user_input = input("\nAgent> ")
            if user_input.lower() in ['exit', 'quit']:
                break
            
            if user_input.startswith("run "):
                cmd = user_input[4:]
                print(f"Executing: {cmd}")
                res = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="gbk")
                print(res.stdout + res.stderr)
            elif user_input == "help":
                print("Commands:\n  run <cmd> : Execute a system command\n  help      : Show this menu")
            else:
                print(f"[Agent] I received: '{user_input}'. (LLM integration pending...)")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
