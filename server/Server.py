from server.config.ServerConfig import ServerConfig
from server.ServerPeer import ServerPeer
import socket
import threading


class Server:

    def __init__(self, MAX_CLIENTS, TCP_PORT):

        self.MAX_CLIENTS = MAX_CLIENTS
        self.TCP_PORT = TCP_PORT

        self.IP = socket.gethostbyname(socket.gethostname())
        ADDR = (self.IP, self.TCP_PORT)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)
        self.users = []

    def listen(self):

        self.server.listen(self.MAX_CLIENTS)
        print(f"[LISTENING] Server is listening on {self.IP}")

        while True:

            conn, addr = self.server.accept()

            if conn and addr:

                sp_thread = ServerPeer(self, conn, addr)
                sp_thread.start()
                print(f"[ACTIVE_CONNECTIONS] {threading.activeCount() - 1}")

    def removeClient(self):
        pass


if __name__ == "__main__":

    sc = ServerConfig()
    s = Server(int(sc.getMaxClients()), int(sc.getTcpPort()))
    print("[STARTING SERVER] server is starting...")
    s.listen()


