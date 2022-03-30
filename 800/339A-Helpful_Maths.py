numbers=input()
numbers_split=numbers.split('+')
numbers_split.sort()
result: str = numbers_split[0]
for i in range(1, len(numbers_split)):
    result += ("+" + numbers_split[i])
print(result)



