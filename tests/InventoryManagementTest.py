
      
from InventoryManagement import InventoryManagement
from Menu import Product


class TestInventoryManagement:
    def test_is_available(self):
        product1 = Product(1, 'Tomato', 10)
        product2 = Product(2, 'Milk', 0)
        inventory = InventoryManagement([product1, product2])

        assert inventory.is_available(1) == True
        assert inventory.is_available(2) == False
        assert inventory.is_available(3) == False

    def test_decrement(self):
        product1 = Product(1, 'Tomato', 10)
        product2 = Product(2, 'Milk', 0)
        inventory = InventoryManagement([product1, product2])

        inventory.decrement(1)
        assert product1.quantity == 9

        try:
            inventory.decrement(2)
        except ValueError as e:
            assert str(e) == "Product not found or quantity is already 0"
        else:
            assert False, "Expected ValueError but no exception was raised"

        try:
            inventory.decrement(3)
        except ValueError as e:
            assert str(e) == "Product not found or quantity is already 0"
        else:
            assert False, "Expected ValueError but no exception was raised"
