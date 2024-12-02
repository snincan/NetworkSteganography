# NetworkSteganography

A proof of concept program for sending and receiving data hidden in the headers of internet protocols over a network.

# Installation

1. Have python 3 installed
2. Clone this repository
```
git clone https://github.com/snincan/NetworkSteganography.git
```
3. Install required libraries found in requirements.txt
```
pip install -r requirements.txt
```

# Usage

## Transmitter

The transmitter will keep sending packets until the entire message is sent, at which point the program terminates.

```
sudo ./NetworkSteganography.py -t -i 127.0.0.1 -p 1234 -O 2 -d "secret message"
```
```
-t (Assume the role of a transmitter)
-i [IP] (IP address to send packets to)
-p [Port] (The port to send packets on)
-O [0/1/2] (The level of optimisation to use)
-d [Data] (The data to hide in packets and send)
-v (Verbose mode)
```

## Receiver

The receiver will keep scanning for packets, until the user interrupts the program (CTRL+C). At this point, the program prints the messages found by scanning all hiding places for data implemented in the transmitter. It is then up to the user to determine which method was used.

```
sudo ./NetworkSteganography.py -r -p 1234 -I lo
```
```
-r (Assume the role of a receiver)
-p [Port] (The port to open for communication)
-I [Interface] (Network interface to scan packets on)
-v (Verbose mode)
```

# Disclaimer

This program is just a proof of concept and should not be used as a real network steganography method.
