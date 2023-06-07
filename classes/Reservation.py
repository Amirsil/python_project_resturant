

from datetime import datetime
import csv
from data_export.CsvFactory import save_instances_to_csv


class Reservation:
    def __init__(self, reservation_id, customer_id, table_id, reservation_time):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.table_id = table_id
        self.reservation_time = reservation_time
        self.status = None

    def __str__(self):
        # return f"Employee ID={self.reservation_id}, Date={self.date}, Start time={self.start_time}, End time={self.end_time}"
        return f"{self.reservation_id}, {self.customer_id}, {self.table_id}, {self.reservation_time}"

    @staticmethod
    def reserve_table(self, reservation_id, customer_id, reservation_time):
        reservation = Reservation.reserve_table(
            reservation_id, customer_id, reservation_time)
        self.reservations.append(reservation)
        ReservationData(self.fileName).save(self.reservations)

    @staticmethod
    def create_reservation(self, reservation_id, customer_id, table_id, reservation_time):
        reservation = Reservation.create_reservation(
            reservation_id, customer_id, table_id, reservation_time)
        self.reservations.append(reservation)
        ReservationData(self.fileName).save(self.reservations)

    @staticmethod
    def update_reservation(self, reservation_id, table_id, reservation_time):
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                reservation.table_id = table_id
                reservation.reservation_time = reservation_time
                ReservationData(self.fileName).save(self.reservations)
                return True
        return False

    @staticmethod
    def delete_reservation(self, reservation_id):
        if Reservation.delete_reservation(self.reservations, reservation_id):
            ReservationData(self.fileName).save(self.reservations)
            return True
        return False

    @staticmethod
    def printAll(self):
        try:
            for reservation in self.reservations:
                print(
                    f"{reservation.reservation_id=}, {reservation.customer_id=}, {reservation.table_id=}, {reservation.reservation_time=}")
        except Exception as e:
            print(f"An error occurred while printing reservations: {e}")
# ReservationMain().run()
