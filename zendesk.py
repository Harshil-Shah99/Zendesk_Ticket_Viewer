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
import pprint

# Function to display a particular ticket using its index value at the list of all tickets
def display_ticket(index, json_obj, testing = False):
    if testing:
        return json_obj["tickets"][index]["id"], json_obj["tickets"][index]["status"], json_obj["tickets"][index]["subject"]
    
    print ("{:<12} {:<12} {:<30}".format(json_obj["tickets"][index]["id"], json_obj["tickets"][index]["status"], json_obj["tickets"][index]["subject"]))
    
    
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

# Function to page through the tickets by taking in input choices to move to
# either to the previous or the next page
def take_input(page_count, total_pages, testing = False, testing_choice = ''):
    if not testing:
        choice = input("\nPress - | r:Next Page | l:Previous Page | e:Exit to Main Menu | -\t")
    else:
        choice = testing_choice
        
    if choice=='r' or choice=='R':
        if page_count<total_pages-1:
            page_count+=1 
        else:
            print("\nAlready at the last page")
            choice, page_count = take_input(page_count, total_pages)
            
    elif choice=='l' or choice=='L':
        if page_count>0:
            page_count-=1 
        else:
            print("\nAlready at the first page")
            choice, page_count = take_input(page_count, total_pages)
            
    elif choice=='e' or choice=='E':
        pass
    
    else:
        print("\nPlease enter a valid input")
        choice, page_count = take_input(page_count, total_pages)
        
    return choice, page_count

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

if __name__ == '__main__':
    run()