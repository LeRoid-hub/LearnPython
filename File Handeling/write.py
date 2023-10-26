f = open("demo.txt", "a")
f.write("-BAH")
f.close()

f = open("demo.txt")
print(f.read())

f = open("demo.txt", "w")
f.write("tom stinkt")
f.close()

f = open("demo.txt")
print(f.read())
