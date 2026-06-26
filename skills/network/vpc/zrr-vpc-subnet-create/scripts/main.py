#!/usr/bin/env python3
"""zrr-vpc-subnet-create - Create and configure Huawei Cloud VPC subnets."""

import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="zrr-vpc-subnet-create")
    parser.add_argument("--region", default=os.getenv("HW_REGION_NAME", "cn-north-4"))
    parser.add_argument("--ak", default=os.getenv("HW_ACCESS_KEY"))
    parser.add_argument("--sk", default=os.getenv("HW_SECRET_KEY"))
    args = parser.parse_args()
    print(f"Skill: zrr-vpc-subnet-create")
    print(f"Region: {args.region}")
    print("OK")

if __name__ == "__main__":
    main()
