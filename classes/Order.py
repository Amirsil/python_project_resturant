
import csv
from classes.Product import Product
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

    def get_total_amount(self, products):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total
    

