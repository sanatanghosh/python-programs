x= [[1,2,3],[4,5,6],[7,8,9]]
print(x)
for i in range (len(x)):
    for j in range(len(x[0])):
        print(x[i][j],end='')
    print()