import random
import time
from os import system

def pr_X(m):
    print("  A B C D")
    for i in range(4):
        print(i+1, end=" ")
        for j in range(4):
            print(m[i][j], end = " ")
        print()

def check(m1,m2,c):
    i1,j1,i2,j2 = c;
    m1[i1][j1] = m2[i1][j1];
    m1[i2][j2] = m2[i2][j2];
    pr_X(m1);
    time.sleep(5)
    system('cls');
    if m1[i1][j1] != m1[i2][j2]:
        m1[i1][j1] = "X";
        m1[i2][j2] = "X";

def ask():
    letters = "ABCD"
    numbers = "1234"
    t1 = input("Please, enter the coordinates of first card: ")
    while len(t1) != 2:
        while (t1[0] not in letters) or (t1[1] not in numbers):
            t1 = input("Please, enter the coordinates of first card: ")
    j1,i1 = map(str,t1)

    t2 = input("Please, enter the coordinates of second card: ")
    while len(t2) != 2:
        while (t2[0] not in letters) or (t2[1] not in numbers):
           t2 = input("Please, enter the coordinates of second card: ")
    j2,i2 = map(str,t2)
    cor = {"A": 0, "B": 1, "C": 2, "D": 3}
    j1, j2 = cor[j1], cor[j2]
    i1, i2 = int(i1)-1, int(i2)-1
    return i1,j1,i2,j2

mas_X = [["X"]*4 for i in range(4)];

mas = [[1]*4 for i in range(4)];

ch = ["!","@","#","$","%","^","&","*","!","@","#","$","%","^","&","*"];

for i in range(4):
    for j in range(4):
        n = random.randint(0,len(ch)-1)
        mas[i][j] = ch[n];
        ch.remove(ch[n]);

print("Hello player, you need to open all cards")
print("Successes!!!")
while mas_X != mas:
     pr_X(mas_X);
     print("Symbols are: !, @, #, $, %, ^, &, *")
     coord = ask();
     check(mas_X, mas, coord);
print("You Win!!!")
time.sleep(30)