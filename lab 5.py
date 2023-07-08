def is_subset(a,b):
    for i in b:
        if i not in a:
            return False
    return True
a={2,3,4,5,6,7}
b={2,4,6}
if is_subset(a,b):
    print("set B is a subset of set A")
else:
    print("set B is not a subset of set A")
