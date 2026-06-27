#!/usr/bin/env python3
"""zrr-dli-job-submit - 提交DLI SQL作业"""

import subprocess
import json
import sys

def run_hcloud(service, api, region="cn-north-4", **kwargs):
    """Execute hcloud CLI command."""
    cmd = ["hcloud", service, api, "--cli-region=" + region]
    for k, v in kwargs.items():
        cmd.append("--" + k + "=" + str(v))
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error: " + result.stderr, file=sys.stderr)
        sys.exit(1)
    return result.stdout

def main():
    region = sys.argv[1] if len(sys.argv) > 1 else "cn-north-4"
    print("Executing zrr-dli-job-submit in region " + region)
    # Add specific logic here

if __name__ == "__main__":
    main()
