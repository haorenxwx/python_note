#69.py
x = 10

s,e = 1,x/2+1 #(x/2+1)^2 > x
while s<=e:
    mid = (s+e)/2
    if mid**2 == x:
        print mid
        break
    elif mid**2 >x:
        e = mid-1
    elif mid**2 <x:
        s = mid+1
print e