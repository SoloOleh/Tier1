from datetime import datetime
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
print(seventh_day_2020.strftime('%A %d %B %Y')) # Tuesday 07 January 2020


from datetime import datetime
tenth_day_2020 = '10 January 2020'
print(datetime.strptime(tenth_day_2020, '%d %B %Y')) # 2020-01-10 00:00:00
