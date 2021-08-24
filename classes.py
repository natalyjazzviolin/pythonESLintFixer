import time

class File(object):

    def __init__(self, error_dictionary):
        for key in error_dictionary:
            key = self.clean(key)
            print(key)
            time.sleep(5)

    def clean(self, path: str) -> str:
        clean_path = path.split(':', 1)
        print(clean_path)
        print(type(clean_path))
        return clean_path
