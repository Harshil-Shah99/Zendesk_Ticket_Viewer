# -*- coding: utf-8 -*-
"""
@author: hshar
"""
import requests
import math
import json
import os

# Function to display a particular ticket using its index value at the list of all tickets
def display_ticket(index, json_obj, testing = False):
    if testing:
        return json_obj["tickets"][index]["id"], json_obj["tickets"][index]["status"], json_obj["tickets"][index]["subject"]
    
    print ("{:<12} {:<12} {:<30}".format(json_obj["tickets"][index]["id"], json_obj["tickets"][index]["status"], json_obj["tickets"][index]["subject"]))
    
    
