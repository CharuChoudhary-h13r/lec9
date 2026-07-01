numbers=range(1,11,1)
for i in numbers:
    print(i) 

numbers=range(10,0,-1)
for i in numbers:
    print(i) 

numbers=range(1,11,1)
for i in numbers:
    print(i*i) 


numbers=range(1,11,1)
x=1
for i in numbers:
    print(x)
    x=x*2


numbers=range(1,11,1)
num=int(input("Enter a number:"))
for i in numbers:
    print("{num} x{i}={num*i}")