number=int(input("enter the number:"))
count=0
for i in range(1,number+1):
    if number%i==0:
        count+=1
if count==2:
    print(number,"is prime number")
else:
    print(number,'is not prime number')