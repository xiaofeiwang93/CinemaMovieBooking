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
    

    def  raise_error(e):
        print(e)
        return render_template("/commonview/error.html", error = str(e))