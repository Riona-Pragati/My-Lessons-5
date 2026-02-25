file = open("A.txt", "r")

print("----- Full File Contents -----")
print(file.read())

file.seek(0)
print("\n----- First 10 Characters -----")
print(file.read(10))

file.seek(0)
print("\n----- First Line -----")
print(file.readline())

file.seek(0)
print("\n----- First 4 Lines -----")
for i in range(4):
    print(file.readline(), end="")

file.seek(0)
print("\n----- Loop Through All Lines -----")
for line in file:
    print(line, end="")

file.close()
