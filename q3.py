import math
n = 600851475143 
maxprime = 0
while n%2 == 0:
    maxprime = 2
    n << 1


for i in range(3,int(math.sqrt(n)),2):
    while n % i == 0:
        maxprime = i
        n = n/i
        
if n>2:
    maxprime = n

print(maxprime)
