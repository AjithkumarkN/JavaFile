print("welcome to count occurrence program")
def count_value (list, number):
    count=0
    for i in list:
        if (i == number):#check the value how many time occure
            count += 1
    return count


Empty_list = []#it's empty list for getting the value from user
number=int(input("enter the  size of list:"))

for li in range(0, number):#user input range
    num=int(input())
    Empty_list.append(num)#append user input value as a list

print(Empty_list)
value=int(input("enter the value of finding occurrence value:"))
print("{} appear in {} times".format(value,count_value(Empty_list, value)))
#this  is another type it have default input
print("............Another type of Occurrence program.................")
list_number=[1,2,3,1,2]
print("list out the list values:", list_number)
numbe =int(input("enter the number:"))
numb=list_number.count(numbe)
count1=0
for i in range(numb):
    if i==i:
        count1+=1#count the occurent values
print(numbe, 'Occurrence in', count1, 'times')
#this type check how many word Occure:
print(".......String Appear program.......")
name=input("enter the name:")

name1=input("Finding Occurrence word:")
print(name1,"is Appear in ",name.count(name1))