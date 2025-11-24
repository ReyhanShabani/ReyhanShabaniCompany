f = open("a.txt")
lines = f.readlines()
f.close()

g = open("b.txt", mode="w")
for l in range(len(lines) - 1, -1, -1):
    if l == len(lines) - 1:
        g.write(str(lines[l]) + "\n")
    else:
        g.write(str(lines[l]))
g.close()