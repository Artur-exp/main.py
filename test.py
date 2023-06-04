import datetime

cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


today = datetime.date.today()
three_days_ago = today + datetime.timedelta(days=1)

print("Today:", today)
print("Three days ago:", three_days_ago)


today2 = datetime.datetime.today()
days_up = today2 + datetime.timedelta(days=1, minutes=30, seconds=10)

print("Today:", today2.strftime('%Y-%m-%d %H:%M:%S'))
print("1 days +:", days_up.strftime('%Y-%m-%d %H:%M:%S'))