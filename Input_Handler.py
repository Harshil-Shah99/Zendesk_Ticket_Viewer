# -*- coding: utf-8 -*-
"""
@author: hshar
"""

import requests
import math
import json
import os


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