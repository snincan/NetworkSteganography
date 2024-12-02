import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='Network steganography transmitter', description='')
    parser.add_argument('-t', '--transmit', action='store_true', help='Assume the role of a transmitter - you are sending a message')
    parser.add_argument('-r', '--receive', action='store_true', help='Assume the role of a receiver - you want to receive a message')
    parser.add_argument('-i', '--ip', type=str, help='IP to send data to')
    parser.add_argument('-p', '--port', type=int, help='Port to open/send data to', required=True)
    parser.add_argument('-I', '--interface', type=str, help='Interface to listen on')
    parser.add_argument('-d', '--data', type=str, help='Data to send')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
    parser.add_argument('-O', '--optimize', type=int, default=0, help='Level of optimization to use')
    args = parser.parse_args()
    if args.transmit and args.receive:
        parser.error('You cannot be both a transmitter and a receiver')
        exit(1)
    if not args.transmit and not args.receive:
        parser.error('You have to be either a transmitter or a receiver')
        exit(1)
    if args.transmit:
        if not args.ip:
            parser.error('You have to specify an IP to send data to')
            exit(1)
        if not args.data:
            parser.error('You have to specify data to send')
            exit(1)
    if args.receive:
        pass

    return args

