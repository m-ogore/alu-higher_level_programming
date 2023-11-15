#!/usr/bin/python3
'''
Write a class Square that defines a square by: (based on 4-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
You are not allowed to import any module
'''

class Square:
            
    #Initializes a new instance of the class.

    #Parameters: size (int, optional): The size of the object. Defaults to 0.

    #Raises:TypeError: If size is not an integer.
    #and ValueError: If size is less than 0.
    
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
            
        #Get the value of the `size` property.

        #:return: The value of the `size` property.

    @property
    def size(self):
        return self.__size
            
        #Set the size of the object.

        #Parameters:
        #    value (int): The new size of the object.

        #Raises:
        #    TypeError: If the value is not an integer.
        #    ValueError: If the value is less than 0.
        
        #Calculates the area of a square.
        
        """

        Returns:
            int: The area of the square.
        """
                
            #Calculates the area of an object.


        """
        
        Returns:
            int: The area of the object.
        """

        #Calculate and return the area of a square.

        """
        Returns:
            int: The area of the square.
        """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        return self.__size * self.__size
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()




my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")