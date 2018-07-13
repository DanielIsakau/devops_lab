a = input("input string:")
sum = {}
for i in range(len(a)):
    if a[i] in sum:
        sum[a[i]] += 1
    else:
        sum[a[i]] = 1
keys = sorted(sorted(sum, reverse=True), key=sum.get)
keys = keys[::-1]

for i in range(3):
    print(keys[i], sum[keys[i]])
