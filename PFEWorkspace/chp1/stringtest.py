#create a program to use find() and string slicin, then convert it to float and print it out
#6.2 python for everybody assignment

text = "X-DSPAM-Confidence:    0.8475"
spos = text.find('0')
epos = text.find('5', spos)
slice = float(text[23:29])
print(slice)
