def tax_record_from_DW():
    return True


def price_record_from_DW():
    return True


def calc_price():
    Taxes = tax_record_from_DW()
    Price = price_record_from_DW()

    return Taxes + Price


def test_calc_price(monkeypatch):
    monkeypatch.setattr(
        "tests.unit.test_price.tax_record_from_DW", lambda: 10
    )  # Monkeypatching the function
    monkeypatch.setattr(
        "tests.unit.test_price.price_record_from_DW", lambda: 20
    )  # Monkeypatching the function
    value = calc_price()
    assert value == 30

    # Deleting Monkeypatched function
    monkeypatch.delattr("tests.unit.test_price.tax_record_from_DW")
    monkeypatch.delattr("tests.unit.test_price.price_record_from_DW")
