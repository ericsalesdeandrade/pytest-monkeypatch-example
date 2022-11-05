import requests
from monkeypatch_examples.cat_fact import get_cat_fact


def test_cat_fact_no_monkeypatch():
    code, response = get_cat_fact()
    assert code == 200


def test_cat_fact_w_monkeypatch(monkeypatch):
    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = "www.testurl.com"

        def json(self):
            return {'data': ['Mother cats teach their '
                             'kittens to use the litter box.']}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    assert get_cat_fact() == (200, {'data': ['Mother cats '
                                             'teach their kittens '
                                             'to use the litter box.']})
