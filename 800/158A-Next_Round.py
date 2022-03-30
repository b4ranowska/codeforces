n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
suma = 0
for i in a:
    if i == 0:
        continue
    if i >= a[k-1]:
        suma += 1
print(suma)


