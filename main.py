# This is a sample Python script.
import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def how2(x):
    return x*x

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("and " + str(how2(100))+" "+sys.argv[1])

