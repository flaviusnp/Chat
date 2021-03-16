import pickle

class ServerPeer:

    def __init__(self, server):
        self.server = server
        self.HEADER = 64

    def run(self, conn, addr):

        print(f"[NEW_CONNECTION] {addr} connected.")

        full_message = b''
        connected = True
        while connected:
            message = conn.recv(self.HEADER)
            if len(message) <= 0:
                break
            full_message += message

        if len(full_message) > 0:
            
            msg = pickle.loads(full_message)
            print(msg)
            conn.close()
