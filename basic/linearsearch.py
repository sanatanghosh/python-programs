
# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lst) 
item = int(input("Enter the number to be searched: "))
found = False
for i in range (len(lst)):
    if lst[i]== item:
        found =True
        print("item matched")
        break
if found ==False:
        print("item is not present")