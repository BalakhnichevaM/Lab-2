# Балахничёва Мария 367852

def esc(code):
    return f"\u001b[{code}m"

GREEN = esc(42)
RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
PURPLE = esc(45)
BLACK = esc(48)
END = esc(0)

#1 пункт
print("Флаг Бонгладеша")
def flag_bongladesh():
    for i in range(2):
        print(GREEN + '   ' * 21 + END)
    for i in range(1,8, 2):
        print(GREEN + '   ' * ((21-i)//2) + RED + '   ' * i + GREEN + '   ' * ((21-i)//2) + END)
    for i in range(7,0, -2):
        print(GREEN + '   ' * ((21-i)//2) + RED + '   ' * i + GREEN + '   ' * ((21-i)//2) + END)
    for i in range(2):
        print(GREEN + '   ' * 21 + END)

print(flag_bongladesh())


# 2 пункт
x = int(input("введите число повторений арнамента: "))

def uzor(m):
    print((PURPLE + '  ' * 5 + BLACK + '  ' * 2+ END)*m)
    print((PURPLE + '  ' * 1 + BLACK + '  ' * 3 + PURPLE + '  ' * 1 + BLACK + '  ' * 2+ END)*m)
    print((PURPLE + '  ' * 1 + BLACK + '  ' * 1 + PURPLE + '  ' * 3 + BLACK + '  ' * 2+ END)*m)
    print((PURPLE + '  ' * 1 + BLACK + '  ' * 1 + PURPLE + '  ' * 1 + BLACK + '  ' * 4+ END)*m)
    print((PURPLE + '  ' * 1 + BLACK + '  ' * 1 + PURPLE + '  ' * 5 + END)*m)

print(uzor(x))

#3 пункт
print("График функции y = 2*x + 3")

print("19" + BLACK + '  '*7 + RED + ' '*2 + END)
print("17" + BLACK + '  '*6 + RED + ' '*2 + END)
print("15" + BLACK + '  '*5 + RED + ' '*2 + END)
print("13" + BLACK + '  '*4 + RED + ' '*2 + END)
print("11" + BLACK + '  '*3 + RED + ' '*2 + END)
print(" 9" + BLACK + '  '*2 + RED + ' '*2 + END)
print(" 7" + BLACK + '  '*1 + RED + ' '*2 + END)
print(" 5"  + RED + ' '*2 + END)
print(" 3" )
print(" 1")
print(" 0 1 2 3 4 5 6 7 8 9")


# 4 пункт

import csv
before_2015 = 0
cnt_zap = 0

with open("books.csv", encoding='cp1251') as csvfile:
    file = csv.reader(csvfile, delimiter = ";")
    for stroka in file:
        if stroka[0] == "ID":
            continue
        cnt_zap += 1
        if stroka[6][6:11] <= "2015":
            before_2015 += 1
prots_bf2015 = int((before_2015/cnt_zap)*100)
prots_aft2015 = int(((cnt_zap - before_2015)/cnt_zap)*100)

def kr_chislo(x):
    if str(x)[-1] in "01234":
        return x - x % 10
    if str(x)[-1] == "5":
        return x
    if str(x)[-1] in "6789":
        return x - x % 10 + 10
prots_bf2015 = kr_chislo(prots_bf2015)
prots_aft2015 = kr_chislo(prots_aft2015)

def bar_chart(m,n):
    k = max(m,n)
    for i in range(100, 0, -5):
        if i < 100 and i != 5:
            j = ' ' + str(i)
        elif i == 5:
            j = '  '+str(i)
        else:
            j = str(i)
        if m == i and n == i:
            print(j + BLACK + '  ' * 2 + GREEN + '  ' * 2 + BLACK + '  ' * 2 + PURPLE + '  '*2 + BLACK + '  '*2 + END)
            m -= 5
            n -= 5
        elif m == i:
            print(j + BLACK + '  '*2 + GREEN + '  '*2 + BLACK + '  '*5 + END)
            m -= 5
        elif n == i :
            print(j + BLACK + '  '*6 + PURPLE + '  '*2 + BLACK + '  '*2 + END)
            n -= 5
        else:
            print(j + BLACK + '  '*8 + END)
    print("     до 2015   после 2015")

print("Соотношение количества книг, изданных до и после 2015 года")
print(bar_chart(prots_bf2015, prots_aft2015))

