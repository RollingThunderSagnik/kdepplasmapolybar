def fuzTime():
    import datetime
    x = datetime.datetime.now()
    x = int(x.strftime("%w"))
    # print(type(x))
    if(x==0):
        # print('রবিবার')
        print('SUNDAY ')
    elif (x==1):
        # print('সোমবার')
        print('MONDAY ')
    elif (x==2):
        # print('মঙ্গলবার')
        print('TUESDAY ')
    elif (x==3):
        # print('বুধবার')
        print('WEDNESDAY ')
    elif (x==4):
        # print('বৃহস্পতিবার')
        print('THURSDAY ')
    elif (x==5):
        # print('শুক্রবার')
        print('FRIDAY ')
    elif (x==6):
        # print('শনিবার')
        print('SATURDAY ')


if __name__ == "__main__":
    fuzTime()
