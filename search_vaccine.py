#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import time
from datetime import date


# for jabalpur district id is 315, ask dev to find out the id if you are using
# it for someother location

district = "315"
age = 45

# Enter the time interval for which you want the slots to be checked (in seconds) Default is 20 mins.
time_interval = 1200

today = date.today()
date = today.strftime('%d-%m-%Y')

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}.'.format(district, date)
#import pdb; pdb.set_trace()

while True:
    msg_body = ''
    data = requests.get(url)
    for entry in data.json()['sessions']:
        if entry['available_capacity'] > 0 \
           and entry['min_age_limit'] == age:
           send_msg = True
           msg_body = "Available {} slots for {}+ in {}  , pin: {} ".format(entry['available_capacity'
                ], entry['min_age_limit'], entry['name'] , entry['pincode'])
           
           print(msg_body)
        else:
           print('No slots, checked at : ', datetime.datetime.now())
    time.sleep(time_interval)
