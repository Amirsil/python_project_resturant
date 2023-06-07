

import csv
from classes.Product import Product
from data_export.CsvFactory import load_instances_from_csv
from run.DutyMenu import DutyMenu
from run.IncomeReport import IncomeReportMain
from run.InventoryManagement import InventoryManagementMain
from run.MenusMenu import MenusMenu
from run.OrderMenu import OrderMain
from run.ReservationMenu import ReservationMain


class RestaurantFacade:
    def __init__(self, name):
        self.name = name
        self.products = load_instances_from_csv(Product)
        self.duty_menu = DutyMenu()

    def open_menu(self):
        print('This is our menu with appetite!')
        MenusMenu().run()

    def open_duty_menu(self):
        self.duty_menu.run()

    def open_inventory_management(self):
        InventoryManagementMain().run()

    def open_order(self):
        OrderMain().run()

    def open_reservation(self):
        ReservationMain().run()

    def open_income_report(self):
        IncomeReportMain().run()

    def open(self):
        print('Welcome to', self.name, '!')
        while True:
            print("\nMenu Manager Options:")
            print("1. Menu")
            print("2. Duty")
            print("3. Inventory Management")
            print("4. Order")
            print("5. Reservation")
            print("6. Income Report")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.open_menu()
            elif choice == '2':
                self.open_duty_menu()
            elif choice == '3':
                self.open_inventory_management()
            elif choice == '4':
                self.open_order()
            elif choice == '5':
                self.open_reservation()
            elif choice == '6':
                self.open_income_report()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")
