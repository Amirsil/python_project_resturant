from classes.InventoryManagement import InventoryManagement
from data_export.CsvFactory import load_instances_from_csv

class InventoryManagementMain:
    def __init__(self):
        self.fileName = 'csv/InventoryManagementData.csv'
        self.InventoryManagements = load_instances_from_csv(InventoryManagement)

    def is_available(self, product_id):
        for product in self.InventoryManagements:
            if product.product_id == product_id and product.quantity > 0:
                return True
        return False

    def decrement(self, product_id):
        for product in self.InventoryManagements:
            if product.product_id == product_id and product.quantity > 0:
                product.quantity -= 1
                return
        raise ValueError("Product not found or quantity is already 0")

    def printAll(self):
        for inventoryManagement in self.InventoryManagements:
            print(
                f"{inventoryManagement.product_id=}, {inventoryManagement.product_name=}, {inventoryManagement.quantity=}")

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

    def run(self):
        while True:
            print("\nInventory Management Options:")
            print("1. is_available")
            print("2. decrement")
            print("3. printAll")
            print("4. delete")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    product_id = int(input("Enter product ID: "))
                    print(self.is_available(product_id))
                except ValueError:
                    print("Invalid input. Please enter a valid integer ID.")
            elif choice == "2":
                try:
                    product_id = int(input("Enter product ID: "))
                    self.decrement(product_id)
                    print("Quantity decremented successfully.")
                except ValueError as e:
                    print(e)
            elif choice == "3":
                self.printAll()
            elif choice == "4":
                self.deleteById()
                print("Product deleted successfully.")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")
