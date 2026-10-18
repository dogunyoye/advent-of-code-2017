#!/usr/bin/env python3
"""Run the Advent of Code 2017 solutions.

Usage:
    python run.py            # run every day
    python run.py 1 5 25     # run selected days
    python run.py --list     # list the days available
"""
import argparse
import importlib
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def available_days():
    days = [
        int(entry.name[3:])
        for entry in ROOT.glob("day[0-9][0-9]")
        if entry.is_dir() and entry.name[3:].isdigit()
    ]
    return sorted(days)


def run_day(day):
    module_name = f"day{day:02d}.day{day:02d}"
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as exc:
        print(f"Could not load {module_name}: {exc}", file=sys.stderr)
        return 1

    print(f"=== Day {day:02d} ===")
    started = time.perf_counter()
    try:
        result = module.main()
    except FileNotFoundError:
        data_file = f"day{day:02d}/day{day:02d}.txt"
        print(f"Missing input file: {data_file}", file=sys.stderr)
        return 1
    print(f"({time.perf_counter() - started:.2f}s)")
    return result or 0


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Run Advent of Code 2017 solutions.")
    parser.add_argument(
        "days",
        nargs="*",
        type=int,
        metavar="DAY",
        help="day number(s) to run, e.g. 1 or 5 6 7 (default: all)",
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="list the days available and exit",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    days = available_days()

    if args.list:
        print("Available days: " + ", ".join(f"{d:02d}" for d in days))
        return 0

    selected = args.days or days
    unknown = [d for d in selected if d not in days]
    if unknown:
        print(
            "Unknown day(s): " + ", ".join(str(d) for d in unknown),
            file=sys.stderr,
        )
        return 2

    exit_code = 0
    started = time.perf_counter()
    for day in selected:
        exit_code |= run_day(day)
    if len(selected) > 1:
        print(f"Total: {time.perf_counter() - started:.2f}s")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
