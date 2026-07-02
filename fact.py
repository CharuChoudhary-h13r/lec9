# factorial

num=int(input("enter a numberr:"))
f=1
for i in range(1,num+1):
    f=f*i
print(f"the factorial of {num}is {f}")


num=int(input("enter a numberr:"))
f=1
for i in range(1,num+1):
    print(f"{i}x", end="")
    f=f*i
print(f"={f}")


num=int(input("enter a numberr:"))
f=1
for i in range(1,num+1):
    print(f"{i}x", end="")
    f=f*i
print(f"/b={f}")