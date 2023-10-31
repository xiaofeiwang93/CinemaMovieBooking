from flask import render_template
from datetime import datetime, timedelta

class CommonService:
    
    def generate_booking_dates():
        dates = {}
        today = datetime.now().date()
        for i in range(11):
            date = today + timedelta(days=i)
            if i == 0:
                dates["Today"] = date.strftime("%d/%m/%Y")
            elif i == 1:
                dates["Tomorrow"] = date.strftime("%d/%m/%Y")
            else:
                dates[date.strftime("%a %d/%m")] = date.strftime("%d/%m/%Y")
        return dates
    
    def generate_seats():
        seating_arrangement = {}

        for row in range(1, 3):  # Two rows
            for seat in range(1, 11):  # Ten seats in each row
                seat_number = (row - 1) * 10 + seat  # Calculate a unique seat number
                seating_arrangement[seat_number] = {"row": row, "seat": seat}
        
        return seating_arrangement
    

    def  raise_error(e):
        print(e)
        return render_template("/error.html", error = str(e))