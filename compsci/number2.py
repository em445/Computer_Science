number=input('enter a number')
number=float(number)
second=input('enter a second number')
second=float(second)
if number>second:
    print(f'{number} is greater than {second}')
if second>number:
    print(f'{second} is greater than {number}')