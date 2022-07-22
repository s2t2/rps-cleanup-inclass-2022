# rps-cleanup-2022

We created a game of rock-paper-scissors, but does it actually work as desired, and is our code as maintainable as it could be?

## Setup

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Usage

Run the rock paper scissors game:

```sh
python game.py
```

## Testing

Run tests:

```sh
pytest
```

Assessing test coverage:

```sh
coverage run -m pytest
coverage report

# (rps-env)  --->> coverage report
# Name                Stmts   Miss  Cover
# ---------------------------------------
# game.py                30      8    73%
# game_test.py           14      0   100%
# my_script.py            2      0   100%
# my_script_test.py       5      0   100%
# ---------------------------------------
# TOTAL                  51      8    84%
```

Oops looks like this is including the test files. Would need to exclude them from the report.
