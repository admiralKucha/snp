import datetime

def date_in_future(integer):
    date = datetime.datetime.now()
    time = str(date.time())[:-7]
    date = str(date.date())
    if type(integer) == int:
        d = str(int(date[8:10]) + integer)
    else:
        d = date[8:10]
    return d+date[4:8]+date[0:4] + " " + time

    print(date)

print(date_in_future([]))
print(date_in_future(2))