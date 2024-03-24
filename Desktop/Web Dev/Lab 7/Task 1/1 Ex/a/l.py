n = int(input())
h = n // 3600 % 24
n = n % 3600
m = n // 60
if m < 10:
    m = "0" + str(m)
s = n % 60
if s < 10:
    s = "0" + str(s)
print(f"{h}:{m}:{s}")