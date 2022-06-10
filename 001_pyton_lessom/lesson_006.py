import math
# print(math.)
# работает с радианами
# khanacademy
# corner = 90
# print(math.sin(math.radians(corner)))
import calendar
# print(calendar.month(2022, 5, w=10, l=2))
# print(calendar.calendar(1998, w=2, l=1, c=10, m=6))
# print(calendar.HTMLCalendar().formatyear(2022))
# print(calendar.weekday(2022, 6, 10))
# проверка на весокосный год
# print(calendar.isleap(2020))
# print(calendar.isleap(2010))
# print(calendar.leapdays(2000, 2021))
import time
# start = time.time()
# print(time.time())
#
# print(time.asctime())
# time.sleep(5)
# print(time.gmtime())
# stop = time.time()
#
# print(stop - start)
# год месяц число
import datetime
d = datetime.date(2020, 5, 12)
# print(d)
# print(type(d))
# идет из системы
# today = datetime.date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
# # 0-6
# print(today.weekday())
# # 1-7
# print(today.isoweekday())
# # timedelta = date1 - date2
# print(type(today - d))
# tdelta = datetime.timedelta(days=23)
# print(tdelta + today)
#
# bday = datetime.date(2023, 1, 13)
# tillbd = bday - today
# print(bday - today)
# print(tillbd.total_seconds())
t = datetime.time(13, 20, 31)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
dt = datetime.datetime(2021, 3, 12, 12, 31, 14, 5595)
print(dt.date())
print(dt.time())
dt_delta = datetime.timedelta(days=4, hours=23, minutes=21)
print(dt + dt_delta)
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
print(dt_today)
print(dt_now)

print(dt_today.strftime('%B %a %d.%m.%y'))
dt_str = 'November 30, 2020 Monday'
str_to_date = datetime.datetime.strptime(dt_str, '%B %d, %Y %A')
print(dt_today - str_to_date)

now = time.time()
print(datetime.datetime.fromtimestamp(now))

today = datetime.datetime.now()
print(datetime.datetime.timestamp(today))