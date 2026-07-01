#print_2star_in_eachrow
#initialized the  outer loop counter
#nested loop: when we use a loop inside another loop
i=5
while i>=1:
    j=5
    while j>=i:
        print(f"{j}",end=" ")
        j=j-1
    print()
    i=i-1


