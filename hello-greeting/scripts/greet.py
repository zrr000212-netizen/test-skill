#!/usr/bin/env python3
"""Simple greeting generator supporting multiple languages."""

import argparse
import sys

GREETINGS = {
    "en": "Hello, {name}! 🌍",
    "zh": "你好，{name}！🌍",
    "ja": "こんにちは、{name}！🌍",
    "fr": "Bonjour, {name}! 🌍",
    "de": "Hallo, {name}! 🌍",
    "es": "¡Hola, {name}! 🌍",
    "ko": "안녕하세요, {name}! 🌍",
    "ru": "Привет, {name}! 🌍",
}


def main():
    parser = argparse.ArgumentParser(description="Generate greetings in multiple languages")
    parser.add_argument("--lang", default="en", help="Language code (en, zh, ja, fr, de, es, ko, ru)")
    parser.add_argument("--name", default="World", help="Name to greet")
    parser.add_argument("--list", action="store_true", help="List supported languages")
    args = parser.parse_args()

    if args.list:
        print("Supported languages:")
        for code, template in GREETINGS.items():
            print(f"  {code}: {template.format(name='...')}")
        return

    template = GREETINGS.get(args.lang)
    if not template:
        print(f"Unsupported language: {args.lang}", file=sys.stderr)
        print(f"Supported: {', '.join(GREETINGS.keys())}", file=sys.stderr)
        sys.exit(1)

    print(template.format(name=args.name))


if __name__ == "__main__":
    main()
