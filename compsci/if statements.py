percentage=input('enter your percentage')
percentage=float(percentage)
if(percentage>90):
    print('you got an A')
elif percentage>80 and percentage<=90:
    print('you got a B')
elif percentage>=60 and percentage<=80:
    print('you got a C')
else:
    print('you got a D')
