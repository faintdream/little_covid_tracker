#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import time
from datetime import date, datetime
import json


# for jabalpur district id is 315, ask dev to find out the id if you are using
# it for someother location
district = "315"

# age could be either 18 or 45, depending on need
age = 18

# Enter the time interval for which you want the slots to be checked (in seconds) Default is 20 mins.
time_interval = 1200

today = date.today()
date = today.strftime('%d-%m-%Y')

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}.'.format(district, date)
#import pdb; pdb.set_trace()

while True:
    print('--------',datetime.now(),'--------')
    msg_body = ''
    try:
        data = requests.get(url)
    except json.decoder.JSONDecodeError:
        print('json decoder issue, may be no response from api')
    for entry in data.json()['sessions']:
        if entry['available_capacity'] > 0 \
           and entry['min_age_limit'] == age:
           send_msg = True
           msg_body = "Available {} slots for {}+ in {}  , pin: {} ".format(entry['available_capacity'
                ], entry['min_age_limit'], entry['name'] , entry['pincode'])

           print(msg_body)
        else:
           print('No vaccine slot. checked at : ', datetime.now())
    time.sleep(time_interval)

