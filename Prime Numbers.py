primos = list()
for x in range(1, 1000):
    s = 0
    for c in range(1, x+1):
        if x % c == 0:
            s += 1
    if s == 2:
        primos.append(x)
print(primos)
