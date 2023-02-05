# 11.2 Practice Problem using RegEx
# Objectives:
# Read through file, look for all integers using re.findall(), then converting the extracted strings
# to integers

# Open File for Read

name = input("Enter file:")
if len(name) < 1:
    name = "regexsum.txt"
handle = open(name)

# Read Through File Looking for Integers
for line in handle:
    line = line.rstrip()
