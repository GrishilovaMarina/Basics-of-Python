def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
        yield factorial

n = int(input())
print(list(fact(n)))


