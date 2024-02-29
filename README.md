# Balance-bots assignment
Solution to balance bots assignment.

To run the application, make sure atleast python 3.11 is installed locally.

To execute the default set of instructions (found in `input.txt`), run the following:

```
python main.py
```

In order to run the unit & integration tests, the dependencies in `requirements.txt` need to be installed.
Create a virtual env (if virtual env is not installed, install it via: `pip install virtualenv`):

```
python -m virtualenv venv
```

Activate the virtual environment:

```
. ./venv/bin/activate
```

And install the dependencies:

```
pip install -r requirements.txt
```

Then the tests can be run with:

```
pytest
```

## Answers
### Part 1:
`bot 73` is responsible for comparing microchips 17 & 61

### Part 2:
- Output 0: 5
- Output 1: 13
- Output 2: 61

5 * 13 * 61 = `3965`
