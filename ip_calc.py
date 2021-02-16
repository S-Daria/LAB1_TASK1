"""
LAB2 TASK1
GitHub: https://github.com/S-Daria/LAB1_TASK1.git
"""
import re


def validate_address(raw_address):
    rex_ip = re.compile("[0-9]{2,3}[.][0-9]{2,3}[.][0-9]{1,2}[.][0-9]{1,2}")
    if rex_ip.match(raw_address):
        print("Missing prefix")
        return False
    address_list = raw_address.split('/')
    try:
        address_list[-1] = int(address_list[-1])
    except ValueError:
        print("Error1")
        return False
    print(address_list[0])
    if not rex_ip.match(address_list[0]) or address_list[-1] > 32:
        print("Error2")
        return False
    return True

# raw_address = "192.168.1.15/24"
# # raw_address = "192/168"
# print(validate_address(raw_address))

# 1


def get_ip_from_raw_address(raw_address):
    """
    get IP - address and mask (raw_address)
    in the format: ###.###.###.###/##, e.g. 192.168.1.15/24;
    return IP adress
    """
    return raw_address.split("/")[0]

# 2


def get_network_address_from_raw_address(raw_address):
    """
    get IP - address and mask (raw_address)
    in the format: ###.###.###.###/##, e.g. 192.168.1.15/24;
    return network addresses
    """
    ip = get_ip_from_raw_address(raw_address)
    binary_ip = ''.join([bin(int(x)+256)[3:] for x in ip.split('.')])

    prefix = int(raw_address.split("/")[-1])
    mask = [0, 0, 0, 0]
    
    for i in range(prefix):
        mask[i // 8] += 1 << (7 - i % 8)

    binary_mask = ''.join([bin(int(x)+256)[3:] for x in mask])

    network = int(''.join([str(int(binary_ip[x])&int(binary_mask[x])) for x in range(len(binary_ip))]),2)


    return network
raw_address = "192.168.1.15/24"
print(get_network_address_from_raw_address(raw_address))


# 3


def get_broadcast_address_from_raw_address(raw_address):
    """
    get IP - address and mask (raw_address)
    in the format: ###.###.###.###/##, e.g. 192.168.1.15/24;
    return broadcast network address
    """
    pass

# 4


def get_binary_mask_from_raw_address(raw_address):
    """
    get IP - address and mask (raw_address)
    in the format: ###.###.###.###/##, e.g. 192.168.1.15/24;
    return subnet mask in binary form
    """
    pass

# 5


def get_first_usable_ip_address_from_raw_address(raw_address):
    """
    get IP - address and mask (raw_address)
    in the format: ###.###.###.###/##, e.g. 192.168.1.15/24;
    return the first possible node address in this network
    """
    pass

# 6


def get_penultimate_usable_ip_address_from_raw_address(raw_address):
    """
    get IP - address and mask (raw_address)
    in the format: ###.###.###.###/##, e.g. 192.168.1.15/24;
    return the penultimate possible node address in this network
    """
    pass

# 7


def get_number_of_usable_hosts_from_raw_address(raw_address):
    """
    get IP - address and mask (raw_address)
    in the format: ###.###.###.###/##, e.g. 192.168.1.15/24;
    return the total number of possible addresses for allocation (use)
    of nodes in this network
    """
    pass

# 8


def get_ip_class_from_raw_address(raw_address):
    """
    get IP - address and mask (raw_address)
    in the format: ###.###.###.###/##, e.g. 192.168.1.15/24;
    return network class (A, B, C, D, E)
    """
    pass

# 9


def check_private_ip_address_from_raw_address(raw_address):
    """
    get IP - address and mask (raw_address)
    in the format: ###.###.###.###/##, e.g. 192.168.1.15/24;
    return whether the address belongs
    to the space of private networks (True / False)
    """
    pass
