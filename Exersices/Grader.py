#this was faily simple, i didnt need to combine anything or do much conversion. 
#i did not account for error checking, mainly because i knew what i would enter into the program, but to do so i would have to 
#add an additional line, declaring a condtion for a value out of range
#probably something like 
#if sc > 1
#   print('Please Enter a Valid Score')


score = input("Enter Score: ")
sc = float(score)

if sc >= 0.9:
    print('A')
elif sc >= 0.8:
    print('B')
elif sc >= 0.7:
    print('C')
elif sc >= 0.6:
    print('D')
elif sc < 0.6:
    print('f')
    
    
########### NEW CODE WITH ERROR CHECKING

#score = input("Enter Score: ")
#sc = float(score)
#if sc > 1:
#   print('Error. Please Provide a Valid Score')
#elif sc >= 0.9:
#    print('A')
#elif sc >= 0.8:
#    print('B')
#elif sc >= 0.7:
#    print('C')
#elif sc >= 0.6:
#    print('D')
#elif sc < 0.6:
#    print('f')