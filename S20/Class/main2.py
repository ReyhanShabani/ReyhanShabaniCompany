f = open("a.txt")
lines = f.readlines()
f.close()

g = open("b.txt", mode="w")
for l in lines:
    g.write(l)
g.close()