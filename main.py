# 1
n = int(input())
a = 1
b = 1
for i in range(n):
    print(a)
    a, b = b, a + b

# 2
n = int(input())
for i in range(1, n + 1):
    print(i, i + 1, i + 2)

# 3
n = int(input())
for i in range(1, n + 1):
    print("+" * n)

# 4
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()

# 5
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
