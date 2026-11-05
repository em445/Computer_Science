budget=input('enter your budget')
budget=float(budget)
season=input('enter the season')
if budget<=100:
    print('your destination is somewhere in Moldova')
    if season=='summer':
        print('camp-15.00')
    elif season=='winter':
        print('hotel-52.50')
if budget<=1000:
    print('your destination is somewhere in the Balkans')
    if season=='summer':
        print('camp-124.80')
    elif season=='winter':
        print('hotel-542.82')
if budget>1000:
    ('your destination is somewhere in Europe')
    if season=='summer':
        print('hotel-1350.00')
    elif season=='winter':
        print('hotel-542.82')

    