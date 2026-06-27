---
name: zrr-modelarts-model-deploy
description: |
  Deploy ModelArts trained models as online inference services. Supports auto-scaling and custom flavor selection.
  触发词: 模型部署, inference, ModelArts推理
---

# zrr-modelarts-model-deploy

## Overview

Deploy ModelArts trained models as online inference services. Supports auto-scaling and custom flavor selection.

## Prerequisites

- hcloud CLI (KooCLI) installed and authenticated
- IAM user with sufficient permissions for AI operations

## Workflow

1. **Validate parameters** — Check required parameters and region
2. **Execute operation** — Call the appropriate API via hcloud CLI
3. **Verify result** — Confirm the operation succeeded
4. **Report output** — Return structured result to the user

## Core Commands

```bash
# Validate and execute
hcloud AI <API> --cli-region="<region>"

# Verify result
hcloud AI <QueryAPI> --cli-region="<region>"
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
