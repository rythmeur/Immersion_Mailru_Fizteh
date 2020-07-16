import socket, time

class ClientError (Exception):
    # # Constructor or Initializer
    def __init__(self, value):
        self.value = value
        # __str__ is to print() the value
    def __str__(self):
        return ("От сервера получено " + repr(self.value))

class Client:

    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout_client = timeout
        # НАДО СДЕЛАТЬ Соединение с сервером устанавливается при создании экземпляра класса Client  и не должно разрываться между запросами.
        self.sock = socket.create_connection((self.ip, self.port), self.timeout_client)
        # #set socket read timeout
        # self.sock.settimeout(1)

    def put(self, metrika_name, put_dannyie, timestamp = None):
        if timestamp == None:
            timestamp = int(time.time())
        # with socket.create_connection((self.ip, self.port),  self.timeout_client) as sock:
        #     # set socket read timeout
        #     # sock.settimeout(2)
        #     try:
        #         sock.sendall((f"put {metrika_name} {put_dannyie} {timestamp}\n").encode("utf8"))
        #         response = sock.recv(4096)
        #         print(response)
        #     except socket.timeout:
        #         print("send data timeout")
        #     except socket.error as ex:
        #         print("send data error:", ex)
        try:
            self.sock.sendall((f"put {metrika_name} {put_dannyie} {timestamp}\n").encode("utf8"))
            response = self.sock.recv(4096).decode("utf-8")
            response_splitted = response.split("\n")
            #print(response_splitted)
            if response_splitted[0] != "ok":
                raise ClientError (response_splitted[0])
        except socket.timeout:
            print("send data timeout")
        except socket.error as ex:
            print("send data error:", ex)



    def get(self, metrika_name_to_get):
        # with socket.create_connection((self.ip, self.port), self.timeout_client) as sock:
        #     # set socket read timeout
        #     # sock.settimeout(2)
        #     try:
        #         sock.sendall((f"get {metrika_name_to_get}\n").encode("utf8"))
        #         response = sock.recv(4096)
        #         print(response)
        #     except socket.timeout:
        #         print("send data timeout")
        #     except socket.error as ex:
        #         print("send data error:", ex)
        dict_with_metrika ={}
        try:
            self.sock.sendall((f"get {metrika_name_to_get}\n").encode("utf8"))
            response = self.sock.recv(4096).decode("utf-8")

            if response == "ok\n\n":
                return dict_with_metrika

            response_splitted = response.split("\n")
            # print(response_splitted)
            if response_splitted[0] != "ok" or (response[-2:-1]+response[-1]) != "\n\n":
                raise ClientError (response_splitted[0])

            for d in response_splitted[1:-2]:
                dannie = d.split(" ")
                if len(dannie) == 3:
                    if dannie[0] not in dict_with_metrika.keys():
                        dict_with_metrika[dannie[0]] = [(int(dannie[2]),float(dannie[1]))]
                    else:
                        dict_with_metrika[dannie[0]].append((int(dannie[2]),float(dannie[1])))
                        dict_with_metrika[dannie[0]].sort()
                else:
                    raise ClientError(d)




        except socket.timeout:
            print("send data timeout")
        except socket.error as ex:
            print("send data error:", ex)

        return dict_with_metrika


if __name__ == "__main__":
    client = Client("127.0.0.1", 8888, timeout=2)
    #
    # client.put("palm.cpu", 0.5, timestamp=1150864247)
    #
    # client.put("palm.cpu", 2.0, timestamp=1150864248)
    #
    # client.put("palm.cpu", 0.5, timestamp=1150864248)
    #
    # client.put("eardrum.cpu", 3, timestamp=1150864250)
    #
    # client.put("eardrum.cpu", 4, timestamp=1150864251)
    #
    # client.put("eardrum.memory", 4200000)
    #
    print(client.get("*"))
    # print(client.get("palm.cpu"))
