a = int(input("a:"))
b = int(input("b:"))
print("{0:b}".format(a))
print("{0:b}".format(b))
print("Hamming Distance: ", bin(a^b).count('1'))

