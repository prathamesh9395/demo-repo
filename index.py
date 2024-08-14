print("hello world...!")
print("hello world...!")
def fun(l1, tar):
    d={}
    for i,num in enumerate(l1):
        d[num] = i
    for i in d:
        c = tar - i
        if c in d and d[c]!= 1:
            return d[i] , d[c]
l=[6,5,7,8,9,3]
print(fun(l, 10))
