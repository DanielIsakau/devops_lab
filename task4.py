import random
T = 0
dic = {}
N = int(input("Number of neighbors:"))
for i in range(0, N):
    dic[random.randint(0, 100)] = random.randint(0, 1)
for key, value in dic.items():
    if value == 1:
        if key > T:
            T = key
print("The oldest age is ", T)
print(dic)
