from channels.generic.websocket import WebsocketConsumer
import socket,struct,os
class ChatConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.port=''
        self.max_x=''
        self.max_y=''


    def connect(self):
        self.accept()


    def disconnect(self, close_code):
        print("minitouch 离开")
        self.close()



    def receive(self, text_data):
        import json
        res=json.loads(text_data)
        operation = res['operation']

        if operation=='link':
            if res['device']=="emulator-5554":
                self.port=1111
                print(text_data,"5554")
            else:
                self.port=1112
                print(text_data, "5556")


            c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c.connect(("localhost", self.port))
            res=c.recv(1024).decode('utf-8')
            print(res,"返回值")
            _, contacts, self.max_x, self.max_y, pressure = (res).split("\n")[1].split(' ')

        elif operation=='input':
            content=res['key']
            cmd="adb shell input text  {}".format(content)
            os.system(cmd)

        else:
                c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                c.connect(("localhost", self.port))
                x_P = res['xP']
                y_p = res['yP']
                x = int(int(x_P)*(int(self.max_x) / 377))
                y = int(int(y_p)*(int(self.max_y) / 724))

                f = "d 0 {} {} 50\nc\nu 0\nc\n ".format(x, y)
                if operation=="down":
                    f="d 0 {} {} 50\nc\n ".format( x,y)

                elif operation=="up":
                    f="u 0\nc\n"

                else:
                    f="m 0 {} {} 50\nc\n ".format( x,y)
                print(f)
                f = (f.encode('utf-8'))

                c.sendall(f)
                c.close()




