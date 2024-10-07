from scapy.all import *

def create_packet(destination_ip):
    """Create an ICMP packet to send to the specified destina>
    packet = IP(dst=destination_ip) / ICMP()
    return packet

def send_packet(packet):
    """Send the created packet."""
    try:
        send(packet)
        print(f"Packet sent to {packet[IP].dst}")
    except Exception as e:
        print(f"Error sending packet: {e}")

def main():
    """Main function to run the packet injection tool."""
    print("Packet Injection Tool")
    destination_ip = input("Enter the destination IP address:>

    # Create the packet
    packet = create_packet(destination_ip)

    # Send the packet
    send_packet(packet)

if __name__ == "__main__":
    main()