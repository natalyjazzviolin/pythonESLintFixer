import subprocess
import pandas as pd
import time

from setup import format_errors, get_error_list

# Variables
# error_list = []
# d_values = []
# directory = ''


setup = get_error_list()
error_list = setup[0]
dictionary = format_errors(error_list, setup[1])

print(dictionary)
breakpoint()

# Convert list to a dataframe
# df = pd.DataFrame(error_list, columns=['Console Output'])

# for index, row in df.iterrows():
#     # If no filepath has been found yet
#     if key != '':
#         if directory in row.values[0]:
#             key = row.values[0]
#         if 'ERROR' in row.values[0]:
#             d_values.append(row.values[0])
#             print('Value appended!')
#         if str(row.values[0]).isspace():
#             print('This is an empty string.')
#             dictionary[key] = d_values
#             key = ''
#             d_values = []
#             time.sleep(1)
#     # If filepath is defined
#     else:
#         if directory in row.values[0]:
#             print('KEY FOUND!')
#             key = row.values[0]
#             print(key)


