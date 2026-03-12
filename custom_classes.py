class Calculator:
    def __init__(self):
        self.__current_val = 0

    def get_current_val(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        return self.__current_val
    
    def add(self, x, y):
        self.__current_val = x + y
>>>>>>> feat/add
=======
        return self.__current_val

    def subtract(self, x, y):
        self.__current_val = x - y
>>>>>>> feat/sub
        return self.__current_val
=======
        return self.__current_val
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")

        self.__current_val = x / y
        return self.__current_val 
>>>>>>> feat/div
=======
        return self.__current_val
    def multiply(self, x, y):
        self.__current_val = x * y
        return self.__current_val
>>>>>>> feat/mul
