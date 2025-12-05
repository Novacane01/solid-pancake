import pytest
# content of test_sample.py
def func(x):
    return x + 1
@pytest.mark.xfail
def test_answer():
    assert func(3) == 5