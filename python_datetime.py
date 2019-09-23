import datetime
import locale

locale.setlocale(locale.LC_ALL, 'russian')

datetime_str = '01/01/17 12:10:03.234567'
output = datetime.datetime.strptime(datetime_str, '%d/%m/%y %H:%M:%S.%f')

print(output)

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
month_ago = datetime.datetime.now() - datetime.timedelta(days=30)

print(month_ago)
print(yesterday)
print(datetime.datetime.now())