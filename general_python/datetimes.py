import datetime

now = datetime.datetime.now()
print('Now:', now)

"""
see strftime() arguments
"""
date = datetime.datetime(2020, 3, 15)
print('Date:', date)
print('Weekday short:', date.strftime('%a'))
print('Weekday #:', date.strftime('%w'))
print('Day of month:', date.strftime('%d'))
print('Month full:', date.strftime('%B'))
print('Timezone:', date.strftime('%Z'))
print('UTC offset:', date.strftime('%z'))
print('Local version of date:', date.strftime('%x'))