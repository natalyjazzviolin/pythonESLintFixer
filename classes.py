import time

class File(object):

    def __init__(self, error_dictionary):
        for key in error_dictionary:
            print(f'From File class: {error_dictionary[key]}')
            for value in error_dictionary[key]:
                print(error_dictionary[key][value])
            # key = self.clean(key)
            # print(key)
            time.sleep(5)

    def clean(self, path: str) -> str:
        clean_path = path.split(':', 1)
        clean_path = clean_path[0]
        return clean_path
