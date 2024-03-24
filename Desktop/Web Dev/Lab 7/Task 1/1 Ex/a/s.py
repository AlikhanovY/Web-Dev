h = int(input())
a = int(input())
b = int(input())
d = 0
c = 0
while(True):
    c += 1
    if(d < h):
        d += a
        d -= b
    else:
        break
print(c)
