def check(st1,st2):
    i=0
    j=0
    while i<len(st1) and j<len(st2) :
        if (st1[i]==st2[j]):
            j+=1
        i+=1
    return j==len(st2)
st1=input("enter string1 b: ")
st2=input("enter string2: ")
if check(st1,st2):
    print("YES")
else:
    print("NO")
