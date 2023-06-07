
import unittest
import io
from contextlib import redirect_stdout
import ast
import csv


class IncomeReport:
    def __init__(self, restaurant_name, year, month, total_income, expenses=None):
        self.restaurant_name = restaurant_name
        self.year = year
        self.month = month
        self.total_income = total_income
        if expenses is None:
            self.expenses = {}
        else:
            self.expenses = expenses

    def __str__(self):
        return f"{self.restaurant_name}, {self.year}, {self.month}, {self.total_income}, {self.expenses}"

    @staticmethod
    def generate_report(self, income_report):
        try:
            if isinstance(income_report.expenses, int):
                net_income = income_report.total_income - income_report.expenses
                print("Income Report")
                print("Restaurant Name:", income_report.restaurant_name)
                print("Year:", income_report.year)
                print("Month:", income_report.month)
                print("Total Income:", income_report.total_income)
                print("Expenses:")
                print("Total Expenses:", income_report.expenses)
            else:
                net_income = income_report.total_income - \
                    sum(income_report.expenses.values())
                print("Income Report")
                print("Restaurant Name:", income_report.restaurant_name)
                print("Year:", income_report.year)
                print("Month:", income_report.month)
                print("Total Income:", income_report.total_income)
                if income_report.expenses:
                    print("Expenses:")
                    print("Total Expenses:", sum(
                        income_report.expenses.values()))
                    print("Expenses Breakdown:")
                    for expense, amount in income_report.expenses.items():
                        print(f"{expense}: ${amount}")
                else:
                    print("No expense data available.")
            print("Net Income:", net_income)
        except Exception as e:
            print(f"An error occurred while generating the income report: {e}")
