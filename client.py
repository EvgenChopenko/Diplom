import pickle

from twisted.internet import reactor, threads, defer, task, protocol
from twisted.internet.protocol import Factory, Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint


class Greeter(Protocol):
    def __init__(self):
        super().__init__()
        self.flag =1
        self.__name=""
        self.__password=""
        self.__msg="GET"
        self.__out_msg=""
    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self,name):
        self.__name = name

    @property
    def Password(self):
        return  self.__password
    @Password.setter
    def Password(self,possword):
        self.__password=possword

    @property
    def MSG(self):
        return self.__msg
    @MSG.setter
    def MSG(self,value):
        self.__msg=value

    @property
    def OUTMSG(self):
        return self.__out_msg

    @OUTMSG.setter
    def OUTMSG(self, valeu):
        self.__out_msg = valeu

    def sendData(self):
        d = {'name': self.__name, 'password': self.__password, 'msg':self.__msg}
        pd = pickle.dumps(d, protocol=0)
        pd.decode()
        if self.flag==1:
            self.flag = 0
            print("sending %s...." % self.__msg)
            self.transport.write(pd)

        else:
            self.transport.loseConnection()



    def connectionMade(self):

        self.sendData()

    def dataReceived(self, data):


        d=data.decode()
        self.__out_msg=d
        print(d)








class EchoClientFactory(ClientFactory):
    def __init__(self,Greeter):
        super().__init__()
        self.Gre =Greeter

    def startedConnecting(self, connector):
        print('Started to connect.')

    def buildProtocol(self, addr):
        print('Connected.')
        return self.Gre

    def clientConnectionLost(self, connector, reason):  ## События отключения и переподключения
        print('Lost connection.  Reason:', reason)
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)


"""
if __name__=="__main__":

    g = Greeter()
    g.Name="vasy"
    g.Password="asdfsa"
    z=EchoClientFactory(g)
    from twisted.internet import reactor

    def aSillyBlockingMethodOne(x):
        import time
        time.sleep(2)
        print (x)

    def aSillyBlockingMethodTwo(x):
        while True:
            if (g.flag == 0):
                g.sendData()


# run both methods sequentially in a thread
    commands = [(aSillyBlockingMethodOne, ["Calling First"], {})]
    commands.append((aSillyBlockingMethodTwo, ["And the second"], {}))
    threads.callMultipleInThread(commands)






    reactor.connectTCP("localhost", 777, z)

    reactor.run()
"""