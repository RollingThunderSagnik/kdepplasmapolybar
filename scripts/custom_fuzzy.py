def fuzTime():
    import datetime
    y = datetime.datetime.now()
    x = int(y.strftime("%H"))
    z = int(y.strftime("%I"))
    m = int(y.strftime("%M"))
    if(m>40):
        z=z+1
        x=x+1
    # print(type(x))
    if(x<5):
        print("GHUMOTE JA ")
    elif (x<9):
        print("SOKAL {}'TA ".format(z))
    elif (x<12):
        print('BREAKFAST ')
    elif (x<14):
        print("DUPUR {}'TA ".format(z))
    elif (x==14):
        print("DUPUR {}'TO ".format(z))
    elif (x<17):
        print("BIKEL {}'TE ".format(z))
    elif (x<18):
        print("BIKEL {}'TA ".format(z))
    elif (x<20):
        print("SONDHYE {}'TA ".format(z))
    elif (x<23):
        print("RAAT {}'TA ".format(z))


if __name__ == "__main__":
    fuzTime()
