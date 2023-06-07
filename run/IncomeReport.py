from classes.IncomeReport import IncomeReport
from data_export.IncomeReportData import IncomeReportData


class IncomeReportMain:
    def __init__(self):
        self.fileName = 'csv/IncomeReport.csv'
        self.incomeReports = IncomeReportData(self.fileName).load()

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

    def run(self):
        while True:
            print("\nIncome Report Options:")
            print("1. Print Report")
            print("2. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                try:
                    self.generate_report(self.incomeReports[0])
                except IndexError:
                    print("No income reports found.")
            elif choice == '2':
                break
            else:
                print("Invalid choice. Please try again.")