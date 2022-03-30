matrix = []

rows = 5
cols = 5

for element in range(0, rows):
    matrix.append([int(i) for i in input().split()])

a = 0
b = 0

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 1:
            if i != 2:
                a = abs(2-i)
            if j != 2:
                b = abs(2-j)
            number_of_operations = a + b
print(number_of_operations)