
import  pika


class conection_:
    def __init__(self, connectionInfo):
        try:
            print("Connecting")

            credentials = pika.PlainCredentials(connectionInfo.getUserName(), connectionInfo.getPassword())
            parameters = pika.ConnectionParameters(connectionInfo.getIP(),
                                                   connectionInfo.getPort(),
                                                   connectionInfo.getvHsot(),
                                                   credentials)

            connection = pika.BlockingConnection(parameters)
            self.channel = connection.channel()

        except Exception as ex :
            print("Connection failed")
            print(str(ex))
        else:
            print("Connection succeed")




    def getChannel(self):
        return  self.channel


    def colse(self):
        self.connection.close()
