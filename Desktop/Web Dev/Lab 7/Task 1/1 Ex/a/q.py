v = int(input())
s = int(input())
print(s//v + (s%v + v -1) // v)