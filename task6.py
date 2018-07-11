import ipaddress
MASK = list()
n = int(input("Number of masks: "))
Co = 0
for i in range(int(n)):
    k = input("Mask: ")
    MASK.append(k)
ips = list()
P = int(input("IP pairs = : "))
for j in range(int(P)):
    m = input("IP 1: ")
    p = input("IP 2: ")
    ips.append(m)
    ips.append(p)
ip_number = P * 2 - 1
same_network = list()
for s in range(int(P)):
    same_network.append(0)
for i in range(0, ip_number, 2):
    for j in range(int(n)):
        IP1 = ips[i]
        IP2 = ips[i + 1]
        Vmatch = MASK[j]
        net1 = ipaddress.IPv4Network(IP1 + '/' + Vmatch, False)
        ipnet1 = ipaddress.ip_network(net1)
        if ipaddress.ip_address(IP1) in ipnet1 and ipaddress.ip_address(IP2) in ipnet1:
            Co += 1
    print("Number of subnets ", Co)
