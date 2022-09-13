year=int(input("enter the year:"))
if year>1999 or year<4000:
    if year%4 == 0:
        print(year,"is Leap year")
    else:
        print(year,"is not Leap year")
else:
    print("invalid ")