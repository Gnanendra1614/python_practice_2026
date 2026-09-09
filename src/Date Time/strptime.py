from datetime import datetime

date_string = "09-09-2026"

date_object = datetime.strptime(date_string, "%d-%m-%Y")

print(date_object)