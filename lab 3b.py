def asc_check(li):
    for i in range(n-1):
        if(li[i]>li[i+1]):
            return False
    return True   
n=int(input("enter the number of elements in the list: "))
li=[int(input()) for i in range(n)]
print("ascending" if asc_check(li) else "not ascending")
