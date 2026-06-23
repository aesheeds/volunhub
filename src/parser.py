import argparse

parser = argparse.ArgumetnParser(description='process some files')
parser.add_argument('filename', help='File to process')
parser.add_argument('-o', '--output', help='Output file')
parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

if __name__ == "__main__":
    print("this is the main file")