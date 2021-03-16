from server.config.ServerConfig import ServerConfig
from server.ServerPeer import ServerPeer
import socket
import threading


class Server(ServerPeer):

    def __init__(self, outer_server):
        super().__init__(outer_server)

    def start(self, MAX_CLIENTS, outer_SERVER):

        server.listen(MAX_CLIENTS)
        print(f"[LISTENING] Server is listening on {outer_SERVER}")

        while True:

            conn, addr = server.accept()

            if conn and addr:
                thread = threading.Thread(target=ServerPeer.run, args=(self, conn, addr))
                thread.start()
                print(f"[ACTIVE_CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == "__main__":

    sc = ServerConfig()

    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, int(sc.getTcpPort()))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

    s = Server(server)

    print("[STARTING SERVER] server is starting...")
    s.start(int(sc.getMaxClients()), SERVER)


