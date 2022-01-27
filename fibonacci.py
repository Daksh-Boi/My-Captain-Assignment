n = int(input("Input the number of elements in the sequency: "))
f1 = 0
f2 = 1
print(f1)
print(f2)
i=1
while (i<=n-2):
    print(f1+f2)
    temp = f2
    f2=f1+f2
    f1=temp
    i=i+1
