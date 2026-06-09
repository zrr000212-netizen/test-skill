---
name: hello-greeting
displayName: Hello Greeting
description: A simple greeting skill that says hello in multiple languages and formats.
tags: [greeting, hello, utility]
trigger: When the user asks to generate a greeting or say hello.
---

## Overview

A minimal utility skill that generates greetings in various languages and styles.

## Core Commands

```bash
python3 scripts/greet.py --lang en --name "World"
python3 scripts/greet.py --lang zh --name "世界"
python3 scripts/greet.py --lang ja --name "世界"
python3 scripts/greet.py --list
```

## Output Format

```
Hello, World! 🌍
你好，世界！🌍
こんにちは、世界！🌍
```

## Verification

```bash
python3 scripts/greet.py --lang en --name "Test"
# Expected: Hello, Test! 🌍
```
