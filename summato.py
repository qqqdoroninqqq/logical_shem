def xor(a,b):
    if (a==1 and b==0) or (a==0  and b==1):
        return True
    else:
        return False
a,b,p=[int(i) for i in input().split()]
k=xor(a,b)
pr=xor(k,p)
print(pr)
x1=a and b
x2= k and p
d=x1 or x2
print(d)



