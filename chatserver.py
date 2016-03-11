from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor


class IphoneChat(Protocol):
    """
    IphoneChat extends Twisted Protocol, contains methods to handle client connections.
    """

    def connectionMade(self):
        #self.transport.write("""connected""")
        self.factory.clients.append(self)
        print("clients are ", self.factory.clients)

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def dataReceived(self, data):
        """
        Decodes data bytes to string and parses into command and content

        :param data: bytes e.g. b'iam:joe\r\n'
        data format uses a colon as the separator
        <command>:<content>
        Decoded string e.g. 'iam:joe' or 'msg:hello there'
        """
        # print("data is ", data)
        # print("data.__class__ is ", data.__class__)

        # convert bytes to string
        data_str = data.decode('utf-8')
        a = data_str.split(':')
        if len(a) > 1:
            command = a[0]
            content = a[1]

            msg = ""
            if command == "iam":
                self.name = content
                msg = self.name + " has joined"

            elif command == "msg":
                msg = self.name + ": " + content

            print(msg)

            for c in self.factory.clients:
                c.message(msg)

    def message(self, message):
        """
        Send message to all connected clients

        Appends newline \n to indicate end of message
        :param message: string message to send
        """

        message_with_newline = message + '\n'
        # transport.write needs a byte string, not a unicode string
        # https://twistedmatrix.com/trac/ticket/6422
        # convert string to bytes
        message_bytes = message_with_newline.encode('utf-8')
        self.transport.write(message_bytes)


factory = Factory()
factory.protocol = IphoneChat

# clients model object stores each connected client.
# Each client is an IphoneChat instance, and is assigned its own socket.
factory.clients = []

reactor.listenTCP(80, factory)
print("Iphone Chat server started")
reactor.run()

