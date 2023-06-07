import csv

from classes.Order import Order
from classes.Product import Product

from data_export.CsvFactory import load_instances_from_csv


class OrderMain:
    def __init__(self):
        self.orders = load_instances_from_csv(Order)
        self.products = load_instances_from_csv(Product)

    def deleteById(self):
        id = input("Enter order id to delete: ")

        try:
            id = int(id)
        except ValueError:
            print("Invalid order id. Please enter a valid integer.")
            return 

        orderToRemove = None

        for order in self.orders:
            if order.order_id == id:
                orderToRemove = order
                break

        if orderToRemove is not None:
            self.orders.remove(orderToRemove)

            with open(self.fileName, 'r') as file:
                rows = list(csv.reader(file))

            for index, row in enumerate(rows):
                if index > 0 and row[0] == str(id):
                    del rows[index]

            with open(self.fileName, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
        else:
            print(f"No order found with id: {id}")


    def printAll(self):
        for order in self.orders:
            print(f"{order.order_id=}, {order.table_id=}, {order.products=}, {order.total_amount=}, {order.customer_id=}, {order.status=}")

    def place_order(self):
        reservation_status = "confirmed"
        order_id = input("Enter order id: ")

        try:
            order_id = int(order_id)
        except ValueError:
            print("Invalid order id. Please enter a valid integer.")
            return

        for order in self.orders:
            if order.order_id == order_id:
                order.status = reservation_status
                print("Update succeeded!")
                break
        else:
            print(f"No order found with id: {order_id}")

        self.Order_data.save(self.orders)


    def clear_order(self):
        reservation_status = "finished"
        order_id = input("Enter order id: ")

        try:
            order_id = int(order_id)
        except ValueError:
            print("Invalid order id. Please enter a valid integer.")
            return

        for order in self.orders:
            if order.order_id == order_id:
                order.status = reservation_status
                print("Update succeeded!")
                break
        else:
            print(f"No order found with id: {order_id}")

        self.Order_data.save(self.orders)

        product_name = input("Enter product name: ")
        product_price = input("Enter product price: ")
        product_quantity = input("Enter product quantity: ")
        product_customer_id = input("Enter product customer id: ")

        try:
            product_price = int(product_price)
            product_quantity = int(product_quantity)
            product_customer_id = int(product_customer_id)
        except ValueError:
            print("Invalid input for product details. Please enter valid integers for price, quantity, and customer id.")
            return

        product = Product(product_name, product_price, True,
                          product_quantity, product_customer_id)
        self.products.append(product)

    def update_product_quantity(self):
        product_name = input("Enter product name: ")
        new_quantity = input("Enter new quantity: ")

        try:
            new_quantity = int(new_quantity)
        except ValueError:
            print("Invalid quantity. Please enter a valid integer.")
            return

        for product in self.products:
            if product.name == product_name:
                product.quantity = new_quantity
                print(f"Quantity updated for {product.name}")
                return
        else:
            print(f"No product found with name: {product_name}")


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
