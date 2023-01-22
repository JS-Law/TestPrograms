largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    
    try: 
        smallest = int(num)
    except:
        smallest = -1
        print('Invalid input')
   
    for value in smallest:
        if smallest is None:
            smallest = value
        elif value < smallest:
            smallest = value
            
            
            
            
#### NEW code for a program that prompts the user for numbers, prints the largest and the smallest, with a try and except that filters unwanted input


largest = None
smallest = None

while True:
    
    #Enter Input, converts if data, prints invalid if not
    
    num = input("Enter a number: ")
    if num == "done" :
        break
    
    #the filter, if it can make this conversion it runs it through the logic, if not it skipts to except
    
    try: 
        num = int(num)
        
    except:
        print("Invalid input")
        continue
        
    #Comparisons between values
    
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
        
print("Maximum is", largest)
print("Minimum is", smallest)
    