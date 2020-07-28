import pika


class Connection_:
    def __init__(self, connection_info):
        try:
            print("Connecting")

            credentials = pika.PlainCredentials(connection_info.getUserName(), connection_info.pssword)
            parameters = pika.ConnectionParameters(connection_info.ip,
                                                   connection_info.port,
                                                   connection_info.host,
                                                   credentials)

            connection = pika.BlockingConnection(parameters)
            self.channel = connection.channel()

        except Exception as ex:
            print("Connection failed")
            print(str(ex))
        else:
            print("Connection succeed")

    def get_channel(self):
        return self.channel

    def close(self):
        self.connection.close()
