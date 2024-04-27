from datetime import datetime

current_datetime = datetime.now()
print(current_datetime) # 2020-10-09 22:13:35.053819


from datetime import datetime
current_datetime = datetime.now()
print(current_datetime.year)        # 2020
print(current_datetime.month)       # 10
print(current_datetime.day)         # 09
print(current_datetime.hour)        # 22
print(current_datetime.minute)      # 32
print(current_datetime.second)      # 22
print(current_datetime.microsecond) # 819366

from datetime import datetime
current_datetime = datetime.now()
print(current_datetime.date())  # 2020-10-09
print(current_datetime.time())  # 22:13:35.053819

from datetime import datetime
d1 = datetime(year=2012, month=1, day=7, hour=14)
print(d1) # 2012-01-07 14:00:00

from datetime import datetime
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
print(seventh_day_2020.weekday())   # 1

from datetime import datetime
current_datetime = datetime.now()
future_month = (current_datetime.month % 12) + 1
future_year = current_datetime.year + int(current_datetime.month / 12)
future_datetime = datetime(future_year, future_month, 1)
print(current_datetime < future_datetime)    # True
print (future_datetime)