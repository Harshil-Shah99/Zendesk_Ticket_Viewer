# -*- coding: utf-8 -*-
"""
@author: hshar
"""

import requests
import math
import json
import os
from Ticket_Displayer import display_ticket

# Function to display a single page of tickets, capped at 25 tickets per page
# Works by passing the current page number and printing all tickets from 25
# times that page number to a maximum of 25 tickets
def display_page(page_count, total_pages, json_obj, testing = False):
    if page_count==total_pages-1:
        end_of_range = len(json_obj["tickets"])
        entry_count = len(json_obj["tickets"])-25*page_count
    else:
        end_of_range = 25*(page_count+1)
        entry_count = 25
      
    if testing:    
        if page_count>=total_pages:
            return "error", "error"
        return end_of_range, entry_count
    
    print("\nThis is page  - " + str(page_count+1) + " of " + str(total_pages) + " | Showing " + str(entry_count) + " entries:\n")
    
    print ("{:<12} {:<12} {:<30}".format('Ticket ID','Status','Subject'))
    for index in range(25*page_count, end_of_range):
        display_ticket(index, json_obj)