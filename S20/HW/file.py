import random

def write_file():
    f = open("numbers.txt", mode="w")
    for n in range(10):
        number = random.randint(1, 9)
        f.write(str(number) + "\n")
    f.close()

def count(n, lst):
    c = 0
    for i in lst:
        if i == n:
            c += 1
    return c

def count_numbers():
    f = open("numbers.txt")
    lines = f.readlines()
    f.close()
    print(lines)
    new_lst_1 = []
    new_lst_2 = []
    while len(lines) != 0:
        i = lines[0]
        c = count(i, lines)
        new_lst_1.append(i)
        new_lst_2.append(c)
        for j in range(c):

            lines.remove(i)
    
    f2 = open("count.txt", mode="w")
    for i in range(len(new_lst_1)):
        number = ""
        for j in range(len(new_lst_1[i])-1):
            number += new_lst_1[i][j]
        f2.write(number + ": " + str(new_lst_2[i]) + "\n")
    f2.close()

write_file()
count_numbers()