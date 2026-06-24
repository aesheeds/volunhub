import argparse
from enum import Enum, auto

programname = 'Volunhub'

class CLIstate(Enum):
    INTRO = auto()
    CREDENTIALS = auto()
    QUERY = auto()
    PROFILE = auto()

""" Class State
stores the current state of the program and parses the CLI
"""
class State():
    #initialize the parser and the argumetns we are looking for
    def __init__(self, msg=None):
        if not msg:
            #todo make a better help_message
            help_message = 'This is a temporary help message to be redone later'
        else:
            help_message = msg

        self.parser = argparse.ArgumentParser(exit_on_error=False, description=programname, add_help=False)
        
        #arguments to be parsed
        self.group = self.parser.add_mutually_exclusive_group()
        self.group.add_argument('-h', '--help', action='store_true', help='')
        self.group.add_argument('-b', '--back', action='store_true', help='')
        self.group.add_argument('-e', '--exit', action='store_true', help='')
        self.group.add_argument('-s', '--saved', action='store_true', help='')
        self.group.add_argument('-p', '--profile', action='store_true', help='')
        self.group.add_argument('-c', '--confirm', action='extend', nargs='+',   help='')
        self.group.add_argument('-u', '--unconfirm', action='extend', nargs='+',  help='')
        
        self.args = None
        self.state = CLIstate.INTRO
        self.data = {
            "first_name": None,
            "last_name": None,
            "degree": None,
            "major": None,
            "skills": None,
            "experience": None,
            "location": None
            }

    def print_data(self):
        print(self.data)

    def parse(self, string):
        self.args = self.parser.parse_known_args(string.split())
        if self.args.help:
            print(help_message)
        if self.args.back and self.state == CLIstate.PROFILE:
            self.state = CLIstate.QUERY
        if self.args.profile:
            self.state = CLIstate.PROFILE


    def exit(self):
        if self.args:
            self.args.exit

    def create_account(self):
        for key in self.data:
            self.data[key] = input(f"{key}: ")

    def display_state(self):
        match self.state:
            case CLIstate.INTRO :
                print("Welcome to JobHub!\nPlease enter your credentials or create a new account")
                self.state = CLIstate.CREDENTIALS

            case CLIstate.CREDENTIALS :
                FL_name = None
                pswd = None
                I = None
                while I != "login" or I != "create":
                    I = input("Login or Create an account (login/create)? ")
                    if I == "login":
                        while not FL_name:
                            print("Login to your account")
                            name = input("Enter your First and Last name: ")
                            pswd = input("Enter your password: ")
                            if len(name.split()) > 2:
                                print("invalid name")
                            else:
                                FL_name = name
                                self.data["first_name"] = name[0]
                                self.data["last_name"] = name[1]
                        print("retrieving information to database")

                    elif I == "create":
                        while  not FL_name:
                            print("Creating new account")
                            FL_name = input("Enter your First and Last name: ")
                            pswd = input("Enter your password: ")
                            if len(name.split()) > 2:
                                print("invalid name")
                            else:
                                FL_name = name
                                self.data["first_name"] = name[0]
                                self.data["last_name"] = name[1]

                        print("Please enter the following information:")
                        create_account()
                        print("sending information to database")

                    else: 
                        print("invalid option")

            case CLIstate.QUERY :
                print("Currently in Query State")
            
            case CLIstate.PROFILE :
                print("Currently in Profile State")
            
            case _ :
                print("Unknown State Reached")

if __name__ == "__main__":
    state = State()
    state.display_state()
    state.display_state()