# Networked Technology 12.1
""""""
"""
Transport Control Protocol(TCP)
    -Built on top of IP(Internet Protocol)
    -Assumes IP mighty lost some data - stores and retransmits data if it seems to be lost
    -Handles "flow control" using a transmit window
    -Provides a nice reliable "pipe"
    -Were going to focus on the end-to-end layer, and simplify the rest
    -"Communication between two applications" like a phone call
TCP Connections/Sockets
    -"In computer networking, an internet socket or network socket is an endpoint of bidirectional inter-process
    communication flow across an Internet Protocol-based network, such as the Internet"
    -PROCESS<------->INTERNET<------->PROCESS
TCP Port Numbers
    -A port is an application-specific or process-specific software communications endpoint
    -It allows multiple networked applications to coexist on the same server
    -There is a list of well-known port numbers
        Incoming Email -- Port: 25
        Login -- Port: 23
        Web Server -- Port: 80 and 443 (We are going to primarily work with Port 80)
        Personal Mailbox -- Port: 109 and 110
Common TCP Ports
    -Telnet (23) - Login            Imap    (143/220/993) - Mail Retrieval
    -SSH    (22) - Secure Login     POP     (109/110)     - Mail Retrieval
    -HTTP   (80)                    DNS     (53)          - Domain Name
    -Https  (443)- Secure           FTP     (21)          - File Transfer
    -SMTP   (25) - Mail
Sockets in Python
    -Python has built-in support for TCP Sockets!
ex.
import socket                                               #First we need to import the socket module
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Creates some endpoint thats not yet connected
mysock.connect( ('data.pr4e.org', 80) )                     #HOST = data.pr4e.org PORT = 80
                                                            #Essentially "dials the phone"
"""

# Hypertext Transfer Protocol(HTTP) 12.2
"""
Application Protocol
    -Since TPC (and Python) give us a reliable socket, what do want to do with the socket? 
    What problem do we want to solve?
    -Application Protocols
        -Mail
        -World Wide Web
    -There are rules to describe how we talk with them
    -Think: When we call someone, there is a "protocol" that we all follow. A greeting. A "Hello"
    Then hopefully you start talking!

HTTP - Hypertext Transfer Protocol
    -The dominant Application Layer Protocol on the Internet!
    -Invented for the Web - to retrieve HTML, Images, Documents, etc
    -Extended to be data in addition to documents - RSS, Web Services, etc
    Basic concept: Make a connection - Request a document - Retrieve a document - Close the connection
    -Simple right??
    -So simple that 
HTTP
    -The Hypertext Transfer Protocol is the set of rules that allow browsers to retrieve web documents over the
    Internet

What Is a Protocol?
    -A set of rules that all parties follow so we can predict each others behavior
    -And not bump into each other
        -On two way roads in the USA, drive on the right hand side of the road
        -On two way roads in the UK, drive on the left hand side of the road
    -One of the things that HTTP standardized was Uniform Resource Locators or URLS

        http://www.dr-chuck.com/page1.htm   <-- Uniform Resource Locator(URL)
  Protocol^      Host^       Document^

Getting Data From The Server
    -Each time the user clicks on an anchor tag with an href= value to switch to a new page, the browser makes
    a connection to the web server and issues a "GET" request - to GET the content of the page at the specified URL
    -The server returns the HTML document to the browser which formats and displays the document to the user!
    -What an insane concept, links to other documents within documents. 
    -The Internet really is just other peoples computers
    -Clickable links are Anchors

Clicking a Link To Another Page(REQUEST/RESPONSE CYCLE)
    -Lets say we are on "http://www.dr-chuck.com/page1.htm" and there is a link to Page 2
    -If we click on the link, we initiate a GET REQUEST on PORT:80 
        -Then the web server may run some software to figure out the document associated
        -Parses the markup language, and displays the webpage on the SAME SOCKET
              
              WEBSERVER PORT:80 
                     ^       
                     V
                     
     CLICK <----> BROWSER <----> PARSE/RENDER(Display)
   (REQUEST)                          (RESPONSE)
    
Internet Standards
    -The standards for all Internet protocols(inner workings) are developed by an organization
    -Internet Engineering Task Force(IETF)
    -www.ietf.org
    -Standards are called "RFCs" - "Request for Comments"
    -"No matter how perfect we think we have these standards, we request for comments because they can always be
    improved"
    -RFC 2616 is the HTTP RFC which standardizes the way in which we communicate to the server
        -GET must be in all caps etc..

Making an HTTP Request
    -Connect to the server like "www.dr-chuck.com"
    -Request a document(or the default document)
        -GET http://www.dr-chuck.com/page1.htm HTTP/1.0
        -GET http://www.mlive.com/ann-arbor/ HTTP/1.0
        -GET http://www.facebook.com HTTP/1.0

An HTTP Request in Python
ex.
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Basically makes a doorway
mysock.connect(('data.pr4e.org', 80)) #Goes and finds the server, connects to port 80, establishes the socket
cmd = 'GET http://data.pr4e.org/romet.txt HTTP/1.0\r\n\r\n'.encode() #Now we can call methods on the socket
mysock.send(cmd)

while True:
    data = mysock.recv(512) #We're going to receive up to 512 characters
    if (len(data) < 1):     #If we get no data it means end of file or transmission
        break
    print(data.decode())    #If we do, were going to decode it!
mysock.close()
         
"""

# Using the Developer Console to Explore HTTP
# Status: 200 means "Youre good!!:
# Status: 404 means NOT FOUND
# Status: 302 means redirection, GET request for the page you WERE looking for, cause it aint here

# Unicode Characters and Strings 12.3
"""
Representing Simple Strings
    -Each character is represented by a number between 0 and 256 stored in 8 bits of memory
    -We refer to 8 bits of memory as a "byte" of memory - (i.e. my disk drive contains 3 TeraBytes of memory)
    -The ord() function tells us the numeric value of the character
ex.
print(ord('H')) OP:72
print(ord('e')) OP:101
print(ord('\n'))OP:10

    -Explains why lowercase letters are greater than uppercase letters
        -Uppercase letters were the only option in earlier computers, therefore were translated into ASCII
        first.
        -Meaning uppercase letters are a lesser number value because there are 126 ASCII translations
Unicode
    -Unicode is universal code for hundreds of millions of characters
    -It became import for the universal exchange of the SAME data
Multi-Byte Characters
    -To represent the wide range of characters computers must handle, we represent characters with more than one byte
        -UTF-16 - Fixed Length - Two Bytes  #
        -UTF-32 - Fixed Length - Four Bytes #
        -UTF-8  - 1-4 Bytes
            -Upwards compatible with ASCII
            -UTF-8 is recommended practice for encoding data to be exchanged between systems
            - 1, 2, 3, OR 4 characters
            -Automatically detectable
            
Two Kinds of Strings in Python
    -in Python 3, ALL strings are unicode
Python 3 and Unicode
    -In Python 3, all strings internally are UNICODE!!!
    -Working with string variables in Python programs and reading data from files usually "just works"
    -When we talk to a network resource using sockets or talk to a database we have to encode and decode data
        -Usually to UTF-8
        -99% code usually will be UTF-8
Python String to Bytes
    -When we talk to an external resource like a network socket, we send bytes, so we need to encode Python 3 strings 
    into a given character encoding
    -When we read data from an external resource, we must decode it based on the character set so it is properly 
    represented in Python 3 as a string!
ex.
while True
    data = mysock.recv(512)         #recieves up to 512 bytes (data variable is bytes)
    if ( len(data) < 1 ) :          #if data length is less than 1, break loop, transmission has ended
        break
    mystring = data.decode()        #we pass decode() into data and assign it to a new variable 'mystring'
    print(mystring)                 #decode() by default decodes to UTF-8 or ASCII(dynamically)

An HTTP Request in Python
ex.
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #BYTES!!!!!!(UTF-8 or ASCII)
mysock.send(cmd)    #send argument is 'cmd; which are BYTES

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='') #Decode upon receiving data!

mysock.close()

SEND --------> ENCODE
RECEIVE -----> DECODE


"""

# Retrieving Web Pages
"""
DRY(Coding Concept)
    -Dont Repeat Yourself
    -In an effort to be DRY, programmers already have written a library that handles the REQ/REP cycle for us!
    
Using urllib in Python
    -Since HTTP is so common, we have a library that does all the socket work for us and makes
    web pages look like a file!
    -Thats honestly pretty sick!
ex._______________________________________________
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.data.pr4e.org/romeo.txt')
for line in fhand:                  
    print(line.decode().strip())    #the iterable variable line comes in as BYTE ARRAY and we must decode on way in

If We Can Open Web Pages Like a File...
    -Start thinking of them like files
    -Start using urlopen() instead of open()
ex._______________________________________________
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split() #Since this is coming from network, we must decode from byte string to char string
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
"""

# Parsing Web Pages 12.5
"""
What is Web Scraping?
    -When a program or script pretends to be a browser and retrieves web pages, looks at those web pages, extracts
    information, and then looks at some more web pages
    -Search engines scrape web pages - we call this "spidering the web" or "web crawling"
Why Scrape?
    -Pull data - particularly social data - who links to who?
    -Get your own data back out of some system that has no "export capability"
    -Monitor a site for new information
    -Spider the web to make a database for a search engine
Scraping Web Pages
    -There is some controversy about web page scraping and some sites are a bit snippy about it
    -Republishing copyrighted information is not allowed
    -Violating terms of service is not allowed
    -Parsing HTML is very ugly and RegEx does not make it any easier because HTML can be so messy
        -FULL of syntax errors
        -Lets say you are searching for 'href=' or links and there are new lines strewn throughout in unexpected
        places. Your algorithm would blow up because it would not return correct values!
The Easy Way - Beautiful Soup
    -You could do string searches the hard way
    -Or the easy way by using Beautiful Soup from www.crummy.com
        -named something silly because HTML on the web is just that bad!
To Install Beautiful Soup
    -https://pypi.python.org/pypi/beautifulsoup4

Using Beautiful Soup To Parse Anchor Tags!
ex.______________________________________________
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter:')
html = urllib.request.urlopen(url).read() #Opens the url that weve assigned to input
soup = BeautifulSoup(html, 'html.parser') # Takes nasty HTML and cleans it up for us!

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
__________________________________________________
"""
# Summary!!
"""
The TCP/IP gives us pipes/sockets between applications
We Designed application protocols to make use of these pipes
HTTP is a simple yet powerful protocol
Python has good support for sockets, HTTP, and HTML parsing

"""