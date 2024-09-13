from inventory_report.product import Product

def test_create_product() -> None:
    product = {
        "id": "1",
        "product_name": "Borracha",
        "company_name": "Papelaria Solar",
        "manufacturing_date": "2021-07-04",
        "expiration_date": "2029-02-09",
        "serial_number": "FR48",
        "storage_instructions": "Ao abrigo de luz solar",
    }
    product = Product(**product)

    assert product.id == "1"
    assert product.product_name == "Borracha"
    assert product.company_name == "Papelaria Solar"
    assert product.manufacturing_date == "2021-07-04"
    assert product.expiration_date == "2029-02-09"
    assert product.serial_number == "FR48"
    assert product.storage_instructions == "Ao abrigo de luz solar"
