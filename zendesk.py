# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 03:36:38 2021

@author: hshah6
"""
 # headers = {
    #     'Content-Type': 'application/json',
    # }
    
    # data = open('tickets.json')
    # response = requests.post(f'https://{subdomain}.zendesk.com/api/v2/imports/tickets/create_many.json', headers=headers, data=data, auth=(f'{username}', f'{password}'))

import requests
import math
import json
import os
import pprint

def display_ticket(index, json_obj):
    print ("{:<12} {:<12} {:<30}".format(json_obj["tickets"][index]["id"], json_obj["tickets"][index]["status"], json_obj["tickets"][index]["subject"]))
    
def display_page(page_count, total_pages, json_obj):
    if page_count==total_pages-1:
        end_of_range = len(json_obj["tickets"])
        entry_count = len(json_obj["tickets"])-25*page_count
    else:
        end_of_range = 25*(page_count+1)
        entry_count = 25
        
    print("\nThis is page  - " + str(page_count+1) + " of " + str(total_pages) + " | Showing " + str(entry_count) + " entries:\n")
    
    print ("{:<12} {:<12} {:<30}".format('Ticket ID','Status','Subject'))
    for index in range(25*page_count, end_of_range):
        display_ticket(index, json_obj)

def take_input(page_count, total_pages):
    choice = input("\nPress - | r:Next Page | l:Previous Page | e:Exit to Main Menu | -\t")
    if choice=='r':
        if page_count<total_pages-1:
            page_count+=1 
        else:
            print("\nAlready at the last page")
            choice, page_count = take_input(page_count, total_pages)
            
    elif choice=='l':
        if page_count>0:
            page_count-=1 
        else:
            print("\nAlready at the first page")
            choice, page_count = take_input(page_count, total_pages)
            
    elif choice=='e':
        pass
    
    else:
        print("\nPlease enter a valid input")
        choice, page_count = take_input(page_count, total_pages)
        
    return choice, page_count

def connect_api():
    try:
        json_obj = ""
        if os.path.exists("params.json"):
            f = open('params.json')
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
        response = requests.get(f'https://{subdomain}.zendesk.com/api/v2/tickets.json', auth=(f'{username}', f'{password}'))
        
        if response.status_code==200:
            json_obj = response.json()
            return 1, json_obj
        else:
            return 0, json_obj
        
    except:
        print("Authentication failed. Please make sure parameters are correctly set in params.json")
        return 0, json_obj
    
def run():

    status, json_obj = connect_api()
    
    if status==0:
        return 0
    
    if len(json_obj["tickets"])==0:
        print("\nYou have no tickets left to resolve. Yayy!")
        return 1
    
    page_count = 0
    total_pages = math.ceil(len(json_obj["tickets"])/25)
    
    while(True):
        main_choice = input("\nMain Menu: Select your viewing choice - \n| 1:View All Tickets |\n| 2:View latest ticket |\n| 3:Select ticket by ID |\n| e:Exit |\n")
        if main_choice=='1':
            print("\nViewing all Tickets:")
            while(True):
                
                display_page(page_count, total_pages, json_obj)
                choice, page_count = take_input(page_count, total_pages)
                
                if choice=='e':
                    print("\nExit to Main Menu Successful")
                    break
                
        elif main_choice=='2':
            print ("\n{:<12} {:<12} {:<30}".format('Ticket ID','Status','Subject'))
            display_ticket(len(json_obj["tickets"])-1, json_obj)
            
        elif main_choice=='3':
            flag = 0
            select_id = int(input("\nEnter required ticket ID:\t"))
            for index in range(len(json_obj["tickets"])):
                if(json_obj["tickets"][index]["id"]==select_id):
                    print ("\n{:<12} {:<12} {:<30}".format('Ticket ID','Status','Subject'))
                    display_ticket(index, json_obj)
                    flag = 1
            if flag==0:
                print(f'\nTicket with ID = {select_id} not found')
                
        elif main_choice=='e':
            print("\nExit Successful\nThank you for using my Ticket Viewer and have an awesome day!")
            break
        
        else:
            print("\nPlease enter a valid input choice")
    
    return 1

if __name__ == '__main__':
    run()