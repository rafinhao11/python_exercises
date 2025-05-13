a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))


if (a > b):
    x = a
    a = b
    b = x
    
if (a > c):
    x = a
    a = c
    c = x

if (b > c):
    x = b
    b = c
    c = x

print(a, b, c)