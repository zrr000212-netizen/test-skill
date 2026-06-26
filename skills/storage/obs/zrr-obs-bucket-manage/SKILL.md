---
name: zrr-obs-bucket-manage
description: "Manage Huawei Cloud OBS buckets: create, delete, list buckets."
---

# zrr obs bucket manage | sed 's/  / /g'

## Overview

Manage Huawei Cloud OBS buckets: create, delete, list buckets.

## Prerequisites

- Python >= 3.8
- huaweicloudsdkcore >= 3.0.0

## Usage

```bash
python3 scripts/main.py --region cn-north-4
```

## Parameters

| Parameter | Description | Required | Default |
|-----------|-------------|----------|---------|
| --region | Target region code | No | cn-north-4 |
| --ak | Access Key AK | No | HW_ACCESS_KEY env var |
| --sk | Secret Key SK | No | HW_SECRET_KEY env var |
