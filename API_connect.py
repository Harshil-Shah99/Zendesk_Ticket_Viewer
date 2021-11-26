# -*- coding: utf-8 -*-
"""
@author: hshar
"""
import requests
import math
import json
import os

# Function to send the API request page by page fetching 100 tickets at a time and obtaining the concatenated response content as a json object
def connect_api():
    try:
        json_obj = ""
        if os.path.exists("params.json"):
            with open('params.json') as f:
                params = json.load(f)
            username = params["username"]
            password = params["password"]
            subdomain = params["subdomain"]
            
        else:
            print("\nParams file not found! Please ensure that params file is in the current directory")
            return 0, json_obj
        
    except:
        print("\nParams file not configured correctly. Follow instructions in readme")
        return 0, json_obj
    
    try:

        response = requests.get(f'https://{subdomain}.zendesk.com/api/v2/tickets.json?page[size]=100', auth=(f'{username}', f'{password}'))
        if response.status_code==200:
            json_obj = response.json()
            while(response.json()["meta"]["has_more"]==True):
                link = response.json()["links"]["next"]
                response = requests.get(link, auth=(f'{username}', f'{password}'))
                json_obj["tickets"].extend(response.json()["tickets"])
                
            return 1, json_obj
        elif response.status_code==404 or response.status_code==410:
            print("\nAPI seems to be unavailable. Please try again later")
            return 0, json_obj
        elif response.status_code==409:
            print("\nThe request encountered a conflict. Please try again later")
            return 0, json_obj
        else:
            return 0, json_obj
        
    except:
        print("Authentication failed. Please make sure that the API is up and the parameters are correctly set in params.json")
        return 0, json_obj
