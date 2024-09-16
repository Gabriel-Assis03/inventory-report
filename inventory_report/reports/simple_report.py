from ..inventory import Inventory
from ..product import Product
from .report import Report
from datetime import datetime

class SimpleReport(Report):
    inventories : list[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)
    
    def generate(self) -> str:
        return (f"Oldest manufacturing date: {self.oldest_manufacturing()}\n"
                f"Closest expiration date: {self.closest_expiration()}\n"
                f"Company with the largest inventory: {self.largest_inventory()}\n")

    def oldest_manufacturing(self):
        products: list[Product] = []
        for inventory in self.inventories:
            products.extend(inventory.data)
        oldDate = None
        for product in products:
            nowProductDate = datetime.strptime(product.manufacturing_date, '%Y-%m-%d').date()
            if oldDate is None or nowProductDate < oldDate:
                oldDate = nowProductDate
        return oldDate.strftime('%Y-%m-%d')
    
    def closest_expiration(self):
        products: list[Product] = []
        for inventory in self.inventories:
            products.extend(inventory.data)
        expirationDate = None
        now = datetime.now().date()
        for product in products:
            nowProductDate = datetime.strptime(product.expiration_date, '%Y-%m-%d').date()
            if nowProductDate >= now:
                if expirationDate is None or nowProductDate < expirationDate:
                    expirationDate = nowProductDate
        return expirationDate.strftime('%Y-%m-%d')
    
    def largest_inventory(self):
        largest: list[Product] = []
        for inventory in self.inventories:
            if len(inventory.data) > len(largest):
                largest = inventory.data
        return largest[1].company_name
