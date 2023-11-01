#!/usr/bin/python3

#A program that imports the function add(a, b): 
#from the file add_0.py 
#and prints the result of the addition 1 + 2 = 3

s = __import__('add_0')


def main():
    a = 1
    b = 2
    print("{} + {} = {}\n".format(a, b, s.add(a, b)))

if __name__ == "__main__":
    main()