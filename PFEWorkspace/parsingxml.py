from urllib import request
import xml.etree.ElementTree as ET

url = input("Enter Location: ")
print ("Retrieving", url)
html = request.urlopen(url) # STORES HTML WITHIN VARIABLE
data = html.read()          # READS THE DATA INTO VARIABLE DATA
print("Retrieved",len(data),"characters")

tree = ET.fromstring(data)  # MOST IMPORTANT LINE, GIVES US GOOD XML TO WORK WITH
results = tree.findall('comments/comment') # CREATES LIST WE CAN LOOP OVER
icount=len(results) # PRINTS LENGTH OF LIST
isum=0

for result in results:
    isum += float(result.find('count').text) # CONVERTS THE TEXT TO FLOAT AND ADDS IT TO ITSELF THEN SUM
print(icount)
print(isum)
