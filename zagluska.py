from twisted.internet import protocol, reactor


class Twist(protocol.Protocol):
    # Событие connectionMade срабатывает при соединении
    def __init__(self):
        pass

    def connectionMade(self):
        print('connection success!')

    # Событие dataReceived - получение и отправление данных
    def dataReceived(self, data):
        print(data)
        # transport.write - отправка сообщения
        self.transport.write(data)
        # print(s)

    # Событие connectionLost срабатывает при разрыве соединения с клиентом
    def connectionLost(self, reason):
        print('Connection lost!')

if __name__=="__main__":
    factory = protocol.Factory()
    factory.protocol = Twist
    print('wait...')
    reactor.listenTCP(777, factory)
    reactor.run()