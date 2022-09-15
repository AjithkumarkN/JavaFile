number=int(input("enter the size of values:"))
li=[]#using Empty list to get the user input values
for i in range(number):
    num=int(input())
    li.append(num)

li.sort()#order the list values
print(li)
print("smallest element is :",li[0])#find smallest number in the list
print("largest element is :",li[-1])#find largest number in the list
print("smallest element is :",min(li))#find minimum value in the list using min() function
print("largest element is :",max(li))#find maximum value in the list using max() function
print("find second Largest number in the list:",li[-2])#find second largest number in the list
print("find second smallest number in the list:",li[1])#find second smallest number in the list, because array index start in 0 position
