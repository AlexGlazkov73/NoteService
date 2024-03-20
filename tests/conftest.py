import pytest

from starlette.testclient import TestClient

from app import app


@pytest.fixture(scope="module")
def test_app():
    with TestClient(app) as client:
        yield client


@pytest.fixture
def example_note():
    return {
        "text": "Hello World!",
    }
