from datetime import datetime, timedelta

today = datetime.now()

future_date = today + timedelta(days=7)

print(future_date)

previous_date = today - timedelta(days=7)

print(previous_date)