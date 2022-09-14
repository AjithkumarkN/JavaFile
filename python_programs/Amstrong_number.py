print("enter the range of Amstrong NUmber:")
number=int(input("range of Amstrong number is:"))#get the range of Amstrong number
for i in range(number):
    num=i
    result=0
    n=len(str(i))
    while(i!=0):
        digit=i%10#it's get the value of last digit
        result=result+digit**n#add digit + cuib value of digit
        i=i//10
    if num==result:
        print(num,end=' ')#end keyword used to allocate the space for end of the line
print("\nplease.., give the number is Amstrong number:")
number1=int(input('check given number is Amstrong or not:'))
result1=0
temp=number1
while(temp>0):
    digit1=temp%10
    result1 +=digit1**3
    temp//=10
if number1==result1:#check the condition is Amstrong or mot
    print(number1,"is Amstrong")
else:
    print(number1,"is not Amstrong number")

