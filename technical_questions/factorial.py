def fact(n):
    if n ==1:
        return 1
    else:
        return (n*fact(n-1))
x= int(input("enter the number "))
f= fact(x)
print("the factorial of x is ", f)