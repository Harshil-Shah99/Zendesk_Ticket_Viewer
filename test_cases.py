# -*- coding: utf-8 -*-
"""
@author: hshah6
"""
# I use the unittest framework to test all of the components of the code
import unittest
from zendesk import *
import json

class TestCases(unittest.TestCase):

    # Tests for the display_ticket() function
    # Checks if each individual ticket is displayed properly by using sample json data from the file test_data.json
    def test_display_ticket_case_1(self):
        with open('test_data.json') as f:
             json_obj = json.load(f)
        ticket_id, status, subject = display_ticket(index=0, json_obj=json_obj, testing=True)
        self.assertEqual(ticket_id, 1)
        self.assertEqual(status, "open")
        self.assertEqual(subject, "test subject 1")

    def test_display_ticket_case_2(self):
        with open('test_data.json') as f:
             json_obj = json.load(f)
        ticket_id, status, subject = display_ticket(index=1, json_obj=json_obj, testing=True)
        self.assertEqual(ticket_id, 2)
        self.assertEqual(status, "pending")
        self.assertEqual(subject, "test subject 2")
        
    def test_display_ticket_case_3(self):
        with open('test_data.json') as f:
             json_obj = json.load(f)
        ticket_id, status, subject = display_ticket(index=2, json_obj=json_obj, testing=True)
        self.assertEqual(ticket_id, 3)
        self.assertEqual(status, "closed")
        self.assertEqual(subject, "test subject 3")
        
    def test_display_ticket_case_4(self):
        with open('test_data.json') as f:
             json_obj = json.load(f)
        ticket_id, status, subject = display_ticket(index=3, json_obj=json_obj, testing=True)
        self.assertEqual(ticket_id, 4)
        self.assertEqual(status, "open")
        self.assertEqual(subject, "test subject 4")
        
    def test_display_ticket_case_5(self):
        with open('test_data.json') as f:
             json_obj = json.load(f)
        ticket_id, status, subject = display_ticket(index=4, json_obj=json_obj, testing=True)
        self.assertEqual(ticket_id, 5)
        self.assertEqual(status, "pending")
        self.assertEqual(subject, "test subject 5")
        
    # Tests for the display_page() function
    # Checks if pages display the appropriate number of tickets, with the correct beginning and end of ticket indices
    def test_display_page_case_1(self):
        with open('test_data.json') as f:
             json_obj = json.load(f)
        end_of_range, entry_count = display_page(page_count=0, total_pages=1, json_obj=json_obj, testing=True)
        self.assertEqual(end_of_range, 5)
        self.assertEqual(entry_count, 5)
        
    def test_display_page_case_2(self):
        with open('test_data.json') as f:
             json_obj = json.load(f)
        end_of_range, entry_count = display_page(page_count=1, total_pages=5, json_obj=json_obj, testing=True)
        self.assertEqual(end_of_range, 50)
        self.assertEqual(entry_count, 25)
        
    def test_display_page_case_3(self):
        with open('test_data.json') as f:
             json_obj = json.load(f)
        end_of_range, entry_count = display_page(page_count=1, total_pages=2, json_obj=json_obj, testing=True)
        self.assertEqual(end_of_range, 5)
        self.assertEqual(entry_count, -20)
        
    def test_display_page_case_4(self):
        with open('test_data.json') as f:
             json_obj = json.load(f)
        end_of_range, entry_count = display_page(page_count=3, total_pages=3, json_obj=json_obj, testing=True)
        self.assertEqual(end_of_range, "error")
        self.assertEqual(entry_count, "error")
        
    def test_display_page_case_5(self):
        with open('test_data.json') as f:
             json_obj = json.load(f)
        end_of_range, entry_count = display_page(page_count=7, total_pages=5, json_obj=json_obj, testing=True)
        self.assertEqual(end_of_range, "error")
        self.assertEqual(entry_count, "error")
        
    # Test for the take_input() function
    # Checks if given the choice and current page number, the take_input function returns the correct page
    def test_take_input(self):
        choice, page_count = take_input(page_count=1, total_pages=3, testing=True, testing_choice='r')
        self.assertEqual(choice, 'r')
        self.assertEqual(page_count, 2)
        
    # Test for the connect_api() function
    # Checks if the connect api function is 
    def test_connect_api(self):
        passed, json_obj = connect_api()
        self.assertEqual(passed, 1)

    # Tests for the run() function
    # Checks if all of the tickets are correctly fetched from the ticketing system by checking the length of the list
    def test_run_case_1(self):
        with open('test_data.json') as f:
             json_obj = json.load(f)
        length = run(testing=True, testing_json=json_obj)
        self.assertEqual(length, 5)
        
    def test_run_case_2(self):
        length = run(testing=True, testing_json={"tickets":[]})
        self.assertEqual(length, "pass")
        
if __name__ == '__main__':
    unittest.main()
