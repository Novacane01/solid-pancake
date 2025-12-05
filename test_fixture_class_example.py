import pytest
# Définir une fixture globale
@pytest.fixture
def sample_data():
    """Fixture qui fournit des données de test."""
    return {"name": "Alice", "age": 30}
# Définir une fixture avec une portée spécifique (scope)
@pytest.fixture(scope="class")
def setup_class_level():
    """Fixture exécutée une fois par classe de test."""
    return {"message": "Hello from class-level setup"}
# Classe de test
class TestExample:
    def test_data_content(self, sample_data):
        """Test utilisant la fixture sample_data."""
        assert sample_data["name"] == "Alice"
        assert sample_data["age"] == 30
    def test_data_modification(self, sample_data):
        """Test qui modifie les données fournies par la fixture."""
        sample_data["name"] = "Bob"
        assert sample_data["name"] == "Bob"
        assert sample_data["age"] == 30
    def test_class_fixture(self, setup_class_level):
        """Test utilisant une fixture avec une portée de classe."""
        assert setup_class_level["message"] == "Hello from class-level setup"