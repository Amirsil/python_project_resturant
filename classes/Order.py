
import csv
from classes.Product import Product,ProductData
from classes.Table import Table
from classes.Menu import Menu




class Order:
    def __init__(self, order_id, table_id, products, total_amount, customer_id, status):
        self.order_id = order_id
        self.table_id = table_id
        self.products = products
        self.total_amount = total_amount
        self.customer_id = customer_id
        self.status = status

    @staticmethod
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

    @staticmethod
    def printAll(self):
        for order in self.orders:
            print(f"{order.order_id=}, {order.table_id=}, {order.products=}, {order.total_amount=}, {order.customer_id=}, {order.status=}")

    @staticmethod
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
    @staticmethod
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

    @staticmethod
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

    def get_total_amount(self, products):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total