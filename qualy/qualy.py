import sys

num_periods = int(input())
total = 0
for i in range(num_periods):
    a, b = map(float, input().split())
    total += a * b
print(total)