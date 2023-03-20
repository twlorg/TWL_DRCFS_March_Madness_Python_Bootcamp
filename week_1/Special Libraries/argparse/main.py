import argparse

# Creating an ArgumentParser object
parser = argparse.ArgumentParser(description="Example script for argparse")

# Adding arguments to the parser
parser.add_argument("-n", "--name", type=str, help="Your name")
parser.add_argument("-a", "--age", type=int, help="Your age")

# Parsing the arguments
args = parser.parse_args()

# Accessing the parsed arguments
if args.name and args.age:
    print("Your name is", args.name, "and your age is", args.age)
else:
    print("Please provide both name and age using command-line options.")



# What's the difference?
    """
    In this example, the program uses argparse to parse command-line arguments. 
    The program takes two optional arguments, --name and --age, using the a
    dd_argument() method. The type argument is used to specify the type of 
    the argument, and the help argument provides a description of the argument.

    When the program is run, the user can provide the arguments via the command line, like this:
    python example.py --name John --age 25

    The argparse module automatically parses the command-line arguments,
    validates them, and stores them in the args object. The program then
    prints the values entered by the user if both the arguments are
    provided, otherwise, it prompts the user to provide both the arguments.
    """