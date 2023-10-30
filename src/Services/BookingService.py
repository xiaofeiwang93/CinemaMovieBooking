from Services.DbService import DbService


class BookingService:
    def save_booking(self, booking):
        DbService.add_record(DbService.bookingDbName, booking, DbService.bookingDbNameColumns)