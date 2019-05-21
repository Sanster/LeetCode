import math

n = 19
end = n
start = 1
mid=(start+end)/2.0

count = 0
print(math.sqrt(y))

while abs(mid**2 - n) > 0.00001:
    count += 1
    
    if mid**2 < n:
        start = mid
        mid = (start + end) / 2.0
    elif mid**2 > n:
        end = mid
        mid = (start + end) / 2.0
    else:
        break
        
print(x)
print(count)
