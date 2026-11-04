sales=input('enter your monthly sales')
sales=int(sales)
if sales >40000:
   commission=sales*0.15
   print(commission,'is your commission')
else:
    commission=sales*0.05
    print(commission,'is your commission')
  