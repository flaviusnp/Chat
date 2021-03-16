from server.exceptions import InvalidFormatException
from server.exceptions import UnknownKeyException
from server.exceptions import MissingKeyException

class ServerConfig:

    __slots__ = {'name', 'MAX_CLIENTS', 'TCP_PORT'}

    # fisierul de configurare citit
    def __init__(self, name=r'C:\Users\flavius.negrea\PycharmProjects\LabPOO\server.conf.txt'):

        object.__setattr__(self, 'name', name)

        with open(self.name) as openfileobject:
            for line in openfileobject:

                try:

                    if "MAX_CLIENTS=" in line:
                        object.__setattr__(self, 'MAX_CLIENTS', line[(line.index("MAX_CLIENTS=")+12):])

                    elif "TCP_PORT=" in line:
                        object.__setattr__(self, 'TCP_PORT', line[(line.index("TCP_PORT=")+9):])

                except IOError:
                    print("Something went wrong")
                except InvalidFormatException:
                    print("Something went wrong")
                except UnknownKeyException:
                    print("Something went wrong")
                except MissingKeyException:
                    print("Something went wrong")

    def __setattr__(self, *args):
        raise AttributeError("Attributes of ServerConfig cannot be changed")

    def __delattr__(self, *args):
        raise AttributeError("Attributes of ServerConfig cannot be deleted")

    def getTcpPort(self):
        return self.TCP_PORT
    
    def getMaxClients(self):
        return self.MAX_CLIENTS




