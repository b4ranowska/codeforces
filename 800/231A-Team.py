n = int(input())
solutions = []
for i in range(n):
    m = input()
    solutions.append(m)

i = 0
for s in solutions:
    if s.count('1') >= 2:
        i += 1
print(i)