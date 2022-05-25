import platform
from datetime import datetime

print("="*10, "Systam Information", "="*10)
uname = platform.uname()
print(f"System:{uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
