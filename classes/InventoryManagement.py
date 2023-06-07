

from classes.Product import Product
import csv


class InventoryManagement:
    def __init__(self, product_id, product_name, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity

    @staticmethod
    def is_available(self, product_id):
        for product in self.InventoryManagements:
            if product.product_id == product_id and product.quantity > 0:
                return True
        return False

    @staticmethod
    def decrement(self, product_id):
        for product in self.InventoryManagements:
            if product.product_id == product_id and product.quantity > 0:
                product.quantity -= 1
                return
        raise ValueError("Product not found or quantity is already 0")

    @staticmethod
    def printAll(self):
        for inventoryManagement in self.InventoryManagements:
            print(
                f"{inventoryManagement.product_id=}, {inventoryManagement.product_name=}, {inventoryManagement.quantity=}")

    @staticmethod
    def deleteById(self):
        try:
            id = int(input("Enter id to delete: "))

            inventoryManagementToRemove = None

            for inventoryManagement in self.InventoryManagements:
                if inventoryManagement.product_id == id:
                    inventoryManagementToRemove = inventoryManagement
                    break

            if inventoryManagementToRemove:
                self.InventoryManagements.remove(inventoryManagementToRemove)

                with open(self.fileName, "r") as file:
                    rows = list(csv.reader(file))

                for index, row in enumerate(rows):
                    if index > 0 and int(row[0]) == id:
                        del rows[index]

                with open(self.fileName, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
            else:
                print("Product not found.")
        except ValueError:
            print("Invalid input. Please enter a valid integer ID.")
