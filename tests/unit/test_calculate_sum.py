# from monkeypatch_examples.calculate_sum import calculate_addition, my_string
from monkeypatch_examples import calculate_sum


def test_calculate_sum_no_monkeypatch() -> None:
    """
    Tests to calculate sum with NO Monkeypatch
    :return: None
    """
    x = calculate_sum.calculate_addition(2, 2)
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

    x = calculate_sum.calculate_addition(2, 2)
    assert x == "Sum of the 2 Numbers is `4`"


# Random Example
def test_return_string_monkeypatch(monkeypatch) -> None:
    def monkeypatched_function():
        return "DEF"

    monkeypatch.setattr(calculate_sum, "my_string", monkeypatched_function)

    x = calculate_sum.my_string()

    assert x == "DEF"
