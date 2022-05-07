class IP_list:
    def __init__(self, ip_addresses):
        self.ip_addresses = ip_addresses

    def reverse(self):
        ips_reverse = []
        for ip_address in self.ip_addresses:
            ip = ip_address.split(".")
            ip.reverse()
            ips_reverse.append(".".join(ip))
        return ips_reverse

    def first_null(self):
        ips_first_null = []
        for ip_address in self.ip_addresses:
            ip = ip_address.split(".")
            ip.pop(0)
            ips_first_null.append(".".join(ip))
        return ips_first_null

    def last_value(self):
        ips_last_value = []
        for ip_address in self.ip_addresses:
            ip = ip_address.split(".")
            ips_last_value.append(ip[-1])
        return ips_last_value


if __name__ == '__main__':
    proccess_input = IP_list(ip_addresses=['10.10.22.12', '20.23.52.10'])
    print(proccess_input.reverse())
    print(proccess_input.first_null())
    print(proccess_input.last_value())
