#!/usr/bin/env python3
"""Timestamp generator in multiple common formats."""

import argparse
import datetime

FORMATS = {
    "iso":      lambda t: t.isoformat(),
    "compact":  lambda t: t.strftime("%Y%m%d%H%M%S"),
    "log":      lambda t: f"[{t.strftime('%Y-%m-%d %H:%M:%S')}]",
    "filename": lambda t: t.strftime("%Y-%m-%d_%H-%M-%S"),
}


def main():
    parser = argparse.ArgumentParser(description="Generate timestamps in various formats")
    parser.add_argument("--format", default="iso", choices=list(FORMATS) + ["all"],
                        help="Output format: iso, compact, log, filename, all")
    args = parser.parse_args()

    now = datetime.datetime.now()

    if args.format == "all":
        for name, fn in FORMATS.items():
            print(f"{name + ':':<10} {fn(now)}")
    else:
        print(FORMATS[args.format](now))


if __name__ == "__main__":
    main()
