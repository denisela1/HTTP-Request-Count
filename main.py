from collections import Counter
import re


def read_file():
    data = open("data_file.txt").readlines()
    data_list = []
    for item in data:
        data_list.append((item.strip()).split(" "))
    return data_list


def count_host():
    hosts = []
    host_list = read_file()
    for i in host_list:
        hosts.append(i[0])
    domains = []
    for i in hosts:
        try:
            domains.append(re.match('.*com', i).group(0))
        except AttributeError:
            pass
    c = Counter(domains)
    for values,keys in c.items():
        print(values, keys)


if __name__ == '__main__':
    count_host()

