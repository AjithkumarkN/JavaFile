factorial=int(input("enter the factorial number:"))
sum=1
for i in range(1,factorial+1):
    sum*=i
print(sum)