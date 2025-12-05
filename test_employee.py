import pytest
from Employee import Employee
from copy import deepcopy

@pytest.fixture(scope="class")
def setup_employee():
    """Fixture exécutée une fois par classe de test."""
    return Employee(first="Alice", last="Aliceson", left=1)

class TestEmployee:
    def test_oject(self, setup_employee):
        assert setup_employee.first == "Alice"
        assert setup_employee.last == "Aliceson"
        assert setup_employee.email == "Alice.Aliceson@ec-nantes.fr"
        assert setup_employee.holiday_left == 1

    def test_name(self, setup_employee):
        assert setup_employee.fullname() == "Alice Aliceson"

    def test_holiday(self, setup_employee):
        employee = deepcopy(setup_employee)
        assert employee.holiday_left == 1
        employee.new_holiday(10)
        assert employee.holiday_left == 11

    def test_str(self, setup_employee):
        assert str(setup_employee) == "Alice Aliceson Alice.Aliceson@ec-nantes.fr, jours restants : 1"