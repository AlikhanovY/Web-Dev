n = int(input())

sum_result = 0

for i in range(1, n + 1):
    sum_result += 1 / (i ** 2)

print(sum_result)