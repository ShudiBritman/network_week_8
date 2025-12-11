from core.utils import *
from core.output_string import *

def main():
    ip_address = get_valid_ip()
    subnet_mask = get_valid_mask()
    print(ip_address, subnet_mask)
    f_ip = format_input_ip(ip_address)
    f_subnet_mask = format_subnet_mask(subnet_mask)
    network_address = get_network_address(ip_address, subnet_mask)
    f_network_address = format_network_address(network_address)
    broadcast_address = get_broadcast_address(ip_address, subnet_mask)
    f_broadcast_address = format_broadcast_address(broadcast_address)
    num_hosts = get_amount_hosts(ip_address, subnet_mask)
    f_num_hosts = format_num_hosts(num_hosts)
    data = f_ip, f_subnet_mask, f_network_address, \
    f_broadcast_address, f_num_hosts
    write_to_file(data, ip_address)


if __name__ == "__main__":
    main()