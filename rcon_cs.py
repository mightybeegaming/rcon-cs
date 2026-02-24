import socket
import sys
import re
import configparser

CS_CONFIG = configparser.ConfigParser()
CS_CONFIG.read("rcon_cs-config.ini")

SERVER_IP = CS_CONFIG.get("RCON", "IPAddress")
SERVER_PORT = CS_CONFIG.getint("RCON", "Port")
RCON_PASSWORD = CS_CONFIG.get("RCON", "Password")

def get_challenge(sock):
    packet = b"\xFF\xFF\xFF\xFFchallenge rcon\n"
    sock.sendto(packet, (SERVER_IP, SERVER_PORT))

    try:
        data, _ = sock.recvfrom(4096)
        text = data[4:].decode(errors="ignore")

        match = re.search(r"challenge rcon (\d+)", text)
        if match:
            return match.group(1)
    except socket.timeout:
        pass

    return None

def send_rcon(command):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)

    challenge = get_challenge(sock)
    if not challenge:
        print("Failed to get RCON challenge")
        return

    packet = (
        b"\xFF\xFF\xFF\xFFrcon "
        + challenge.encode()
        + b" "
        + RCON_PASSWORD.encode()
        + b" "
        + command.encode()
        + b"\n"
    )

    sock.sendto(packet, (SERVER_IP, SERVER_PORT))

    try:
        while True:
            data, _ = sock.recvfrom(4096)
            print(data[4:].decode(errors="ignore"))
    except socket.timeout:
        pass

    sock.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rcon_cs.py <command>")
        sys.exit(1)

    send_rcon(" ".join(sys.argv[1:]))
