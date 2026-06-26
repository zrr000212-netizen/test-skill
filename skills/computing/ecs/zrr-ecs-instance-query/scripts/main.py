#!/usr/bin/env python3
"""zrr-ecs-instance-query - Query Huawei Cloud ECS instance list and details."""

import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="zrr-ecs-instance-query")
    parser.add_argument("--region", default=os.getenv("HW_REGION_NAME", "cn-north-4"))
    parser.add_argument("--ak", default=os.getenv("HW_ACCESS_KEY"))
    parser.add_argument("--sk", default=os.getenv("HW_SECRET_KEY"))
    args = parser.parse_args()
    print(f"Skill: zrr-ecs-instance-query")
    print(f"Region: {args.region}")
    print("OK")

if __name__ == "__main__":
    main()
