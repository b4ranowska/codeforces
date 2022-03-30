words = []
x = int(input())
for i in range(x):
    n = input()
    words.append(n)
for word in words:
    if len(word) <= 10:
        print(word)
    else:
        print(word[0] + str(len(word)-2) + word[-1])