import sys
from PyQt5.QtWidgets import QApplication

from client import Greeter,EchoClientFactory
from twisted.internet import reactor, threads
from Windows import Windows,profil

class ModelView:
    g = Greeter()
    z = EchoClientFactory(g)


    def aSillyBlockingMethodOne(x):
        import time
        time.sleep(1)
        print(x)

    def aSillyBlockingMethodTwo(x):

        while True:
            if (ModelView.g.flag == 0):
                import time
                time.sleep(1)
                app = QApplication(sys.argv)
                w = Windows()
                w.show()
                sys.exit(app.exec_())


                # ModelView.g.sendData()
    #





    def aSillyBlockingMethodThree(*args,**kwargs):
        app = QApplication(sys.argv)
        w = profil()
        w.show()

        app.exec_()










    @staticmethod
    def auntification(name,pasword):
        ModelView.g.Name =name
        ModelView.g.Password=pasword

    @staticmethod
    def initial():
        ModelView.g.Name="df"
        ModelView.g.Password="123"
        z = EchoClientFactory(ModelView.g)
        commands = [(ModelView.aSillyBlockingMethodOne, ["Calling First"], {})]
        commands.append((ModelView.aSillyBlockingMethodTwo, ["And the second"], {}))
        # commands.append((ModelView.aSillyBlockingMethodThree, ["And the Three"], {}))
        threads.callMultipleInThread(commands)
        #threads.deferToThread(ModelView.aSillyBlockingMethodThree,1)
        # reactor.callFromThread(ModelView.aSillyBlockingMethodThree, 1)

        reactor.callFromThread(ModelView.aSillyBlockingMethodThree,1)
        reactor.connectTCP("localhost", 777, ModelView.z)
        reactor.run()



