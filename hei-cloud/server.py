import json
import time

class Server:
    
    def __init__(self):
        self.storage_limit = 0
        self.request_number_limit = 0
        self.free_storage = 0
        self.is_server_up = False
        self.list_file = []

    def server_start(self):
        self.is_server_up = True

    def server_down(self):
        self.is_server_up = False
    
    def is_up(self):
        return self.is_server_up

    def get_all_files(self):
        print(json.dumps(self.list_file))

if __name__ == '__main__':

    server = Server()

    server.server_start()
    print("Starting server ...")

    try:
        storage_limit = int(input("Enter storage limit (GB): "))
        server.storage_limit = storage_limit * 1000
        server.free_storage = storage_limit * 1000
        request_number_limit = int(input("Enter request number limit: "))
        server.request_number_limit = request_number_limit
        print("Now you can use our cloud")
        print("press Ctrl+C to stop server")

        while server.is_up():
            pass

    except KeyboardInterrupt:
        print("Stop server")
        server.server_down()
