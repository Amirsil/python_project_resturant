

from classes.Customer import Customer
# from classes.IncomeReport import IncomeReport
# from classes.Product import Product
# from classes.Reservation import Reservation
# from classes.Resturant import RestaurantFacade
# import csv

from data_export.CsvFactory import load_instances_from_csv



def main():
    RestaurantFacade("Tokio").open()






if __name__ == "__main__":
    # print(a)
    # print(a)
    print(load_instances_from_csv(Customer)[0])
    # main()
    




