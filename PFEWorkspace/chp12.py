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

# Unicode Characters and Strings
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
            
            
            @10:51
        



"""
