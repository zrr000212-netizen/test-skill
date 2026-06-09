---
name: time-stamper
displayName: Time Stamper
description: Generate formatted timestamps for logging, filenames, and debugging in various formats.
tags: [timestamp, time, utility, logging, date]
trigger: When the user needs a timestamp or formatted date/time string.
---

## Overview

A minimal utility skill that generates timestamps in common formats for logging, filenames, and debugging.

## Core Commands

```bash
python3 scripts/stamper.py --format iso
python3 scripts/stamper.py --format compact
python3 scripts/stamper.py --format log
python3 scripts/stamper.py --format filename
python3 scripts/stamper.py --format all
```

## Output Format

```
ISO:       2026-06-09T22:50:00+08:00
Compact:   20260609225000
Log:       [2026-06-09 22:50:00]
Filename:  2026-06-09_22-50-00
```

## Verification

```bash
python3 scripts/stamper.py --format iso
# Expected: current time in ISO 8601 format
```
