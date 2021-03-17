import socket
from client.ClientPeer import ClientPeer

class TextClient:

    def __init__(self):
        self.HEADER = 1024
        self.PORT = 9000
        self.SERVER = '192.168.56.1'
        self.ADDR = (self.SERVER, self.PORT)


if __name__ == "__main__":

    tc = TextClient()
    name = input("Introduceti numele de utilizator:\n")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(tc.ADDR)

    while True:


        msg = input("Trimite mesaj:")

        if msg is not None:

            cp = ClientPeer(name, msg, client)
            cp.start()
            cp.join()
            msg = None

        elif msg == '/w':
            break



