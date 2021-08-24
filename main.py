import subprocess
import pandas as pd
import time

from setup import format_errors, get_error_list
from classes import File

# Get error list from the terminal.
# This returns a list (setup[0]) and the filepath (setup[1])
setup = get_error_list()
error_list = setup[0]

# Make list into dataframe. Iterate over it to make a dictionary
dictionary = format_errors(error_list, setup[1])

test = File(dictionary)
