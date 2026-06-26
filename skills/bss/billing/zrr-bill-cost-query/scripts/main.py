#!/usr/bin/env python3
"""zrr-bill-cost-query - Query Huawei Cloud billing and cost details."""

import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="zrr-bill-cost-query")
    parser.add_argument("--region", default=os.getenv("HW_REGION_NAME", "cn-north-4"))
    parser.add_argument("--ak", default=os.getenv("HW_ACCESS_KEY"))
    parser.add_argument("--sk", default=os.getenv("HW_SECRET_KEY"))
    args = parser.parse_args()
    print(f"Skill: zrr-bill-cost-query")
    print(f"Region: {args.region}")
    print("OK")

if __name__ == "__main__":
    main()
