x =int(input("enter number to check prime number "))
for i in range (2, x):
    if x%i==0:
        print (x,"this is a not a prime number")
        break
else:
    print("the number is prime")