number=input('enter a number')
number=float(number)
if number>0:
   if number%2==0:
       print('this number is even')
   else:
        print('the number is odd')
        
elif number < 0:
    print('the number is negative')
else:
    print('the number is equal to 0')
   