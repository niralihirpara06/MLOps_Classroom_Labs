LAB 01 – MLOps (IE-7374)

This lab introduces foundational MLOps concepts through hands-on exercises with GitHub, virtual environments, testing frameworks, and CI/CD automation. 
The goal is to create a reproducible Python project that integrates unit testing and GitHub Actions.

-------------------------------------------------------------------------------
1. OBJECTIVE
-------------------------------------------------------------------------------
- Learn to create and manage a virtual environment for project isolation.
- Build modular Python code and test it with both pytest and unittest.
- Implement Continuous Integration (CI) pipelines using GitHub Actions.
- Understand how automated testing ensures reliability and reproducibility.

-------------------------------------------------------------------------------
2. PROJECT STRUCTURE
-------------------------------------------------------------------------------
Lab1/
│
├── data/                     # Placeholder for datasets or input files
│   └── __init__.py
│
├── src/                      # Core Python logic
│   ├── __init__.py
│   └── calculator.py
│
├── test/                     # Unit test files
│   ├── __init__.py
│   ├── test_pytest.py
│   └── test_unittest.py
│
├── .github/                  # GitHub Actions workflows for CI/CD
│   └── workflows/
│       ├── github_lab1_pytest_action.yml
│       └── github_lab2_unittest_action.yml
│
├── requirements.txt          # Python dependencies
├── .gitignore                # Ignored files and folders (e.g., .venv, __pycache__)
└── README.txt                # Documentation (this file)

-------------------------------------------------------------------------------
3. STEP-BY-STEP IMPLEMENTATION
-------------------------------------------------------------------------------

STEP 1: CREATE AND ACTIVATE A VIRTUAL ENVIRONMENT
-------------------------------------------------
python -m venv .venv
.\.venv\Scripts\activate
pip install --upgrade pip

STEP 2: INSTALL DEPENDENCIES
----------------------------
Add dependencies to requirements.txt:
pytest
Then install:
pip install -r requirements.txt

STEP 3: CREATE SOURCE CODE (src/calculator.py)
----------------------------------------------
def fun1(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x + y

def fun2(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def fun3(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def fun4(x, y, z):
    return x + y + z

STEP 4: WRITE UNIT TESTS
------------------------
PYTEST (test/test_pytest.py)
----------------------------
import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5

def test_fun2():
    assert calculator.fun2(5, 2) == 3

def test_fun3():
    assert calculator.fun3(2, 3) == 6

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10

UNITTEST (test/test_unittest.py)
--------------------------------
import unittest
from src import calculator

class TestCalculator(unittest.TestCase):
    def test_fun1(self): self.assertEqual(calculator.fun1(2, 3), 5)
    def test_fun2(self): self.assertEqual(calculator.fun2(5, 2), 3)
    def test_fun3(self): self.assertEqual(calculator.fun3(2, 3), 6)
    def test_fun4(self): self.assertEqual(calculator.fun4(2, 3, 5), 10)

if __name__ == "__main__":
    unittest.main()

STEP 5: RUN TESTS LOCALLY
-------------------------
pytest -q
python -m unittest -q

Expected output:
pytest: 8 passed
unittest: 4 tests passed

STEP 6: CONFIGURE GITHUB ACTIONS (CI/CD)
----------------------------------------
.github/workflows/github_lab1_pytest_action.yml
------------------------------------------------
name: Lab1 - Pytest
on: [push, pull_request]

jobs:
  pytest:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: Lab1
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - run: python -m pip install --upgrade pip
      - run: pip install -r requirements.txt
      - run: pytest -q

.github/workflows/github_lab2_unittest_action.yml
-------------------------------------------------
name: Lab1 - Unittests
on: [push, pull_request]

jobs:
  unittest:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: Lab1
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - run: python -m pip install --upgrade pip
      - run: pip install -r requirements.txt
      - run: python -m unittest -q

-------------------------------------------------------------------------------
4. .GITIGNORE
-------------------------------------------------------------------------------
.venv/
__pycache__/
*.pyc
*.pyo
*.log
*.xml

-------------------------------------------------------------------------------
5. RESULTS
-------------------------------------------------------------------------------
| Framework      | Tests Run | Result |
|----------------|------------|--------|
| pytest         | 8          | PASSED |
| unittest       | 4          | PASSED |
| GitHub Actions | Automated  | SUCCESS |

-------------------------------------------------------------------------------
6. KEY TAKEAWAYS
-------------------------------------------------------------------------------
- Virtual environments ensure reproducibility.
- Automated CI pipelines provide early feedback and maintain code quality.
- Both Pytest and Unittest frameworks are essential for reliable ML workflows.

-------------------------------------------------------------------------------
Author: Your Name
Course: IE-7374 – MLOps
Institution: Northeastern University
Instructor: Prof. Ramin Mohammadi
-------------------------------------------------------------------------------
