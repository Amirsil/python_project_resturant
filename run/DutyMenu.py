import csv

from data_export.CsvFactory import load_instances_from_csv
from classes.Duty import Duty

class DutyMenu:
    def __init__(self):
        self.fileName = 'csv/DutyData.csv'
        self.duties = load_instances_from_csv(Duty)

    def duration(self):
        try:
            for duty in self.duties:
                print(f"{duty.employee_id=}, {duty.end_time=} - {duty.start_time=}")
        except Exception as e:
            print(f"An error occurred while calculating duty durations: {e}")

    def printAll(self):
        try:
            for duty in self.duties:
                print(
                    f"{duty.employee_id=}, {duty.date=}, {duty.start_time=}, {duty.end_time=}")
        except Exception as e:
            print(f"An error occurred while printing duties: {e}")

    def deleteById(self):
        try:
            id = input("Enter id to delete: ")
            dutyToRemove = None

            for duty in self.duties:
                if duty.employee_id == int(id):
                    dutyToRemove = duty
                    break

            if dutyToRemove:
                self.duties.remove(dutyToRemove)

                with open(self.fileName, 'r') as file:
                    rows = list(csv.reader(file))

                for index, row in enumerate(rows):
                    if index > 0 and int(row[0]) == int(id):
                        del rows[index]

                with open(self.fileName, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
            else:
                print("No duty found with the given id.")
        except Exception as e:
            print(f"An error occurred while deleting duty: {e}")

    def run(self):
        while True:
            print("\nDuty Options:")
            print("1 - Show durations")
            print("2 - Delete")
            print("3 - Show all")
            print("4 - Go back")

            choice = input("Enter your choice: ")

            if choice == '1':
                print('Here are all the duties durations:')
                self.duration()
            elif choice == '2':
                self.deleteById()
            elif choice == '3':
                self.printAll()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
