price=input('enter your cost price')
price=float(price)
if(price>10000):
    tax=price*0.15
    print(f'the tax you have to pay is {tax}')
elif price>5000 and price<=10000:
    tax=price*0.10
    print(f'the tax you have to pay is {tax}')
else:
    tax=price*0.05
    print(f'the tax you have to pay is {tax}')