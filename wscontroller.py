import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import uinput

keys = [
    uinput.KEY_UP,          #0 (U)
    uinput.KEY_DOWN,        #1 (D)
    uinput.KEY_LEFT,        #2 (L)
    uinput.KEY_RIGHT,       #3 (R)
    uinput.KEY_1,           #4 (START P1)
    uinput.KEY_A,           #5 (SELECT)
    uinput.KEY_LEFTCTRL,    #6 (A)
    uinput.KEY_LEFTALT,     #7 (B)
    uinput.KEY_5,           #8 (COIN)
    ]
device = uinput.Device(keys)

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
      
    def on_message(self, message):
#        print 'message received:  %s' % message
        ac=message[:1]
        kp=keys[int(message[1:])]
        if ac=='.':
            device.emit_click(kp)
        else:
            ud=0 if ac=='-' else 1
            device.emit(kp,ud)
 
    def on_close(self):
        print 'connection closed'
 
    def check_origin(self, origin):
        return True
 
application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print '*** Websocket Server Started at %s***' % myIP
    tornado.ioloop.IOLoop.instance().start()

