import csv

from sympy import Product
from data_export.OrderData import OrderData
from data_export.ProductData import ProductData


class OrderMain:
    def __init__(self):
        self.fileName = 'csv/OrderData.csv'
        self.Order_data = OrderData(self.fileName)
        self.orders = self.Order_data.load()
        product_data = ProductData('csv/ProductData.csv')
        self.products = product_data.load()



    def run(self):
        while True:
            print("\nOrder Options:")
            print("1. Place Order")
            print("2. Remove Product")
            print("3. Update Product Quantity")
            print("4. Get Total Amount")
            print("5. Show All Orders")
            print("6. Finish Order")
            print("7. Exit")
            

            choice = input("Enter your choice: ")

            if choice == '1':
                self.place_order()
            elif choice == '2':
                self.deleteById()
            elif choice == '3':
                self.update_product_quantity()
            elif choice == '4':
                print(f"Total Amount: {self.get_total_amount()}")
            elif choice == '5':
                self.printAll()
            elif choice == '6':
                self.clear_order()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")
