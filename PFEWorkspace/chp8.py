fname = input("Enter file name: ")
fh = open(fname)
lst = list()                        # list for the desired output
for line in fh:                     # to read every line of file romeo.txt
    word = line.rstrip().split()    # to eliminate the unwanted blanks and turn the line into a list of words
    for element in word:            # Held me up for AWHILE, did not know you can nest for loops within for loops
        if element in lst:          # if element is repeated
            continue                # do nothing
        else:                       # else if element is not in the list
            lst.append(element)     # append
lst.sort()              # sort the list (de-indent indicates that you sort when the loop ends)
print(lst)
