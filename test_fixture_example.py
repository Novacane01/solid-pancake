# Fichier : test_fixture_example.py
import pytest
# Définir une fixture avec @pytest.fixture
@pytest.fixture
def sample_data():
    """Fixture qui fournit des données de test."""
    return {"name": "Alice", "age": 30}

# Test utilisant la fixture
def test_data_is_correct(sample_data):
    """Vérifie que les données de la fixture sont correctes."""
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30

    # Une autre fixture plus complexe
@pytest.fixture
def compute_numbers():
    """Fixture qui fait une opération simple."""

    def compute(a, b):
        return a + b

    return compute

# Test utilisant la fixture compute_numbers
def test_compute_numbers(compute_numbers):
    """Teste une opération mathématique avec une fixture."""

    assert compute_numbers(3, 5) == 8
    assert compute_numbers(10, -2) == 8