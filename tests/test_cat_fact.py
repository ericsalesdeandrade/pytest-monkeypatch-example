import pytest
from src.cat_fact import get_cat_fact


class MockResponse:
    @staticmethod
    def json():
        return {"data": ["Cats can jump up to six times their length."]}


def test_get_cat_fact(monkeypatch):
    monkeypatch.setattr("requests.get", lambda x: MockResponse())
    assert get_cat_fact() == {"data": ["Cats can jump up to six times their length."]}


@pytest.fixture
def mock_meowfacts_api(monkeypatch):
    class MockResponse:
        @staticmethod
        def json():
            return {"data": ["Cats sleep 70% of their lives."]}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)


def test_get_cat_fact_fixture(mock_meowfacts_api):
    result = get_cat_fact()
    assert result == {"data": ["Cats sleep 70% of their lives."]}
