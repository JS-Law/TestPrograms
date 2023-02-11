import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')  # prompting user to enter URL, while assigning it to our variable
repeat = int(input('Enter count: '))  # determines how many links we follow
position = int(input('Enter position: '))     # determines when we want to stop

# to repeat desired times/ range() is commonly used w/ for loops to determine loop length
for i in range(repeat):  # repeat is passed into range() to repeat desired amount of times
    html = urllib.request.urlopen(url, context=ctx).read()  # opens link
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')  # find all anchor tags
    print("Retrieving: ", url)
    count = 0
    for tag in tags:  # keeps track of how many links we have followed!
        count = count + 1

        # stopping at desired position
        if count > position:  # compares position from input to count to determine when we have reached dest
            break
        url = tag.get('href', None)
        name = tag.contents[0]  # acquires tag contents which is the name and stores it into name

print(name)
