import os
import time
def esc(code):
    return f"\u001b[{code}m"

GREEN = esc(42)
BROWN = esc(43)
BIRUSA = esc(46)
RED = esc(41)
BLUE = esc(44)
WHITE = esc(107)
PURPLE = esc(45)
BLACK = esc(48)
END = esc(0)


def elka_red():
    print(WHITE + "  "*25 + END)
    print(WHITE + "  " * 12 + BIRUSA + "  " * 1 + WHITE + "  "*12 + END)
    print(WHITE + "  " * 11 + BIRUSA + "  " * 3 + WHITE + "  "*11 + END)
    print(WHITE + "  " * 12 + BIRUSA + "  " * 1 + WHITE + "  " * 12 + END)
    print(WHITE + "  " * 11 + RED + "  " + GREEN + "  " * 2 + WHITE + "  " * 11 + END)
    print(WHITE + "  " * 10 + GREEN + "  " * 3 + BLUE+ "  " + GREEN +"  " + WHITE + "  " * 10 + END)
    print(WHITE + "  " * 10 + GREEN + "  " * 1 + RED + "  " + GREEN +"  " * 3 + WHITE + "  " * 10 + END)
    print(WHITE + "  " * 9 + GREEN + "  " * 4 + RED + "  " + GREEN + "  " * 2 + WHITE + "  " * 9 + END)
    print(WHITE + "  " * 9 + GREEN + "  " + RED + "  " + GREEN + "  " * 3 + RED + "  " + GREEN + "  "*1 + WHITE + "  " * 9 + END)
    print(WHITE + "  " * 8 + GREEN + "  " * 1 + BLUE + "  " + GREEN + "  " * 4 + RED + "  " + GREEN + "  "*2 + WHITE + "  " * 8 + END)
    print(WHITE + "  " * 8 +  GREEN + "  " * 3 + RED + "  " + GREEN + "  " * 3 + BLUE + "  " + GREEN + "  "*1 + WHITE + "  " * 8 + END)
    print(WHITE + "  " * 7 +  GREEN + "  " * 1 + BLUE + "  " + GREEN + "  " * 3 + RED + "  " + GREEN + "  "*3 + RED + "  " + GREEN + "  " + WHITE + "  " * 7 + END)
    print(WHITE + "  " * 7 + RED + "  " + GREEN + "  " * 4 + RED + "  " + GREEN + "  "* 1 + BLUE + "  " + GREEN + "  "*3 + WHITE + "  " * 7 + END)
    print(WHITE + "  " * 6 + GREEN + "  " * 4  + RED + "  " + GREEN + "  " * 4 +  RED + "  " + GREEN + "  " * 3  + WHITE + "  " * 6 + END)
    print(WHITE + "  " * 6 + GREEN + "  " + RED + "  " + GREEN + "  " * 3 + BLUE + "  " + GREEN + "  " * 2 + RED + "  " + GREEN + "  "* 3 + RED + "  " + WHITE + "  " * 6 + END)
    print(WHITE + "  " * 5 + GREEN + "  " * 2 + RED + "  " + GREEN + "  " * 2 + RED + "  " + GREEN + "  " * 2 + BLUE + "  " + GREEN + "  "* 3 + RED + "  " + GREEN + "  " * 2 + WHITE + "  " * 5 + END)
    print(WHITE + "  " * 5 + GREEN + "  "  + BLUE + "  " + GREEN + "  " * 4 + RED + "  " + GREEN + "  " * 3 + RED + "  " + GREEN + "  "*2 + BLUE + "  " + GREEN + "  "+ WHITE + "  " * 5 + END)
    print(WHITE + "  " * 10 + BROWN + "  " * 5 + WHITE + "  " * 10 + END)
    print(WHITE + "  " * 11 + BROWN + "  " * 3 + WHITE + "  " * 11 + END)
    print(WHITE + "  " * 11 + BROWN + "  " * 3 + WHITE + "  " * 11 + END)
    print(WHITE + "  " * 25 + END)
for i in  range(100):
    RED, BLUE = BLUE, RED
    elka_red()
    time.sleep(0.5)
    os.system("clear")
        

