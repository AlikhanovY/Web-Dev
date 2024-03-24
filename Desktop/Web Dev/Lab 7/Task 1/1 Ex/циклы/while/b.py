a = float(input())
n = int(input())

sum_result = 1

for i in range(1, n + 1):
    sum_result += a ** i

print(sum_result)