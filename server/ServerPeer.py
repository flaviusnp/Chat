import pickle
import threading


class ServerPeer(threading.Thread):

    def __init__(self, server, conn, addr):
        threading.Thread.__init__(self)
        self.server = server
        self.HEADER = 1024
        self.conn = conn
        self.addr = addr

    def run(self):
        print("[STARTING THREAD] ServerPeer thread has started.")
        # Must read Message and PrivateMessage and send it to
        # other users/user
        self.receiveMessage(self.conn, self.addr)
        print("[STOPPING THREAD] ServerPeer thread has stopped.")

    def receiveMessage(self, conn, addr):

        users = []

        while addr:

            if addr not in users:
                users.append(addr)
                print(f"[NEW_CONNECTION] {addr} connected.")

            connected = True

            while connected:

                full_message = b''
                try:
                    message = conn.recv(self.HEADER)
                    if len(message) <= 0:
                        break
                    full_message += message

                except:
                    continue

                    # verify select()
                if full_message != '':
                    msg = pickle.loads(full_message)
                    print(msg)

            conn.close()
