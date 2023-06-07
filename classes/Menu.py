
import csv


class Menu:
    def __init__(self, products):
        self.products = products

    @staticmethod
    def view_menu(self):
        try:
            for product in self.products:
                print(f"{product.name=}, {product.price=}, {product.id=}")
        except Exception as e:
            print(f"An error occurred while viewing the menu: {e}")

    @staticmethod
    def deleteById(self):
        try:
            id = input("Enter id to delete: ")
            productToRemove = None

            for product in self.products:
                if product.id == int(id):
                    productToRemove = product
                    break

            if productToRemove is not None:
                self.products.remove(productToRemove)
                print(f"Product with ID {id} has been deleted.")
            else:
                print(f"Error: Product with ID {id} not found.")

            self.menu_data.save(self.products)
        except Exception as e:
            print(
                f"An error occurred while deleting a product from the menu: {e}")

    @staticmethod
    def AddById(self):
        try:
            id = input("Enter id to add: ")
            productToAdd = None

            for product in self.products:
                if product.id == int(id):
                    productToAdd = product
                    break

            if productToAdd is not None:
                self.products.append(productToAdd)
                print(f"Product {productToAdd.id} has been added to the menu.")
            else:
                print(f"Error: Product with id {id} does not exist.")

            self.menu_data.save(self.products)
        except Exception as e:
            print(f"An error occurred while adding a product to the menu: {e}")
