from channels.generic.websocket import WebsocketConsumer
import socket,struct
class ChatConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def connect(self):
        self.accept()


    def disconnect(self, close_code):
        print("minitouch 离开")
        self.close()


    def receive(self, text_data):
        import json
        res=json.loads(text_data)
        operation=res['operation']
        x_P=res['xP']
        y_p=res['yP']
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect(("localhost", 1111))
        # text_data=(text_data.split(','))
        # print(text_data,int(text_data[0]))
        # x = int(int(text_data[0])*(1080 / 377))
        # y = int(int(text_data[1])*(1920 / 724))

        x = int(int(x_P)*(19199 / 377))
        y = int(int(y_p)*(10799 / 724))

        # f = "d 0 {} {} 50\nc\nu 0\nc\n ".format(x, y)
        if operation=="down":
            f="d 0 {} {} 50\nc\n ".format( x,y)

        elif operation=="up":
            f="u 0\nc\n"

        else:
            f="m 0 {} {} 50\nc\n ".format( x,y)
        # print(f)
        f = (f.encode('utf-8'))

        self.__socket.sendall(f)
        self.__socket.close()




