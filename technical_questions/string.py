x= []
n = int(input("enter the no of elements in list"))
for i in range(0,n):
    ele=int(input())
    x.append(ele)
print(x)
print("the max element of the list is",max(x))
print("the length of the list is", len(x))