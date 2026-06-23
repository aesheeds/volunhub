import argparse
from enum import Enum, auto

programname = 'Volunhub'

class CLIstate(Enum):
    INTRO = auto()
    CREDENTIALS = auto()
    SEARCH = auto()
    SAVED = auto()
    PROFILE = auto()

#todo make a better help_message
help_message = 'This is a temporary help message to be redone later'


parser = argparse.ArgumentParser(description=programname)

group = parser.add_mutually_exclusive_group()
group.add_argument('-b', '--back', action='store_true', help='')
group.add_argument('-e', '--exit', action='store_true', help='')
group.add_argument('-s', '--saved', action='store_true', help='')
group.add_argument('-p', '--profile', action='store_true', help='')
group.add_argument('-c', '--confirm', action='extend', nargs='+',   help='')
group.add_argument('-u', '--unconfirm', action='extend', nargs='+',  help='')

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    while not args.exit :
        s = input("Volunhub: ")
        args = parser.parse_args(s.split())
        