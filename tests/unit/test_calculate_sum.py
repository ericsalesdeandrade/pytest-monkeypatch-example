from monkeypatch_examples.calculate_sum import calculate_sum


def test_calculate_sum_no_monkeypatch() -> None:
    """
    Tests to calculate sum with NO Monkeypatch
    :return: None
    """
    x = calculate_sum(2, 2)
    assert x == "Sum of the 2 Numbers is `4`"


def test_calculate_sum_w_monkeypatch(monkeypatch) -> None:
    """
    Test to calculate sum WITH monkeypatch (delay function)
    :param monkeypatch:
    :return: None
    """
    def mock_return():
        return print("NO 5 Sec Delay!!!")

    monkeypatch.setattr("monkeypatch_examples.calculate_sum.delay", mock_return)

    x = calculate_sum(2, 2)
    assert x == "Sum of the 2 Numbers is `4`"
