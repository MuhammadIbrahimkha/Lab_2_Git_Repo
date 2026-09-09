#!/usr/bin/env python3

import platform
import shutil

print("=== Server Inventory ===")
print(f"Hostname: {platform.node()}")
print(f"OS: {platform.system()} {platform.release()}")

# Developer A:
# Add a disk usage section using shutil.disk_usage().
total, used, free = shutil.disk_usage("/")

print("=== Disk Usage ===")
print(f"Total: {total / (1024**3):.2f} GB")
print(f"Used: {used / (1024**3):.2f} GB")
print(f"Free: {free / (1024**3):.2f} GB")

# Developer B:
# Add a memory section.
# On Linux you may read /proc/meminfo.
print("=== Memory Usage ===")

with open("/proc/meminfo", "r") as f:
    meminfo = f.readlines()

for line in meminfo:
    if line.startswith("MemTotal:") or line.startswith("MemAvailable:"):
        print(line.strip())

print("========================")
