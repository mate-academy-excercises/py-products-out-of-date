from datetime import date


def outdated_products(products: list) -> list:
    return [product["name"] for product in products
            if product["expiration_date"] < date.today()]
