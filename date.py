import datetime
import csv
import os

#To set the date to today when initiating the program, (delete and re)generate the file
try:
    os.remove("day.csv")
except FileNotFoundError:
    pass
if not os.path.exists('day.csv'):
    with open('day.csv', 'w', newline="") as date_file:
        today = datetime.date.today()
        #strftime: datetime to string
        today_string = today.strftime("%Y-%m-%d")
        fields = ["date"]
        date_writer = csv.DictWriter(date_file, fieldnames=fields)
        date_writer.writeheader()
        date_writer.writerow({"date": today_string})
        print("Date file created")

#to be able to work with the date throughout the program:
def get_day():
    with open("day.csv", "r") as day_file:
        reader = csv.reader(day_file)
        next(reader)
        for line in reader:
            today = line[0]
            day = datetime.datetime.strptime(today, "%Y-%m-%d").date()
            return day

#print(get_day())