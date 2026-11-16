import subprocess 
import sys 
 
def run_pip(cmd): 
    print("[Fixer] Running: " + cmd) 
    subprocess.run(cmd, shell=True) 
 
def main(): 
    print("=== Win7 AI Environment Fixer ===") 
    print("Installing stable AI libraries for legacy Windows...") 
 
    packages = ["torch==2.2.1", "numpy==1.26.4", "transformers==4.44.0", "pydantic==2.6.2", "safetensors==0.4.2", "mcp==1.1.0", "orjson==3.10.6"] 
 
    for pkg in packages: 
        if pkg.startswith("mcp"): 
            run_pip("pip install " + pkg + " --no-deps") 
        else: 
            run_pip("pip install " + pkg) 
 
    print("✅ Environment fixed! Restart your terminal.") 
 
if __name__ == "__main__": 
    main() 
