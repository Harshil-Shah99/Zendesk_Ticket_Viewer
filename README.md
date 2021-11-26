![Github](https://img.shields.io/badge/Language-Python-red.svg)
![Github](https://img.shields.io/badge/Method-Command--Line%20Interface-blue)
# Zendesk_Ticket_Viewer - Harshil Shah
This is my submission for the Zendesk intern coding challenge.

I've completed all of the requirements using Python, and the code can be executed on the Command Line. I've done so for the following reasons:
* Python is a programming language that I am quite comfortable with and proficient at, so it made sense to use it for an important assignment
* It is simple and easy to set up/install and understand, which makes it easy to evaluate
* I wanted to implement the project in the command line interface, and Python makes this easy to do
* It is the first time that I've used Python for interfacing with a well-documented API, so I got to learn a lot!

Python version used: `Python 3.10.0`

## Steps to set up:
1. Download Python from [this link](https://www.python.org/downloads/release/python-3100/) and install normally by following the instructions on screen.
- Note: You may choose to either add Python to your Path or not. In case you do not, please clone the repository to within the C drive, so you can still use the `py` command in the
Command-Line Interface (CLI) to run the code.
2. Open a command prompt window and navigate to the root of the cloned repository. You can use the cd command to do so. For example: `cd C:\Fall 2021\Zendesk_assignment`
3. Replace the sample authentication variables provided in the file "params.json" with your actual authentication variables. Specifically, replace
- `sample_username` with the email ID related to your account
- `sample_password` with your account password
- `sample_subdomain` with your current subdomain starting with zcc
4. Make sure that your zendesk account supports Password Access for the API. You can do this by going to </br>Admin settings->Apps & Integrations->Zendesk API->Enable Password Access
5. Ensure that you have a working internet connection

## Steps to run
1. After navigating to the root directory as outlined earlier, run the command `py zendesk.py` to execute the code
2. Run the command `py test_cases.py` to execute the test cases
- Note: In steps 1 and 2, if there are any issues, you can try replacing `py` with `py -3` or `python` or `python3`. Sometimes there may be multiple versions of python installed 
from before, so using one of these commands instead may help you execute the code using the correct one.
3. If you are having any issues with the requests library, please run the command `pip install requests` and then restart the command prompt.

## Sample Outputs
- Main Menu and selecting option 1:</br>
![image](https://github.com/Harshil-Shah99/Zendesk_Ticket_Viewer/blob/master/Images/main_menu.JPG)
</br>

- First page of 25 entries:</br>
![image](https://github.com/Harshil-Shah99/Zendesk_Ticket_Viewer/blob/master/Images/page1.JPG)
</br>

- Attempt to move further than the last page - Shows appropriate message:</br>
![image](https://github.com/Harshil-Shah99/Zendesk_Ticket_Viewer/blob/master/Images/last_page.JPG)
</br>

- Selecting option 2 - Show newest ticket:</br>
![image](https://github.com/Harshil-Shah99/Zendesk_Ticket_Viewer/blob/master/Images/last_ticket.JPG)
</br>

- Selecting option 3 - Show ticket by inputting ticket ID:</br>
![image](https://github.com/Harshil-Shah99/Zendesk_Ticket_Viewer/blob/master/Images/ticket_id.JPG)
</br>

- Selecting option e - Exiting the code:</br>
![image](https://github.com/Harshil-Shah99/Zendesk_Ticket_Viewer/blob/master/Images/exit.JPG)
</br>

- Running the test_cases.py file - all tests cases pass:</br>
![image](https://github.com/Harshil-Shah99/Zendesk_Ticket_Viewer/blob/master/Images/test.JPG)
</br>
