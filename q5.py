# coding: utf-8
# Your code here!

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
def lcm(a,b):
    return (a*b)/gcd(a,b)
    
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n =len(a)
result = a[0]
for i in range(1,n):
    result = lcm(a[i],result)
print(result)
