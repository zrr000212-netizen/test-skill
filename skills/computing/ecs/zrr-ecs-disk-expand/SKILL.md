---
name: zrr-ecs-disk-expand
description: |
  Expand ECS system disk or data disk capacity via hcloud CLI. Supports online expansion without stopping the instance.
  触发词: 扩容磁盘, ECS disk expand, 磁盘扩容
---

# zrr-ecs-disk-expand

## Overview

Expand ECS system disk or data disk capacity via hcloud CLI. Supports online expansion without stopping the instance.

## Prerequisites

- hcloud CLI (KooCLI) installed and authenticated
- IAM user with sufficient permissions for COMPUTING operations

## Workflow

1. **Validate parameters** — Check required parameters and region
2. **Execute operation** — Call the appropriate API via hcloud CLI
3. **Verify result** — Confirm the operation succeeded
4. **Report output** — Return structured result to the user

## Core Commands

```bash
# Validate and execute
hcloud COMPUTING <API> --cli-region="<region>"

# Verify result
hcloud COMPUTING <QueryAPI> --cli-region="<region>"
```

## Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `region` | Yes | cn-north-4 | Huawei Cloud region |

## Output Format

| Step | Output |
|------|--------|
| 1. Validate | Parameter check result |
| 2. Execute | API call status and resource ID |
| 3. Verify | Resource state confirmation |
| 4. Report | Structured result summary |

## Best Practices

- Always specify the region explicitly
- Use --cli-jsonInput for complex parameters
- Verify operations before reporting success
