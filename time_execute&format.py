def Time(x=int(input('enter your time in seconds: '))):
    if int(x) == 0:
        print('now')

    elif int(x) > 0 and int(x) < 60:
        if x == 0:
            exit()
        sec = int(x)
        print(str(sec) + ' seconds ')

    elif int(x) >= 60 and int(x) < 60*60:
        min = int(int(x) / 60)
        rest = int(x) % 60
        print(str(min) + ' minutes')
        if rest == 0:
            exit()
        r = str(Time(rest))

    elif int(x) >= 60*60 and int(x) < 60*60*24:
        hour = int(int(x) / (60*60))
        rest = int(x) % (60*60)
        print(str(hour) + ' hours')
        if rest == 0:
            exit()
        r = str(Time(rest))

    elif int(x) >= 60*60*24 and int(x) < 60*60*24*7:
        day = int(int(x) / (60*60*24))
        rest = int(x) % (60*60*24)
        print(str(day) + ' days')
        r = str(Time(rest))

    elif int(x) >= 60*60*24*7 and int(x) < 60*60*24*7*4:
        week = int(int(x) / (60*60*24*7))
        rest = int(x) % (60*60*24*7)
        print(str(week) + ' weeks')
        if rest == 0:
            exit()
        r = str(Time(rest))

    elif int(x) >= 60*60*24*7*4 and int(x) < 60*60*24*7*4*12:
        month = int(int(x) / (60*60*24*7*4))
        rest = int(x) % (60*60*24*7*4)
        print(str(month) + ' months')
        r = str(Time(rest))

    elif int(x) >= 60*60*24*7*4*12:
        year = int(int(x) / (60*60*24*7*4*12))
        rest = int(x) % (60*60*24*7*4*12)
        print(str(year) + ' years')
        if rest == 0:
            exit()
        r = str(Time(rest))

    else:
        print('not valid')

Time()