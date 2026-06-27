---
name: zrr-elb-listener
description: |
  Create and manage ELB listeners with health check configuration. Supports TCP, HTTP, and HTTPS protocols.
  触发词: 监听器, ELB listener, 负载均衡
---

# zrr-elb-listener

## Overview

Create and manage ELB listeners with health check configuration. Supports TCP, HTTP, and HTTPS protocols.

## Prerequisites

- hcloud CLI (KooCLI) installed and authenticated
- IAM user with sufficient permissions for NETWORK operations

## Workflow

1. **Validate parameters** — Check required parameters and region
2. **Execute operation** — Call the appropriate API via hcloud CLI
3. **Verify result** — Confirm the operation succeeded
4. **Report output** — Return structured result to the user

## Core Commands

```bash
# Validate and execute
hcloud NETWORK <API> --cli-region="<region>"

# Verify result
hcloud NETWORK <QueryAPI> --cli-region="<region>"
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
