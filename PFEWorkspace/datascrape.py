
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
# This was really the hard part for me
# I made a loop that was designed to scan for the contents of span, converting it to an integer and storing it
#   within a list I had made prior
# Next I had to loop through that list, summing up the integers along the way and storing it into sum
numlist = []
sum = 0
tags = soup('span')
for tag in tags:
    snum = str(tag.contents[0])
    num = int(tag.contents[0])
    numlist.append(num)
for i in numlist:
    sum = sum + i
print(sum)

