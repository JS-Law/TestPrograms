# Regular expressions
"""


for loop to find and slice
hand = open()
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)
import re
hand = open()
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

"""

# Matching and Extracting Data
"""
Matching and Extracting Data
    -the re.search() returns a True/False depending on whether the string matches the regular expression
    -if we actually want the matching strings to be extracted, we use re.findall()
    -[0-9]+ -- one or more digits
    -kindof like a split() and for: loop all in one!!!!
    -returns a LIST
ex. 
import re
x = 'My 2 favorite numbers are 19 and 42
y = re.findall('[0-9]+',x)   #one or more digits -- [0-9]+ is looking through the string 'x'
print(y)
OP: ['2', '19', '42'] #conveniently extracts out the "one or more digits it found" 

When we use re.findall(), it returns a list of zero or more strings that match the regex
ex.
import re
x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
OP: ['2', '19', '42']
y = re.findall('[AEIOU]+',x) #"Are there any upper case vowels in x" '+' means one or more
print(y)
OP: []  #returns nothing because there are no uppcase vowels
"""

# Warning: Greedy Matching
"""
The repeat characters (* and +) push outward in both directions(greedy) to match the largest possible string.
    - ^F.+:  -- first character in the match is F, '+' one or more characters ':' last character
    - see cheat sheet
ex.
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
OP: ['From: Using the :']

    -why not 'From:'??
    -wants to be as big as possible, while still matching the expression
    -pushy, push outwards as wide as they can
    
"""
# Non-Greedy Matching
"""
Not all regular expression repeat codes are greedy! If you add a ? character, the + and * chill out a bit...
    -^F.+?: One or more characters Non-greedy, starting with 'F', ending in ':'
ex.
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x) # Non-Greedy matching returns the smalls possible string matching the regex
print(y)
OP: ['From:']

"""
# Fine-Tuning String Extraction
"""
You can refine the match for the re.findall() and seperately determine which portion of the match is to be extracted
by using parentheses!
    -\S+@\S+ -  '\S' at least one non-whitespace character
ex.
From stepehn.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
y = re.findall('\S+@\S+', x) 
print(y)
OP: ['stepehn.marquard@uct.ac.za'] 
    -basically looking for s;lkjdsfg;lkj>>>>>@<<<<jhsdf 
    -an @ flanked by nonblank characters!
    -GREEDY, because if it was nongreedy wed get 'd@u'
    
Parantheses are not part of the match, but they tell where to start and stop, and what string to extract!
ex.
From stepehn.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
y = re.findall('^From (\S+@\S+)', x) #from is PART of the match, but START extraction within the parentheses
print(y)
OP: ['stepehn.marquard@uct.ac.za'] 
"""
# The Double Split Pattern (Non Regex)
"""
Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again!
ex.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

words = line.split   #
email = words[1]            #stephen.marquard@uct.ac.za
pieces = email.split('@')   #['stephen.marquard', 'uct.ac.za']
print(pieces[1])            #'uct.ac.za'

THE REGEX VERSION!!
    -'@([^ ]*)'  Look through the string until i find an @ sign
ex.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', lin'
print(y)
OP: ['uce.ac.za']

"""
# Spam Confidence
"""
-Heres alittle bit of code that uses regex to pick lines and extract data
ex.
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
OP: Maximum: 0.9907

"""
# Escape Character
"""
If you want a special regular expression character top just behave normally(most of the time) you prefix it with a '\'
    - \$[0-9.]+  we actually NEED to look for the dollar sign so we prefix it with a backslack '\'
ex.
import re
x = 'We just receieve $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)
OP: ['$10.00']

"""
