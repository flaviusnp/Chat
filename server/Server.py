from server.config.ServerConfig import ServerConfig
from server.ServerPeer import ServerPeer
import socket
import threading


class Server():

    def __init__(self):
        pass

    def start(self, MAX_CLIENTS, outer_SERVER):

        server.listen(MAX_CLIENTS)
        print(f"[LISTENING] Server is listening on {outer_SERVER}")

        while True:

            conn, addr = server.accept()

            if conn and addr:

                sp_thread = ServerPeer(server, conn, addr)
                sp_thread.start()
                print(f"[ACTIVE_CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == "__main__":

    sc = ServerConfig()

    IP = socket.gethostbyname(socket.gethostname())
    ADDR = (IP, int(sc.getTcpPort()))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

    s = Server()

    print("[STARTING SERVER] server is starting...")
    s.start(int(sc.getMaxClients()), IP)


