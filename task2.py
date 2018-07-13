def sortmin(y):
    y = list(str(y))
    y.sort()
    w = y.count("0")
    for i in range(0, w):
        y.remove("0")
    if y[0] != "-":
        for i in range(0, w):
            y.insert(1, '0')
    elif y[0] == "-":
        for i in range(0, w):
            y.insert(2, '0')
    y = int("".join(str(i) for i in y))
    return int(y)


def sortmax(x):
    x = list(str(x))
    x.sort(reverse=True)
    if x[-1] == '-':
        x.pop()
        x.insert(0, "-")
    x = int("".join(str(i) for i in x))
    return int(x)


a = int(input("a = "))
b = int(input("b = "))
if sortmax(a) == sortmin(b):
    print("Numbers are the same")
elif a > 0 > b:
    print("MAX difference", sortmax(a) - sortmax(b))
elif a < 0 < b:
    print("MAX difference", sortmax(b) - sortmax(a))
elif a and b > 0:
    if sortmax(a) > sortmax(b):
        print("MAX difference", sortmax(a) - sortmin(b))
    else:
        print("MAX difference", sortmax(b) - sortmin(a))
elif a and b < 0:
    if sortmax(b) < sortmax(a):
        print("MAX difference", (sortmax(b) - sortmin(a)) * -1)
    else:
        print("MAX difference", (sortmax(a) - sortmin(b)) * -1)
# мы не пришли к общему решению. Каждый понял по своему
