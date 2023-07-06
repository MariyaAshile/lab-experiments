a=[-2,-3,4,5,6]
tup=()
for i in a:
    if i>0:
        tup=tup+(i,)
print("tuple after removing negative values: ",tup)
