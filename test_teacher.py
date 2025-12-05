from Teacher import Teacher
from test_employee import TestEmployee, setup_employee
import pytest
from copy import deepcopy

@pytest.fixture(scope="class")
def setup_teacher():
    """Fixture exécutée une fois par classe de test."""
    return Teacher(first="Alice", last="Aliceson", left=1, teaching_hours=1)

class TestTeacher:
    def test_object(self, setup_teacher):
        assert setup_teacher.teaching_hours == 1

    def test_teaching_hours(self, setup_teacher):
        teacher = deepcopy(setup_teacher)
        assert teacher.teaching_hours == 1
        teacher.set_teaching_hours(10)
        assert teacher.teaching_hours == 10

    def test_str(self, setup_teacher):
        assert str(setup_teacher) == 'Alice Aliceson Alice.Aliceson@ec-nantes.fr, jours restants : 1, teaching hours : 1'.format(super().__str__(), self)