#Discount
#discount>= 500 then 10% discount
mrp= float(input("enter mrp of book"))
discount =0
netprice =0
if mrp>=500:
    discount=mrp*10/100
else :
    discount=mrp*5/100
    net =mrp-discount
    print(f"mrp={mrp}, discount={discount}, net={net}")    