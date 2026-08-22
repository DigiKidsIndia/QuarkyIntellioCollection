import socket

# Configuration
TARGET_IP = "192.168.29.24"
TARGET_PORT = 5006
# The extracted data payload from the capture
PAYLOAD = "frame/2/202/8/1"

def send_udp_payload():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Encode string to bytes
    sock.sendto(PAYLOAD.encode('utf-8'), (TARGET_IP, TARGET_PORT))
    print(f"Payload sent to {TARGET_IP}:{TARGET_PORT}")

if __name__ == "__main__":
    send_udp_payload()
    
    
 