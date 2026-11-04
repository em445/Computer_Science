first=input('enter a number')
first=float(first)
second=input('enter a second number')
second=float(second)
third=input('enter a third number')
third=float(third)
largest=first
if first<second:
    largest=second
if largest<third:
    largest=third
print(f'{largest} is the largest number')
