from ipaddress import *


network_list = []
ip_list = []

# The list of IP's that show up in the pcap
given_ip_list = ["198.18.190.97","192.168.253.241","192.168.206.157",
"192.168.186.29","172.24.82.98","172.23.138.60","172.21.64.145",
"172.19.122.123","172.18.181.208","172.17.93.89"] 

# The file containing network lists in CIDR format (classless inter-domain routing)
with open("./ip_ranges.txt","r") as file:
    for line in file:
        network_list.append(line.strip())


# convert list of CIDR's to list of IP addresses
for network in network_list:
    for addr in IPv4Network(network):
        ip_list.append(str(addr))

# check our given IP's with the list of IP's in the PCAP
for ip in given_ip_list:
    if ip in ip_list:
        print(ip)