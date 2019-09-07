import random
string = "1000 1000\n"
for i in range(1000):
    r1 = random.randint(1, 1000)
    r2 = random.randint(1, 1000)
    string += str(r1) + " " + str(r2) + "\n"
string = string[:-1]
with open("2.in", "w+") as file:
    file.write(string)