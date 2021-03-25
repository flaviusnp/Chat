import pickle
import threading


class ServerPeer(threading.Thread):

    def __init__(self, serverObject, conn, addr):
        threading.Thread.__init__(self)
        self.HEADER = 1024
        self.serverObject = serverObject
        self.conn = conn
        self.addr = addr

    def run(self):
        print("[STARTING THREAD] ServerPeer thread has started.")
        # Must read Message and PrivateMessage and send it to
        # other users/user
        self.receiveMessage()
        print("[STOPPING THREAD] ServerPeer thread has stopped.")

    def receiveMessage(self):

        connected = True

        while self.addr and connected:

            message = b''
            try:
                message = self.conn.recv(self.HEADER)

            except:
                pass

            if message != '':

                msg = pickle.loads(message)

                if str(msg).split(' ')[0] == '/name:' and self.addr not in [user[0] for user in self.serverObject.users]:
                    user = str(msg).split(' ')[1]
                    self.serverObject.users.append((self.addr, self.conn, user))
                    print(self.serverObject.users)
                    print(f"[NEW_CONNECTION] {self.addr} connected.")
                    continue

                if msg == '/q':
                    connected = False
                    self.conn.close()

                if str(msg).split(' ')[0] == '(priv)':
                    string = ''.join(str(msg).split(' ')[1] + ' ' + ' '.join(str(msg).split(' ')[3:]))

                    recipient = str(msg).split(' ')[2]
                    conn_recipient = '0'

                    for user in self.serverObject.users:
                        if user[2] == recipient:

                            conn_recipient = user[1]
                            break

                    message = pickle.dumps(string)
                    if conn_recipient != '0':
                        print(string)
                        print(message)
                        conn_recipient.send(message)
                        print("Am trimis mesajul de la server")

                else:
                    print(msg)

    def getUsername(self, message):
        return message.getSender()
