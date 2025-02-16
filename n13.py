from ipaddress import *

# net = ip_network('172.16.168.9/255.255.248.0', False) # задаем сеть по узлу и маске или адресу сети и маске
# print(net) # выводит адрес сети и через '/' кол-во единиц в маске
# print(net.network_address) # выводит адрес сети
# print(net.netmask) # выводит маску сети
# print(list(net.hosts())) # выводит адрес сети кроме адреса сети и широко везательного
# print([yz for yz in net]) # выводит адрес сети
# print(ip_address('175.125.80.0'))
#
# x = f'{net.network_address:b}'
# print(x)
# print(x.count('1'))

# net = ip_network('172.16.168.9/255.255.248.0', False)
# count = 0
# for ip in net:
#     if f'{ip:b}'.count('1') % 5 != 0:
#         count += 1
# print(count)

# net = ip_network('228.172.236.0/255.255.240.0', False)
# count = 0
# for ip in net:
#     if f'{ip:b}'.count('1') % 5 != 0:
#         count += 1
# print(count)

# net = ip_network('214.187.224.0/255.255.224.0', False)
# count = 0
# for ip in net:
#     if f'{ip:b}'.count('1') % 6 != 0 and f'{ip:b}'[-4:] == '1000':
#         count += 1
# print(count)

# for mask in range(0, 33):
#     ip1 = ip_address('123.20.103.136')
#     ip2 = ip_address('123.20.103.151')
#     net1 = ip_network(f'{ip1}/{mask}', False)
#     net2 = ip_network(f'{ip2}/{mask}', False)
#
#     if net1 != net2 and ip1 in net1.hosts() and ip2 in net2.hosts():
#         print(net1.netmask)

# net = ip_network('100.135.223.130/255.255.252.0', False)
# print(net.network_address)

# for mask in range(0, 33):
#     ip = ip_address('57.179.208.27')
#     net = ip_network(f'{ip}/{mask}', False)
#     net_ip = ip_address('57.179.192.0')
#     if net.network_address == net_ip:
#         print(mask)

# from ipaddress import *
# net = ip_network('192.168.32.160/255.255.255.240', False)
# count = 0
# for ip in net:
#     if f'{ip:b}'.count('0') > 21:
#         count += 1
# print(count)

print(bin(192)[2:].count('1') + bin(214)[2:].count('1') + 2)
