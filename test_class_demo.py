import pytest

# content of test_class_demo.py
class TestClassDemoInstance:
    value = 0
    def test_one(self):
        self.value = 1
        assert self.value == 1

    @pytest.mark.xfail
    def test_two(self):
        assert self.value == 1