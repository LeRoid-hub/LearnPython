try:
    f = open("demo1.txt", "x")
    f.write("HI")
    f.close()

except:
    pass

f = open("demo1.txt")
print(f.read())
