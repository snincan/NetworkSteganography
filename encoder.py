from scapy.sendrecv import send
from scapy.layers.inet import *
from argparse import Namespace


def use_ttl8(data: str, args: Namespace):
    for c in data:
        packet = IP(dst=args.ip, ttl=0) / TCP(dport=args.port)
        packet.ttl = ord(c)
        if args.verbose:
            print(f'Sending \'{c}\' - {packet.ttl}')
        send(packet)


def use_reserved(data: str, args: Namespace):
    bin_data = ''.join([bin(ord(c))[2:].zfill(8) for c in data])
    for i in range(0, len(bin_data), 3):
        packet = IP(dst=args.ip) / TCP(dport=args.port)
        packet.reserved = int(bin_data[i:i+3].ljust(3, '0'), base=2)
        if args.verbose:
            print(f'Sending \'{chr(int(bin_data[i:i+3], 2))}\' - {bin(packet.reserved)[2:].zfill(3)}')
        send(packet)


def use_ttl2(data: str, args: Namespace):
    for c in data:
        for i in range(0, 4):
            packet = IP(dst=args.ip) / TCP(dport=args.port)
            packet.ttl = int(bin(ord(c))[2:].zfill(8)[i*2:i*2+2] + '111111', base=2)  # dear god
            if args.verbose:
                print(f'Sending \'{c}\' - {bin(packet.ttl)[2:].zfill(8)}')
            send(packet)


def encode(args: Namespace):
    data = args.data

    match args.optimize:
        case 0:
            use_ttl8(data, args)
        case 1:
            use_reserved(data, args)
        case 2:
            use_ttl2(data, args)
