---
name: zrr-iam-policy-bind
description: |
  Batch bind IAM policies to users or groups. Supports policy lookup by name and dry-run mode.
  触发词: 策略绑定, IAM policy, 权限分配
---

# zrr-iam-policy-bind

## Overview

Batch bind IAM policies to users or groups. Supports policy lookup by name and dry-run mode.

## Prerequisites

- hcloud CLI (KooCLI) installed and authenticated
- IAM user with sufficient permissions for SECURITY operations

## Workflow

1. **Validate parameters** — Check required parameters and region
2. **Execute operation** — Call the appropriate API via hcloud CLI
3. **Verify result** — Confirm the operation succeeded
4. **Report output** — Return structured result to the user

## Core Commands

```bash
# Validate and execute
hcloud SECURITY <API> --cli-region="<region>"

# Verify result
hcloud SECURITY <QueryAPI> --cli-region="<region>"
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
