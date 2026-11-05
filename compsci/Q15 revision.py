number=input('enter a number')
number=float(number)
number2=input('enter a second number')
number2=float(number2)
if number>number2:
    print(number,'is greater than',number2)
elif number2>number:
    print(number2,'is greater than',number)
else:
    print('they are equal')