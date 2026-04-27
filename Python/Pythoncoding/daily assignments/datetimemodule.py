import datetime

current_datetime = datetime.datetime.now()
print(f"Current date and time: {current_datetime}")

date1 = datetime.date(2023, 1, 1)
date2 = datetime.date(2023, 12, 31)
days_difference = (date2 - date1).days
print(f"Number of days between {date1} and {date2}: {days_difference} days")

formatted_date = current_datetime.strftime("%d-%m-%Y")
print(f"Formatted current date: {formatted_date}")