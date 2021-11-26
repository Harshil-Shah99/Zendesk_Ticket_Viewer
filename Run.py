# -*- coding: utf-8 -*-
"""
@author: hshar
"""


import requests
import math
import json
import os
from API_connect import *
from Ticket_Displayer import *
from Page_Displayer import *
from Input_Handler import *
    
# Main function where the execution begins, from which the other functions are called
def run(testing=False, testing_json=""):

    status, json_obj = connect_api()
    
    if status==0:
        return "fail"
    
    if testing:
        json_obj = testing_json
    
    if len(json_obj["tickets"])==0:
        if not testing:
            print("\nYou have no tickets left to resolve. Yayy!")
        return "pass"
    
    if testing:
        return len(json_obj["tickets"])
    
    with open('params.json') as f:
        params = json.load(f)
    username = params["username"]
    password = params["password"]
    subdomain = params["subdomain"]
            
    page_count = 0
    total_pages = math.ceil(len(json_obj["tickets"])/25)
    
    while(True):
        main_choice = input("\nMain Menu: Select your viewing choice - \n| 1:View All Tickets |\n| 2:View Individual Ticket (Newest ticket) |\n| 3:View Individual Ticket (Select ticket by ID) |\n| e:Exit |\n")
        if main_choice=='1':
            print("\nViewing all Tickets:")
            while(True):
                
                display_page(page_count, total_pages, json_obj)
                choice, page_count = take_input(page_count, total_pages)
                
                if choice=='e' or choice=='E':
                    print("\nExit to Main Menu Successful")
                    break
                
        elif main_choice=='2':
            
            print ("\n{:<12} {:<12} {:<30}".format('Ticket ID','Status','Subject'))            
            display_ticket(len(json_obj["tickets"])-1, json_obj)
            
        elif main_choice=='3':
            
            select_id = int(input("\nEnter required ticket ID:\t"))
            try:
                response = requests.get(f'https://{subdomain}.zendesk.com/api/v2/tickets/{select_id}', auth=(f'{username}', f'{password}'))
                json_ticket = response.json()["ticket"]
                print ("\n{:<12} {:<12} {:<30}".format('Ticket ID','Status','Subject'))
                print ("{:<12} {:<12} {:<30}".format(json_ticket["id"],json_ticket["status"],json_ticket["subject"]))
            except:
                print("Invalid Ticket ID")

        elif main_choice=='e' or main_choice=='E':
            print("\nExit Successful\nThank you for using my Ticket Viewer and have an awesome day!")
            break
        
        else:
            print("\nPlease enter a valid input choice")
    
    return 1