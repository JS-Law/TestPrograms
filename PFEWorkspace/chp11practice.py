# 11.2 Practice Problem using RegEx
# Objectives:
# Read through file, look for all integers using re.findall(), then converting the extracted strings
# to integers


# Import Regular Expression Module
import re

sum = 0
#numlist = []
# Open File for Read, testing for incorrect file name.
fname = input('Enter file: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    exit()

# Read Through File Looking for Integers
for line in fhand:
    line = line.rstrip()
    numlist = re.findall('[0-9]+', line)
    for numbers in numlist:
        sum = sum + int(numbers)

print(sum)


