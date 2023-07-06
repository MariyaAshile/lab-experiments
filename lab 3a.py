n=int(input("enter number of elements in the list: "))
li=[int(input()) for i in range(n)]
target=int(input("enter the element to be found: "))
p_ind=[]
n_ind=[]
for i in range(n):
    if(li[i]==target):
        p_ind.append(i+1)
        n_ind.append(-(len(li)-i))
if(p_ind==[] and n_ind==[]):
    print("element not found")
print(p_ind)
print(n_ind)
        
