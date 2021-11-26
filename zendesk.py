# -*- coding: utf-8 -*-
"""
@author: hshah6
"""
# Code to add tickets in the file tickets.json to the ticketing system
# headers = {
   #     'Content-Type': 'application/json',
   # }
   
   # data = open('tickets.json')
   # response = requests.post(f'https://{subdomain}.zendesk.com/api/v2/imports/tickets/create_many.json', headers=headers, data=data, auth=(f'{username}', f'{password}'))

# Import required libraries
import requests
import math
import json
import os
from Run import *

if __name__ == '__main__':
    run()