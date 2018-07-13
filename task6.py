import ipaddress

n = int(input("How many masks: "))
masks = list()
ips = list()
for i in range(n):
    masks.append(input("Mask %s: " % (i + 1)))
P = int(input("How many IP pairs: "))
for i in range(P):
    ips.append(input("Pair %i IP 1: " % (i + 1)))
    ips.append(input("Pair %i IP 2: " % (i + 1)))
for i in range(0, P):
    Count = 0
    pr1 = ipaddress.ip_address(ips[i])
    pr2 = ipaddress.ip_address(ips[i + 1])
    for j in range(int(n)):
        IP1 = ipaddress.ip_address(ips[i])
        IP2 = ipaddress.ip_address(ips[i + 1])
        net = ipaddress.IPv4Network(ips[i] + '/' + masks[j], False)
        ipnet = ipaddress.ip_network(net)
        if IP1 and IP2 in ipnet:
            Count += 1
    print("Number of subnets are %s %s located =" % (pr1, pr2), Count)
