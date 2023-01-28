from strategy import *

class Product:
    _strategy: ProductIdStrategy

    def __init__(self, strategy: ProductIdStrategy) -> None:
        self._strategy = strategy

    def get_product_id(self) -> str:
        return self._strategy.generate_product_id()

if __name__ == "__main__":
    stock = {
        "id": "1",
        "name": "Maxi Lotion",
        "category": "Skin Care",
        "sku": "6134752",
        "date_added": "2022-12-28",
    }

    ''' Generating the product id using the random strategy '''
    strategy = RandomStrategy()
    product = Product(strategy)
    print("The product id using the Random Strategy is : " + product.get_product_id())

    '''
        Generating the product id using the derived strategy
        The product is passed into to the strategy so as to extract information from it
    '''
    strategy = DerivedStrategy(stock)
    product = Product(strategy)
    print("The product id using the Derived Strategy is : " + product.get_product_id())
