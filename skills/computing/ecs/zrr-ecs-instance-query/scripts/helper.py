#!/usr/bin/env python3
"""Helper utilities for zrr-ecs-instance-query - v9"""

def validate_region(region: str) -> bool:
    valid = ["cn-north-4", "cn-north-1", "cn-south-1", "cn-east-3"]
    return region in valid

def format_output(data: dict) -> str:
    return str(data)
