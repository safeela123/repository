for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

for i in range(0,6):
    for j in range(i):
        print(i ,end=" ")
    print()

num=0
for i in range(5,0,-1):
    num=num+1
    for j in range(i):
        print(num ,end=" ")
    print()

for i in range(5,0,-1):
    for j in range(i):
        print(5, end=" ")
    print( )

for i in range(6,1,-1):
    for j in range(0,i):
        print(j ,end=" ")
    print( )

for i in range(1,6):
    for j in range(0,i):
        print(i*2-1, end=" ")
    print( )

for i in range(5,0,-1):
    for j in range(0,i):
        print(i,end=" ")
    print( )

for i in range(1,6):
     for j in range(i,0,-1):
        print(j,end=" ")
     print( )

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print( )

n=4
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
            print("*",end=" ")
    print()


num=1
for i in range(0,4):
    for j in range(0,4):
        print(num,end=" ") 
        num+=1
    print()


for i in range(1,6):
    for j in range(1,i):
        print("*",end=" ")
    print()

for i in range(5):
    for j in range(1,n-i+1):
        print( " ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print( )

for i in range(5,0,-1):
    for j in range(1,5-i):
            print("",end="")
    for k in range(1,i+1):
            print("*",end="")
    print()

rows=5
k=2 * rows - 2
for i in range(rows,-1,-1):
    for j in range(k,0,-1):
        print(end =" ")
    k=k+1
    for j in range(0,i+1):
            print("*",end=" ")
    print()


