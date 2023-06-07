import datetime
from classes.Reservation import Reservation
from data_export.CsvFactory import load_instances_from_csv, save_instances_to_csv


class ReservationMain:
    def __init__(self):
        self.fileName = 'ReservationData.csv'
        self.reservations = load_instances_from_csv(Reservation)

    def reserve_table(self, reservation_id, customer_id, reservation_time):
        reservation = Reservation.reserve_table(reservation_id, customer_id, reservation_time)
        self.reservations.append(reservation)
        save_instances_to_csv(self.reservations)

    def create_reservation(self, reservation_id, customer_id, table_id, reservation_time):
        reservation = Reservation.create_reservation(reservation_id, customer_id, table_id, reservation_time)
        self.reservations.append(reservation)
        save_instances_to_csv(self.reservations)

    def update_reservation(self, reservation_id, table_id, reservation_time):
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                reservation.table_id = table_id
                reservation.reservation_time = reservation_time
                save_instances_to_csv(self.reservations)
                return True
        return False

    def delete_reservation(self, reservation_id):
        if Reservation.delete_reservation(self.reservations, reservation_id):
            save_instances_to_csv(self.reservations)
            return True
        return False

    def printAll(self):
        try:
            for reservation in self.reservations:
                print(reservation.reservation_id, reservation.customer_id, reservation.table_id, 
                reservation.reservation_time)
        except Exception as e:
            print(f"An error occurred while printing reservations: {e}")

    def run(self):
        while True:
            print("\nMenu Manager Options:")
            print("1. Reserve Table")
            print("2. Update Reservation")
            print("3. Delete Reservation")
            print("4. Show all reservations")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                try:
                    reservation_id = int(input("Enter reservation ID: "))
                    customer_id = int(input("Enter customer ID: "))
                    reservation_time = datetime.fromisoformat(input("Enter reservation time ('%Y-%m-%d %H:%M:%S'): "))
                    self.reserve_table(reservation_id, customer_id, reservation_time)
                    print("Table reserved successfully.")
                except ValueError:
                    print("Invalid input. Please enter numeric values for reservation ID and customer ID.")
                except ValueError as e:
                    print(f"Invalid reservation time format: {e}. Please enter time in 'YYYY-MM-DD HH:MM:SS' format.")
            elif choice == '2':
                try:
                    reservation_id = int(input("Enter reservation ID to update: "))
                    table_id = int(input("Enter new table ID: "))
                    reservation_time = datetime.fromisoformat(input("Enter new reservation time ('%Y-%m-%d HH:MM:SS'): "))
                    if self.update_reservation(reservation_id, table_id, reservation_time):
                        print("Reservation updated successfully.")
                    else:
                        print("Reservation not found.")
                except ValueError:
                    print("Invalid input. Please enter numeric values for reservation ID and table ID.")
                except ValueError as e:
                    print(f"Invalid reservation time format: {e}. Please enter time in 'YYYY-MM-DD HH:MM:SS' format.")
            elif choice == '3':
                try:
                    reservation_id = int(input("Enter reservation ID to delete: "))
                    if self.delete_reservation(reservation_id):
                        print("Reservation deleted successfully.")
                    else:
                        print("Reservation not found.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value for reservation ID.")
            elif choice == '4':
                self.printAll()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")
