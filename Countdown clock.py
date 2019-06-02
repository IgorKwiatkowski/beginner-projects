#!/usr/bin/env python
# coding: utf-8

# In[10]:


import datetime
import time

month_dict = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12}

print('Hello and welcome to countdown clock. We need to establish your target time and then we will count down every 5 seconds.')

while True:

    target_year = int(input('\nWhich year? '))

    target_month = (input('\nWhich month? '))
    if type(target_month) == str:
        month_name = ''
        month_name += target_month[0]
        month_name += target_month[1]
        month_name += target_month[2]
        target_month = month_dict[month_name.lower()]

    target_day = int(input('\nWhich day? '))

    target_hour = int(input('\nWhich hour? '))

    target_minute = int(input('\nWhich minute? '))

    target_second = int(input('\nWhich second? '))

    target_date = datetime.datetime(target_year, target_month, target_day, target_hour, target_minute, target_second)
    
    if target_date < datetime.datetime.now():
        print('The date needs to be in the future.')
        continue
    break
while target_date > datetime.datetime.now():
    print(f'{target_date-datetime.datetime.now()} left until {target_date}.')
    time.sleep(5)
    
print('Target time reached.')

