#Did not need to convert pay back to string, I had an error 
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hrs = float(hrs)
rate = float(rate) #Could have multiplied the two floats
pay = str(hrs * rate) #Line in question
print('Pay: '+ pay) #Must have had a syntax error when adding the String and the Int