from scapy.all import sniff
from scapy.layers.inet import *
from argparse import Namespace

ttl2_message = ""
ttl8_message = ""
reserved_message = ""


def print_ttl8():
    true_message = ""
    for c in range(len(ttl8_message)):
        true_message += ttl8_message[c]

    print('Message in ttl8:', true_message)


def print_ttl2():
    print('Message in ttl2: ', end='')
    for i in range(0, len(ttl2_message), 8):
        # print(int(ttl2_message[i:i+8], base=2))
        print(chr(int(ttl2_message[i:i + 8], 2)), end='')
    print()


def print_reserved():
    print('Message in reserved: ', end='')
    for i in range(0, len(reserved_message), 8):
        print(chr(int(reserved_message[i:i+8], 2)), end='')
    print()


def decode(args: Namespace):

    def process_packet(packet):
        global ttl2_message
        global ttl8_message
        global reserved_message
        if args.verbose:
            print('Received packet')
            print('==========')
            print('ttl:      ' + str(packet.ttl) + '\t- ' + bin(packet.ttl)[2:].zfill(8) + ' : ' + chr(packet.ttl))
            print('reserved: ' + str(packet.reserved) + '\t- ' + bin(packet.reserved)[2:].zfill(8) + ' : ' + chr(packet.reserved))
            print('==========')
        if IP in packet:
            ttl2_message += bin(packet[IP].ttl)[2:].zfill(8)[:2]
            ttl8_message += chr(packet[IP].ttl)
            reserved_message += bin(packet.reserved)[2:].zfill(3)[-3:]

    try:
        if args.interface:
            sniff(prn=process_packet, iface=args.interface, filter=f'port {args.port}', store=False)
        else:
            sniff(prn=process_packet, store=False, filter=f'port {args.port}')
    except KeyboardInterrupt:
        print_ttl8()
        print_ttl2()
        print_reserved()
        exit(0)

    print_ttl8()
    print_ttl2()
    print_reserved()
