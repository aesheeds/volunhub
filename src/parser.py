import argparse
from enum import Enum, auto

programname = 'Volunhub'

class CLIstate(Enum):
    INTRO = auto()
    CREDENTIALS = auto()
    SEARCH = auto()
    SAVED = auto()
    PROFILE = auto()

class State():
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

    def parse(self, string):
        self.args = self.parser.parse_known_args(string.split())
        if self.args.help:
            print(help_message)
        if self.args.profile:
            self.state = CLIstate.PROFILE


    def exit(self):
        if self.args:
            self.args.exit

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
                        print("sending information to database")

                    elif I == "create":
                        while  not FL_name:
                            print("Creating new account")
                            FL_name = input("Enter your First and Last name: ")
                            pswd = input("Enter your password: ")
                            if len(name.split()) > 2:
                                print("invalid name")
                            else:
                                FL_name = name
                        print("sending information to database")

                    else: 
                        print("invalid option")

            case CLIstate.SEARCH :
                print("Currently in Search State")
            case CLIstate.SAVED :
                print("Currently in SAVED State")
            case CLIstate.PROFILE :
                print("Currently in Profile State")
            case _ :
                print("Unknown State Reached")

if __name__ == "__main__":
    state = State()
    state.display_state()
    state.display_state()