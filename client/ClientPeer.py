from Message import Message
from PrivateMessage import PrivateMessage
import pickle
import threading


class ClientPeer(threading.Thread):

    def __init__(self, numeUtilizator, client, message='', recipient=''):

        threading.Thread.__init__(self)
        self.numeUtilizator = numeUtilizator
        self.message = message
        self.client = client
        self.Header = 1024
        self.recipient = recipient

# MUST RECEIVE MESSAGES FROM THE SERVER

    def run(self):
        print("[STARTING THREAD] ClientPeer thread started")

        msg = self.sendMessage(self.message, self.recipient)
        self.client.send(msg)

        if self.message == '':
            print("[THREAD STOPPING] ClientPeer thread has been ended!")
            return 0

        self.receiveMessage()
        print("[THREAD STOPPING] ClientPeer thread has been ended!")

    def sendMessage(self, message='', recipient=''):

        while message != '' and message:

            m = Message(self.numeUtilizator, message)
            p = PrivateMessage(recipient, self.numeUtilizator, message)

            if recipient == '':
                msg = pickle.dumps(m)
                return msg

            else:
                msg = pickle.dumps(p)
                return msg

        if message == '':
            msg = pickle.dumps('/name:' + ' ' + str(self.numeUtilizator))
            return msg

    def receiveMessage(self):

        connected = True

        while connected:

            message = b''
            try:

                print("A LUAT CONN SI ADDR")
                message = self.client.recv(self.Header)
                print("A luat mesajul")
                connected = False

            except:
                print("BREAK")
                break

            print("A trecut de blocul try")
            if message != '':
                msg = pickle.loads(message)
                print(msg)


