for i in range(4):
    print(i)

    c=(input("please enter your color"))

    if c=='green':
        print(f'player {c} 5 points')
    elif c=='black':
        print(f'player {c} 10 points')
    elif c=='red':
        print(f'player {c} 25 points')
    else:
        print(f'your color {c.upper()} not exist')