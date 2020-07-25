# реализация сервера для тестирования метода get по заданию - Клиент для отправки метрик
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import asyncio

# Проблема - не обновлять коннекшн, не разрывать его и соотв. каждый раз не обнулять мою базу self.saved_data

class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.saved_data = {}

    def connection_made(self, transport): #protocol calls transport methods to send data, while the transport calls protocol methods to pass it data that has been received.
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername), "self.saved_data =", self.saved_data )
        self.transport = transport


    def data_received(self, data):

        message = data.decode()
        print('Data received: {!r}'.format(message))

        resp = self.process_data(message)

        print('Send: {!r}'.format(resp))
        self.transport.write(resp.encode())

        # print('Close the client socket')
        # self.transport.close()



    def process_data(self, message):


        # response = 'ok\npalm.cpu 10.5 4\neardrum.cpu 15.3 1501864259\npalm.cpu 11.00 1\npalm.cpu 13.5 3\npalm.cpu 1.5 2\n\n'


        if message[0:4] == "put " and message[-1] == "\n":
            print("start self.saved_data=", self.saved_data)
            status, payload = message.split(" ", 1)
            payload = payload.strip()
            put_msg = payload.split()
            print("status= ", status, "put_msg= ", put_msg)
            if len(put_msg) == 3:
                try:
                    a = float(put_msg[1] )
                    b = int(put_msg[2])
                except ValueError:
                    return "error\nwrong command\n\n"

                if put_msg[0] in self.saved_data:
                    self.saved_data [put_msg[0]][put_msg[2]] = put_msg[1]


                else:
                    self.saved_data [put_msg[0]] = {put_msg[2]:put_msg[1]}

                response = "ok\n\n"

            else:
                print("error!")
                response = "error\nwrong command\n\n"


        elif message[0:4] == "get " and message[-1] == "\n":
            print("get!")
            status, payload = message.split(" ", 1)
            get_msg = payload.strip()
            if get_msg in self.saved_data and (" " not in get_msg):
                response = "ok\n"
                print("self.saved_data[get_msg] =", self.saved_data[get_msg])
                for timestamp, value in self.saved_data[get_msg].items():
                    print("timestamp =", timestamp, "value =", value )
                    response = response + get_msg + " " + value + " " + timestamp + "\n"
                response = response + "\n"


            elif get_msg == "*":
                response = "ok\n"
                for key,val in self.saved_data.items():


                    for timestamp, value in val.items():
                        print("timestamp =", timestamp, "value =", value )
                        response = response + key + " " + value + " " + timestamp + "\n"
                response = response + "\n"

            elif " " not in get_msg and len(get_msg)>0:
                print("no such key!", get_msg, len(get_msg), type(get_msg) )
                response = "ok\n\n"
            else:
                print("error!")
                response = "error\nwrong command\n\n"


        else:
            print("error!")
            response = "error\nwrong command\n\n"


        print("finish self.saved_data=", self.saved_data)
        print("response", response)



        return response



def  run_server(host, port):
    loop = asyncio.get_event_loop()
    # Each client connection will create a new protocol instance
    coro = loop.create_server(ClientServerProtocol,host, port)
    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()




if __name__ == "__main__":
    run_server("127.0.0.1", 8888)
