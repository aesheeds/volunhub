import argparse
from enum import Enum, auto

class CLIstate(Enum):
    INTRO = auto()
    CREDENTIALS = auto()
    SEARCH = auto()
    SAVED = auto()
    PROFILE = auto()

#todo make a better help_message
help_message = 'This is a temporary help message to be redone later'

# parser = argparse.ArgumentParser(description='process some files')
# parser.add_argument('-h', '--help', )
# parser.add_argument('-b', '--back', action=argparse.BooleanOptionalAction)
# parser.add_argument('-e', '--exit', action=argparse.BooleanOptionalAction)
# parser.add_argument('-s', '--saved', action=argparse.BooleanOptionalAction)
# parser.add_argument('-p', '--profile', action=argparse.BooleanOptionalAction)
# parser.add_argument('-c', '--confirm', )
# parser.add_argument('-u', '--unconfirm', )

if __name__ == "__main__":
    for state in CLIstate:
        print(f"{state.name}: {state.value}")
        