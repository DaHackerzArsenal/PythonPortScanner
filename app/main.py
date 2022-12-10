#!/usr/bin/env python3

import socket
from connection_exceptions import NoIP


class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []
        self.ports = [1, 65535]

    def add_port(self, port):
        self.open_ports.append(port)

    def scan(self, port_range):
        for port in port_range:
            if self.is_open(port):
                self.add_port(port)

    def is_open(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((self.ip, port))
        s.close()
        return not bool(result)

    def write(self, filepath):
        with open(filepath, 'w') as file:
            file.write(repr(self))

    def __repr__(self):
        return f'Scanned: {self.open_ports}\n'

    def __str__(self):
        return self.ip


class Connection:
    def __init__(self):
        self.port_range = None
        self.ports = [1, 65535]
        self.ip = ''

    def connection_prompt(self):
        self.ip = input('IP: ')
        if not self.ip:
            raise NoIP('NoIPError: IP cannot be empty')

        print('Insert a port range 1-65535')
        for i in range(2):
            try:
                user_input = input(f'Port [{i}]: ')
                if not user_input:
                    break
                self.ports[i] = int(user_input)
            except TypeError:
                print('Only Integers Are Allowed')

        self.port_range = range(self.ports[0], self.ports[1])


def main():
    conn = Connection()
    conn.connection_prompt()
    scanner = Scanner(conn.ip)
    scanner.scan(conn.port_range)
    print(f'Open ports: {scanner.open_ports}')


if __name__ == '__main__':
    main()
