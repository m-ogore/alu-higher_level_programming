#!/usr/bin/python3

#A program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)
#loop through numbers 0-98 and print
for i in range(0,99):
    print("{} = {}".format(i,hex(i)))