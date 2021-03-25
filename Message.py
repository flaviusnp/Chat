class Message:

    __slots__ = {'numeExpeditor', 'continut'}

    def __init__(self, numeExpeditor, continut):

        self.numeExpeditor = numeExpeditor
        self.continut = continut

        # This class can't be immutable because a socket function creates
        # an instance of this class without calling the constructor
        """
        object.__setattr__(self, 'numeExpeditor', numeExpeditor)
        object.__setattr__(self, 'continut', continut)
        """

    def __str__(self):
        return self.numeExpeditor + ": " + self.continut

    def getSender(self):
        return self.numeExpeditor


"""
    def __setattr__(self, *args):
        raise AttributeError("Attributes of Message cannot be changed")

    def __delattr__(self, *args):
        raise AttributeError("Attributes of Message cannot be deleted")
"""
