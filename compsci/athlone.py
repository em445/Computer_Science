athlone=input('are you living in athlone')
if athlone == ('y'):
    age= input ('enter your age')
    age=float(age)
    if age<18:
        print('you are too young to vote')
    else:
         registered =input("are you registered to vote")
         if registered == 'y':
             print('you can go and vote')
         else:
             print('you need to register to vote')
else:
    print('you cannot vote')