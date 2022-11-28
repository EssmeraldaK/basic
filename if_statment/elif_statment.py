print('hello')
for i in range(5):
    print(f'Iteration# :{i}')

    age=int(input("please enter your age"))

    if 0<age<17:
        print('Sorry,you are still young')
    elif 17<=age<25:
        print('Good you are eligible')
    elif 25<=age<120:
        print('Great,if you have DL')
    else:
        print('Come on be realistic')

