#!/usr/bin/python3

import encoder
import decoder
import arg_parser

if __name__ == "__main__":
    args = arg_parser.parse_args()

    if args.transmit:
        encoder.encode(args)
    else:
        decoder.decode(args)

