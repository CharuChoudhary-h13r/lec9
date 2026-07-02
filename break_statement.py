# break statement the the control outside the loop
# cause of break in the loop become un natural death of the loop
# break terminate the loop in emergency 
# Q. enter a number and check is it prime or not
num=int(input("enter a number :"))
i=2
while i<num:
     if num %i==0:
        break 
     i=i+1
if(i==num):
   print(num,"is prime number") 
else:
    print(num,"is not prime number")
