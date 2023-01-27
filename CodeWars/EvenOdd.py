# def even_or_odd(number):
#  return 'Even' if number % 2 == 0 else 'Odd'
# review syntax regarding functions
'''
def is_leap(year):
    inp = int(input("Enter Year"))

    leap = False
    if inp % 4 == 0:
        print("leap year!")
        return 'Leap year'
    elif inp % 100:
        print("not a leap year sorry bud")
        return False
    else:
        print("leap year!")
        return True
'''
n = int(input("enter a number"))
inp = range(n + 1)
for element in inp:
  element = str(element)
  element = element.rstrip()

print(element)