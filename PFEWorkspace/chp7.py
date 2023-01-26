# Used to prompt user for file name, then strips the whitespace from the file and prints it in uppercase.
#

'''
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    print(line.upper())


'''
# prompt for file name, open that file, read through file looking for data, avg that data and print out statement

fname = input("Enter file name: ")
fh = open(fname)
count = 0
rtotal = 0
msg = "Average spam confidence:"

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    data = float(line[20:26])
    rtotal = rtotal + data
    avg = rtotal / count
    goose = float(avg)
    print(msg, goose)
