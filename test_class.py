import pytest
# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    @pytest.mark.xfail
    def test_two(self):
        x = "hello"
        # hasattr() method returns true if an object has the
        # given named attribute and false if it does not
        assert hasattr(x, "check")