import subprocess
import pandas as pd
import time

# Variables
error_list = []
dictionary = dict()
key = ''
key_is_set = bool(key)
d_values = []

# Runs terminal command to print ESLint errors
a = subprocess.Popen(
    'tslint --config ./tslint.json --project .',
    shell=True,
    cwd='../../bearcat-gui',
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT
)

# Reads/decodes/appends each terminal line to a list
for line in a.stdout.readlines():
    line = line.decode('UTF-8')
    error_list.append(line)
retval = a.wait()

# Convert list to a dataframe
df = pd.DataFrame(error_list, columns=['Console Output'])

# Assign tags to rows depending on content
df['Tag'] = ['Filename' if 'home' in ele else 'Error'for ele in df['Console Output']]

for index, row in df.iterrows():
    if key != '':
        if 'bearcat-gui' in row.values[0]:
            key = row.values[0]
        if 'ERROR' in row.values[0]:
            d_values.append(row.values[0])
            print('Value appended!')
        if str(row.values[0]).isspace():
            print('This is an empty string.')
            dictionary[key] = d_values
            key = ''
            d_values = []
            time.sleep(5)
    else:
        if 'bearcat-gui' in row.values[0]:
            print('KEY FOUND!')
            key = row.values[0]
            print(key)
    time.sleep(2)


# dict_pairs = dictionary.items()

# print(next(iter(dict_pairs)))
