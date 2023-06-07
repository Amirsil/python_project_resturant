from data_export.MenuData import MenuData


class MainMenu:
    def __init__(self):
        self.fileName = 'csv/MenuData.csv'
        self.menu_data = MenuData(self.fileName)
        self.products = self.menu_data.load()

    def view_menu(self):
        try:
            for product in self.products:
                print(f"{product.name=}, {product.price=}, {product.id=}")
        except Exception as e:
            print(f"An error occurred while viewing the menu: {e}")

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

    def run(self):
        while True:
            print("\nMenu Manager Options:")
            print("1. View Menu")
            print("2. Add Product to Menu")
            print("3. Delete Product from Menu")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_menu()
            elif choice == '2':
                self.AddById()
            elif choice == '3':
                self.deleteById()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
