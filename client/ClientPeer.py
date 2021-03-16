from Message import Message
from PrivateMessage import PrivateMessage
import pickle


class ClientPeer():

    def __init__(self, numeUtilizator):

        self.numeUtilizator = numeUtilizator

    def sendMessage(self, message, recipient=None):

        m = Message(self.numeUtilizator, message)

        p = PrivateMessage(recipient, self.numeUtilizator, message)

        if recipient is None:

            mesaj = pickle.dumps(m)
            print(mesaj)
            print("Mesaj in ClientPeer")
            return mesaj

        else:
            mesaj = pickle.dumps(p)
            print(mesaj)
            print("Mesaj privat in ClientPeer")
            return mesaj
