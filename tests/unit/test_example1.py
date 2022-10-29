from monkeypatch_examples.example1 import calculate_sum


def test_calculate_sum_no_monkeypatch():
    x = calculate_sum(2, 2)
    assert x == "Sum of the 2 Numbers is `4`"


def test_calculate_sum_w_monkeypatch(monkeypatch):
    def mock_return():
        return print("NO 5 Sec Delay!!!")

    monkeypatch.setattr("monkeypatch_examples.example1.delay", mock_return)

    x = calculate_sum(2, 2)
    assert x == "Sum of the 2 Numbers is `4`"
