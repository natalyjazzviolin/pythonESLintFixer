import time
import re

class Dictionary_Processor(object):


    def __init__(self, error_dictionary):
        items = []
        files = []

        for key in error_dictionary:
            clean_key = self.clean(key)
            f = File(clean_key)
            for value in error_dictionary[key]:
                value_list = value.split(' ')
                value_list = list(filter(None, value_list))
                f.add(value_list[1], value_list[2])
            f.announce()
                # for item in value_list:
                #     print(item)
                #     breakpoint()
                #     items.append(item)

            # print(f'This is the item list { items }')
            # f.announce()
            files.append(f)
            # File(key)
            # File.add(File, items[1], items[2])
            # files.append(File)
            # print(File().errors)
            time.sleep(5)
            f.reset()
            del f
            items = []

    def clean(self, path: str) -> str:
        clean_path = path.split(':', 1)
        clean_path = clean_path[0]
        return clean_path

class File:
    errors = dict()

    def __init__(self, filepath):
        self.filepath = filepath

    def announce(self):
        print(f'The filepath is { self.filepath }')
        print(f'The errors are { self.errors}')

    def add(self, x, y):
        self.errors[x] = y

    def reset(self):
        self.errors.clear()
