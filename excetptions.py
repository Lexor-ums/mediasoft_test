class ParseException(Exception):
    def __init__(self, what):
        self.__what = what

    def what(self):
        return self.__what
