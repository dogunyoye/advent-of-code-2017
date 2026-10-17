# Advent of Code 2017 — Python

My Python solutions for all 25 days of
[Advent of Code 2017](https://adventofcode.com/2017), plus a small runner,
a test suite, and CI.

## Requirements

- Python 3.12+ (no third-party dependencies)

## Puzzle inputs

Advent of Code asks that puzzle inputs are not shared, so they are **not**
committed. Create a `dayNN/dayNN.txt` file next to each solution containing
that day's input:

```
day01/day01.txt
day02/day02.txt
...
day25/day25.txt
```

## Running

Run every day:

```bash
python run.py
```

Run specific days:

```bash
python run.py 1 5 25
```

List the days available:

```bash
python run.py --list
```

Each solution can also be run on its own (from the repository root):

```bash
python -m day05.day05
```

## Tests

```bash
python -m unittest discover -v
```

The example-based tests run anywhere. The full-input tests run automatically
when the corresponding `dayNN/dayNN.txt` input is present and are skipped
otherwise, so CI stays green without the private inputs.

## Structure

```
.
├── day01/ … day25/   # one package per day (solution + input)
├── tests/            # unittest suite (examples + golden answers)
└── run.py            # runner for all or selected days
```

## License

Licensed under the Apache License 2.0 — see [LICENSE](LICENSE).
