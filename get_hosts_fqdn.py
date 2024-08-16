## https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
## https://www.educative.io/answers/how-to-find-the-domain-name-using-an-ip-address-in-python

import socket


def getNetworkIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('<broadcast>', 12345))  # 12345 is random port. 0 fails on Mac.
    return s.getsockname()[0]


def get_domain_name(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return "No domain name found"


ip_address = getNetworkIp()
domain_name = get_domain_name(ip_address)
print(f"The domain name for {ip_address} is {domain_name}")
