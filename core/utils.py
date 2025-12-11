def get_valid_ip():
    valid_ip = False
    while not valid_ip:
        ip_address = input("Enter an ip address:")
        validate_ip = validate_ip_address(ip_address)
        if validate_ip:
            valid_ip = True
        else:
            print("Please enter a valid IP address")
    return ip_address

def validate_ip_address(ip_address):
    sum_octets = check_4_octets(ip_address)
    valid_range = check_range_octet(ip_address)
    if sum_octets and valid_range:
        return True
    return False

def check_4_octets(ip_address):
    ip_address = ip_address.split(".")
    if len(ip_address) != 4:
        return False
    return True

def check_range_octet(ip_address):
    ip_address = ip_address.split(".")
    for octet in ip_address:
        if int(octet) < 0 or int(octet) > 255:
            return False
    return True

def get_valid_mask():
    valid_mask = False
    while not valid_mask:
        mask = input("Enter network mask:")
        bin_mask = change_dec_mask_to_bin(mask)
        valid_mask = validate_mask(bin_mask)
        if not valid_mask:
            print("Please enter a valid mask")
    return mask

def change_dec_mask_to_bin(mask):
    mask = mask.split(".")
    bin_mask = []
    for octet in mask:
        bin_octet = dec_to_bin(int(octet))
        bin_mask.append(str(bin_octet))
    bin_mask = "".join(bin_mask)
    return bin_mask

def dec_to_bin(dec_num, max_len =8):
    bin_num = ""
    while max_len > 0:
        square = 2 ** (max_len -1)
        if dec_num >= square:
            bin_num += "1"
            dec_num -= square
        else:
            bin_num += "0"
        max_len -= 1
    return bin_num

def validate_mask(mask):
    length_mask = validate_len_mask(mask)
    sequence = validate_sequence(mask)
    only_ones_zeroes = validate_only_ones_zeroes(mask)
    all_once_or_zeroes = validate_all_once_or_zeroes(mask)
    if length_mask and sequence and only_ones_zeroes and all_once_or_zeroes:
        return True
    return False

def validate_sequence(mask):
    if "01" in mask:
        return False
    return True

def validate_only_ones_zeroes(mask):
    for i in range(len(mask)):
        if mask[i] != "1" and mask[i] != "0":
            return False
    return True

def validate_len_mask(mask, length=32):
    if len(mask) == length:
        return True
    return False

def validate_all_once_or_zeroes(mask):
    if mask[0] == "0" or mask[-1] == "1":
        return False
    return True

def get_network_address(ip, mask, bin=False):
    bin_ip = dot_dec_to_bin(ip)
    bin_mask = dot_dec_to_bin(mask)
    length = 32
    cut_index = bin_mask.find("0")
    if cut_index != -1:
        bin_network_prefix = bin_ip[:cut_index]
        dec_network_prefix = binary_to_dot_decimal(bin_network_prefix)
    else:
        bin_network_prefix = 0
        dec_network_prefix = 0
    if bin:
        return bin_network_prefix
    return dec_network_prefix

def dot_dec_to_bin(ip_address):
    octets = ip_address.split('.')
    binary_ip = ""
    for octet in octets:
        decimal_octet = int(octet)
        binary_ip += dec_to_bin(decimal_octet, 8)
    return binary_ip

def binary_to_dot_decimal(binary_string: str):
    octets = []
    for i in range(0, 32, 8):
        octet_binary = binary_string[i:i+8]
        octet_decimal = binary_to_decimal(octet_binary)
        octets.append(str(octet_decimal))
        
    return ".".join(octets)

def binary_to_decimal(binary_string: str):
    decimal_val = 0
    n = len(binary_string)
    for i, bit in enumerate(binary_string):
        if bit == '1':
            power = n - 1 - i
            decimal_val += (2 ** power)
    return decimal_val

def get_broadcast_address(ip, mask):
    bin_mask = dot_dec_to_bin(mask)
    length = 32
    cut_index =  bin_mask.find('0')
    if cut_index != -1:
        host_bits = length - cut_index
    else:
        host_bits = 0 
    network_prefix = get_network_address(ip, mask, bin=True)
    host_suffix_one = '1' * host_bits
    broadcast_binary = network_prefix + host_suffix_one
    broadcast_dec = binary_to_dot_decimal(broadcast_binary)
    return broadcast_dec

def get_amount_hosts(ip, mask):
    bin_mask = dot_dec_to_bin(mask)
    length = 32
    cut_index =  bin_mask.find('0')
    if cut_index != -1:
        host_bits = length - cut_index
    else:
        host_bits = 0 
    if host_bits <= 1:
        hosts = 0
    elif host_bits < 8:
        hosts = (2 ** host_bits) - 2
    elif host_bits < 16:
        third_octet = host_bits - 8
        hosts = ((2 ** third_octet) * 255) - 2
    elif host_bits < 24:
        second_octet = host_bits - 16
        hosts = ((2 ** second_octet) * (255 ** 2)) - 2
    else:
        first_octet = host_bits - 24
        hosts = ((2 ** first_octet) * (255 ** 3)) - 2
    return hosts

def write_to_file(data, ip):
    with open(f"subnet_info_{ip}_325291052.txt", "a") as f:
        for line in data:
            f.write(line)


def check_type_class(mask):
    pass
