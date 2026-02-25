file = open("B.txt", "r")

print(file.read())

file.seek(0)
print(file.readline())

file.seek(0)
for i in range(4):
    print(file.readline(), end="")

file.seek(0)
for line in file:
    print(line, end="")

file.close()
