# coding: utf-8
# Your code here!

x,y = 1,2
sum = 0
limit = 4*(10**6)
while x< limit:
    if x%2 == 0:
        sum += x
    x,y = y,x+y
print(sum)
