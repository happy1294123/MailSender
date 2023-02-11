from datetime import datetime, timedelta
# c = 5
# while c:
#     c -= 1
#     print(c)
# exit()

# b = '5d'
# print(b[:-1])
# exit()

a = '2023-2-11 10:23:23'


# convert date string to date obj
date_obj = datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
print(date_obj) # <class 'datetime.datetime'>


# get weed number (1, monday)(7, sunday)
res = datetime.date(date_obj).isoweekday()
print(res)

# get yesterday
yesterday = (date_obj + timedelta(days=1)).strftime('%Y-%m-%d')
print(yesterday)

# format to mm/dd
final = (date_obj - timedelta(days=1)).strftime('%m/%d')
print(final)




