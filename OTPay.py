#intially found that i was making the first conditional statement evaluate to FALSE
# If hours were less than 40, pay would equal rate times hours which would be False AND the math would be wrong.
# 45*r(or whatever user input would be) instead of 40*r 


hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h >= 40:
    pay = 40 * r
    if h > 40:          #then since i figured that the first conditional needed to be correct for the second to be evaluated, i
        ot = h - 40         #i nested the second conditional to calculate overtime pay by subtracting 40 from user input  
        ot = r * 1.5 * ot # and multiplying rate by ot rate and then by the hours left over from 40
print(pay + ot)
        
#I didnt use any resource other than my notebook.
#Good job keep at it
#Here is a function that prompts the user to enter hours/rate and it calculates for ot
def computepay():
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("Enter Rate:")
    r = float(rate)
    
    if h >= 40:
        pay = 40 * r
        if h > 40:   
            ot = h - 40 
            ot = r * 1.5 * ot
    return print('Pay' , pay + ot)

computepay()