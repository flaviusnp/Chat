from Message import Message

class PrivateMessage(Message):

    __slots__ = {'numeDestinatar'}

    def __init__(self, numeDestinatar, numeExpeditor, continut):

        self.numeDestinatar = numeDestinatar
        self.numeExpeditor = numeExpeditor
        self.continut = continut

        # This class can't be immutable because a socket function creates
        # an instance of this class without calling the constructor

        """
        super().__init__(numeExpeditor, continut)
        object.__setattr__(self, 'numeDestinatar', numeDestinatar)
        """

    def __str__(self):

        return "(priv) " + self.numeExpeditor + ': ' + self.continut

    """
    def __setattr__(self, *args):
        raise AttributeError("Attributes of PrivateMessage cannot be changed")

    def __delattr__(self, *args):
        raise AttributeError("Attributes of PrivateMessage cannot be deleted")
    """

    def getRecipient(self):
        return self.numeDestinatar





