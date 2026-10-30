import pytest
from datetime import date
import datetime
from app.main import outdated_products


@pytest.fixture()
def products_template() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "defined_date, expected",
    [
        pytest.param(date(2022, 2, 1), []),
        pytest.param(date(2022, 2, 10), ["chicken", "duck"]),
        pytest.param(date(2022, 2, 5), ["chicken"]),
        pytest.param(date(2022, 10, 10), ["salmon", "duck", "chicken"])
    ]
)
def test_outdated_products(monkeypatch: any,
                           products_template: list,
                           defined_date: any,
                           expected: list) -> None:

    monkeypatch.setattr(datetime, "date", lambda: defined_date)

    assert outdated_products(products_template) == expected
