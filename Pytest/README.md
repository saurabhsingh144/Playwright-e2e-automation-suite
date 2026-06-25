# Pytest Learning
This repository contains code examples and resources for learning Pytest, a popular testing framework for Python. The examples cover various aspects of Pytest, including test case creation, fixtures, parameterization, and more.
## Getting Started
To get started with Pytest, you can follow these steps:
1. Install Pytest using pip:
```bash 
pip install pytest
```
2. Create a test file (e.g., `test_example.py`) and add your test cases. For example:
```python 
def test_addition():
     assert 1 + 1 == 2
def test_subtraction(): 
      assert 5 - 2 == 3
```
3. Run the tests using the command line:
```bash 
pytest
```

4. Naming Conventions
``` text
1. Test files should be named starting with `test_` or ending with `_test.py` (e.g., `test_example.py`).
2. Test functions should be named starting with `test_` (e.g., `test_addition`).
3. Test classes should be named starting with `Test` (e.g., `TestMathOperations`).
4. Test methods within classes should also start with `test_` (e.g., `test_addition`).
```
## Resources
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
- [Pytest Tutorial](https://realpython.com/pytest-python-testing/)
- [Pytest Fixtures](https://docs.pytest.org/en/stable/fixture.html)
- [Pytest Parameterization](https://docs.pytest.org/en/stable/parametrize.html)

## 
