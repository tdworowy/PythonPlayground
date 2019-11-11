# https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pair.html
import _thread

import zmq


def server(frm):
    port = "5556"
    context = zmq.Context()
    socket = context.socket(5)
    socket.bind("tcp://*:%s" % port)

    while True:
        socket.send_string("Server message from %s" % frm)
        msg = socket.recv().decode("utf-8")
        print(msg)


def client(frm):
    port = "5556"
    context = zmq.Context()
    socket = context.socket(5)
    socket.connect("tcp://localhost:%s" % port)

    while True:
        msg = socket.recv().decode("utf-8")
        socket.send_string("client message from %s" % frm)
        print(msg)


if __name__ == "__main__":
    _thread.start_new_thread(server, ("Thread1",))
    _thread.start_new_thread(client, ("Thread2",))
    _thread.start_new_thread(client, ("Thread3",))

    while 1:
        pass
