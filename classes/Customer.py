
from classes.Order import Order
from classes.Person import Person
from classes.Table import Table


class Customer(Person):
    def __init__(self, name, phone, email, id):
        super().__init__(name, phone, email, id)
    
    def __str__(self):
        return f"Customer: name={self.name}, phone={self.phone}, email={self.email}, id={self.id}"

    def place_order(self, order_id, table_id, products, total_amount, reservation_status):
        order = Order(order_id, table_id, products, total_amount)
        if reservation_status == "reserved":
            print(
                f"{self.name} was seated at the designated table {table_id} as per the reservation.")
        elif reservation_status == "available":
            print(f"{self.name} was seated at an available table {table_id}.")
        else:
            print("Invalid reservation status.")

    @staticmethod
    def duration(self):
        try:
            for duty in self.duties:
                print(f"{duty.employee_id=}, {duty.end_time=} - {duty.start_time=}")
        except Exception as e:
            print(f"An error occurred while calculating duty durations: {e}")

    @staticmethod
    def printAll(self):
        try:
            for duty in self.duties:
                print(
                    f"{duty.employee_id=}, {duty.date=}, {duty.start_time=}, {duty.end_time=}")
        except Exception as e:
            print(f"An error occurred while printing duties: {e}")

    @staticmethod
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
