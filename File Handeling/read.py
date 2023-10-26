f = open("demo.txt", "rt")

print(f.read(1))
print(f.read(1))

for x in f:
    for y in x:
        print(y)
