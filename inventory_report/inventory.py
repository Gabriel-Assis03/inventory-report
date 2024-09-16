from .product import Product
from typing import Optional, List

class Inventory:
    def __init__(self, data: Optional[List[Product]] = None) -> None:
        if data is None:
            data = []
        self._data = data
    
    @property
    def data(self) -> Optional[List[Product]]:
        return self._data
    
    def add_data(self, data: list[Product]) -> None:
        self._data.extend(data)
