from inventory_report.product import Product

def test_product_report(capsys) -> None:
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

    expected = (
        f"The product {product.id} - {product.product_name} "
        f"with serial number {product.serial_number} "
        f"manufactured on {product.manufacturing_date} "
        f"by the company {product.company_name} "
        f"valid until {product.expiration_date} "
        "must be stored according to the following instructions: "
        f"{product.storage_instructions}."
    )

    assert str(product) == expected
