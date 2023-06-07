class Reservation:
    def __init__(self, reservation_id, customer_id, table_id, reservation_time):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.table_id = table_id
        self.reservation_time = reservation_time
        self.status = None

    @classmethod
    def reserve_table(cls, reservation_id, customer_id, reservation_time):
        reservation = cls(reservation_id, customer_id, None, reservation_time)
        reservation.status = 'reserved'
        
        return reservation


    def update_reservation(self, reservation_id, table_id, reservation_time):
        if self.reservation_id == reservation_id:
            self.table_id = table_id
            self.reservation_time = reservation_time
            return True
        else:
            return False

    @classmethod
    def delete_reservation(cls, reservations, reservation_id):
        for reservation in reservations:
            if reservation.reservation_id == reservation_id:
                reservations.remove(reservation)
                return True
        return False
