class Calculator:
    def __init__(self):
        self.__current_val = 0

    def get_current_val(self):
        return self.__current_val

    def subtract(self, x, y):
        self.__current_val = x - y
        return self.__current_val