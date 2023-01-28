from abc import ABC, abstractmethod
from datetime import datetime
import string
import secrets


class ProductIdStrategy(ABC):
    """An interface for strategy type"""

    @abstractmethod
    def generate_product_id() -> None:
        """Each class will have its own implementation of this function"""
        pass


class RandomStrategy(ProductIdStrategy):

    def generate_product_id(self) -> str:
        limit = 12
        product_id = "".join(secrets.choice(
            string.ascii_uppercase+string.digits) for i in range(limit))
        return product_id


class DerivedStrategy(ProductIdStrategy):
    ''' The Derived Strategy will derive the product id from the id, category and sku of the product'''

    def __init__(self, product) -> None:
        super().__init__()
        self.product = product

    def generate_product_id(self) -> str:
        id = self.product["id"]
        # Get the first 3 characters of the category
        category = self.product["category"][:3].upper()
        sku = self.product["sku"]
        # Get the date string and replace remove the hyphens
        date = datetime.strptime(self.product["date_added"], "%Y-%m-%d").date().__str__().replace("-", "")
        product_id = "".join([category, "-", date, "-", sku, id,])
        return product_id
