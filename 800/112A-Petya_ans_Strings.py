a = input()
b = input()
a=a.lower()
b=b.lower()

array=[]

for i in range(len(a)):
    if a[i]==b[i]:
        array.append(0)
    if a[i]<b[i]:
        array.append(-1)
    if a[i]>b[i]:
        array.append(1)

for el in range(len(array)):
    if array[el] != 0:
        break
print(array[el])