a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))

ra2 = a - 2 * int(a / 2)
ra3 = a - 3 * int(a / 3)

if ra2 == 0 or ra3 == 0:
    print(a)

rb2 = b - 2 * int(b / 2)
rb3 = b - 3 * int(b / 3)

if rb2 == 0 or rb3 == 0:
    print(b)

rc2 = c - 2 * int(c / 2)
rc3 = c - 3 * int(c / 3)

if rc2 == 0 or rc3 == 0:
    print(c)

rd2 = d - 2 * int(d / 2)
rd3 = d - 3 * int(d / 3)

if rd2 == 0 or rd3 == 0:
    print(d)