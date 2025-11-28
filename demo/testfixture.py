import pytest


@pytest.fixture
def setup_environment(scope = "local"):
    print("setup environment")
    yield "environment is ready for testing"
    print("teardown environment")

def test_example_action(setup_environment):
    print(f" executing my first test with fixture:{setup_environment}")
    assert setup_environment == "environment is ready for testing"

def test_examplee_action(setup_environment):
     print(f" executing my another test with fixture:{setup_environment}")
     assert  " ready " in setup_environment
