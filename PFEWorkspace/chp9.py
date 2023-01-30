"""
counts = dict()
print('Enter a line of text!')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('counts', counts)
"""

counts = dict()
# count = 0
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Histogram

for line in handle:
    if line.startswith('From:'):
        line = line.split()
        sender = line[1]
        # print(sender)
        for sender in line:
            if sender not in counts or sender.startswith('From:'):
                counts[sender] = 1
            else:
                counts[sender] = counts[sender] + 1
                # print(counts)

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)
