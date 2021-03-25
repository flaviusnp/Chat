import socket
from client.ClientPeer import ClientPeer
import threading
import pickle


class TextClient:

    def __init__(self):
        self.HEADER = 1024
        self.PORT = 9000
        self.SERVER = '192.168.56.1'
        self.ADDR = (self.SERVER, self.PORT)

    def take_input(self):

        cp = None

        while True:
            msg = input("Trimite mesaj:")
            message = msg.split(" ")

            if message[0] != '/w' and message[0] != '/q' and msg:
                cp = ClientPeer(name, client, msg)

            elif message[0] == '/w':
                cp = ClientPeer(name, client, " ".join(message[1:]), recipient=message[1])

            elif message[0] == '/q':
                cp = ClientPeer(name, client, msg)

            if cp is not None:

                cp.start()
                cp.join()


if __name__ == "__main__":

    tc = TextClient()
    name = input("Introduceti numele de utilizator:\n")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(tc.ADDR)

    cp_name = ClientPeer(name, client)
    cp_name.start()
    cp_name.join()

    input_thread = threading.Thread(target=tc.take_input())
    input_thread.start()

    while True:

        message_received = b''

        try:
            message_received = client.recv(1024)

        except:
            pass

        if message_received:
            msg_rcv = pickle.loads(message_received)
            print("SI LA FINALLLLLLLLLLLLLLL")
            print(msg_rcv)




