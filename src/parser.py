import argparse
from database import get_user, save_user
from enum import Enum, auto

programname = 'Jobhub'

class CLIstate(Enum):
    INTRO = auto()
    CREDENTIALS = auto()
    QUERY = auto()
    PROFILE = auto()

class JobType(Enum):
    INTERNSHIP = auto() 
    ENTRY = auto()
    EITHER = auto()

""" Class State
stores the current state of the program and parses the CLI
"""
class State():
    #initialize the parser and the argumetns we are looking for
    def __init__(self, msg=None):
        if not msg:
            help_message = '-h --help           display this help message\n-q --query           query to get a list of potential jobs\n-e --exit           exit this program\n'
        else:
            help_message = msg

        self.parser = argparse.ArgumentParser(exit_on_error=False, description=programname, add_help=False)
        
        #arguments to be parsed
        self.group = self.parser.add_mutually_exclusive_group()
        self.group.add_argument('-h', '--help', action='store_true', help='')
        self.group.add_argument('-e', '--exit', action='store_true', help='')
        
        self.args = None
        self.state = CLIstate.INTRO
        self.data = {
            "first_name": None,
            "last_name": None,
            "degree": None,
            "major": None,
            "skills": None,
            "experience": None,
            "location": None,
            "job_type": 0
            }

    def print_data(self):
        print(self.data)

    def parse(self, string):
        self.args = self.parser.parse_known_args(string.split())
        if self.args.help:
            print(help_message)

    def exit(self):
        if self.args:
            self.args.exit

    def create_account(self):
        for key in self.data:
            if key != "first_name" and key != "last_name":
                if key == "job_type":
                    while self.data[key] < 1 or self.data[key] > 3:
                        self.data[key] = int(input(f"{key}\n1. Internship\n2. Entry-level job\n3. Either\nChoose 1, 2, or 3: "))
                        if self.data[key] < 1 or self.data[key] > 3:
                            print("invalid option")
                else:
                    self.data[key] = input(f"{key}: ")

    def display_state(self):
        match self.state:
            case CLIstate.INTRO :
                print("Welcome to JobHub!\nPlease enter your credentials or create a new account")
                self.state = CLIstate.CREDENTIALS

            case CLIstate.CREDENTIALS :
                I = None
                while I != "l" and I != "c":
                    I = input("Login or Create an account (l/c)? ").lower()
                    
                    if I == "l":
                        FL_name = None
                        while not FL_name:
                            print("Login to your account")
                            name = input("Enter your First and Last name: ")
                            if len(name.split()) > 2 or len(name.split()) < 2:
                                print("invalid name")
                            else:
                                FL_name = name
                                print(FL_name)
                                self.data["first_name"] = name.split()[0]
                                self.data["last_name"] = name.split()[1]
                        print("Retrieving information from the database")
                        response = get_user(self.data["first_name"], self.data["last_name"])
                        if not response:
                            print("Error: Unable to find user. Please Retry.")
                            I = None
                        else:
                            self.data = response
                            print(f"Successfully found user: {self.data}")

                    elif I == "c":
                        FL_name = None
                        while  not FL_name:
                            print("Creating new account")
                            name = input("Enter your First and Last name: ")
                            if len(name.split()) > 2 or len(name.split()) < 2:
                                print("invalid name")
                            else:
                                FL_name = name
                                self.data["first_name"] = name.split()[0]
                                self.data["last_name"] = name.split()[1]

                        print("Please enter the following information:")
                        self.create_account()
                        print("Saving information to database")
                        response = save_user(
                            self.data["first_name"],
                            self.data["last_name"],
                            self.data["degree"],
                            self.data["major"],
                            self.data["skills"],
                            self.data["experience"],
                            self.data["location"],
                            str(self.data["job_type"])
                        )
                        if not response :
                            print(f"Error: Unable to add user. Please Retry.")
                            I = None
                        else:
                            print(f"Successfully added user: {self.data}")

                    else: 
                        print("invalid option")
                self.state = CLIstate.QUERY
            
            case _ :
                print("Unknown State Reached")

if __name__ == "__main__":
    state = State()
    state.display_state()
    state.display_state()
    state.print_data()