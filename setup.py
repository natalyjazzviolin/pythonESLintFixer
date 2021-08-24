from os import error
import subprocess
import pandas as pd
import time

def get_error_list() -> list:
    error_list = []

    # Get path path
    path = input('Please enter path. Press Enter for default. ')
    while len(path) == 0:
        path = '../../bearcat-gui'
    print('Path accepted, processing errors...')

    # Run terminal command to print ESLint errors
    terminal = subprocess.Popen(
        'tslint --config ./tslint.json --project .',
        shell=True,
        cwd= path,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    # Reads/decodes/appends each terminal line to a list
    for line in terminal.stdout.readlines():
        line = line.decode('UTF-8')
        error_list.append(line)
    retval = terminal.wait()

    path = path.split('/', 2)
    directory = str(path[2])
    print(type(directory))

    return error_list, directory

def format_errors(error_list: list, directory: str) -> dict:
    dictionary = dict()
    key = ''
    d_values = []


    print(f'In formater. Directory: { directory }')
    time.sleep(5)
    df = pd.DataFrame(error_list, columns=['Console Output'])
    print('Data frame created')
    # print(df)
    time.sleep(5)

    for index, row in df.iterrows():
        # If no filepath has been found yet
        if key != '':
            if directory in row.values[0]:
                key = row.values[0]
            if 'ERROR' in row.values[0]:
                d_values.append(row.values[0])
                print('Value appended!')
            if str(row.values[0]).isspace():
                print('This is an empty string.')
                dictionary[key] = d_values
                key = ''
                d_values = []
                time.sleep(1)
        # If filepath is defined
        else:
            if directory in row.values[0]:
                print('KEY FOUND!')
                key = row.values[0]
                print(key)
    return dictionary
