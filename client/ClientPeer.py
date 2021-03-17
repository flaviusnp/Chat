from Message import Message
from PrivateMessage import PrivateMessage
import pickle
import threading


class ClientPeer(threading.Thread):

    def __init__(self, numeUtilizator, message, client, recipient=None):

        threading.Thread.__init__(self)
        self.numeUtilizator = numeUtilizator
        self.message = message
        self.client = client
        self.recipient = recipient

# MUST RECEIVE MESSAGES FROM THE SERVER

    def run(self):
        print("[STARTING THREAD] ClientPeer thread started")
        msg = self.sendMessage(self.message, self.recipient)
        self.client.send(msg)
        print("[THREAD STOPPING] ClientPeer thread has been ended!")

    def sendMessage(self, message, recipient=None):

        while message:

            m = Message(self.numeUtilizator, message)

            p = PrivateMessage(recipient, self.numeUtilizator, message)

            if recipient is None:

                msg = pickle.dumps(m)
                print(msg)
                print("Msg in ClientPeer")

                return msg

            else:
                msg = pickle.dumps(p)
                print(msg)
                print("Private msg in ClientPeer")

                return msg

