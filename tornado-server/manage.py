#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import py_eureka_client.eureka_client as eureka_client
from tornado.options import define, options
from time import sleep

define("port", default=3000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('username', 'Hello')
        self.write(username + ', Administrator User!')

    def post(self):
        username = self.get_argument('username', 'Hello')
        self.write(username + ', Administrator User!')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('username', 'Hello')
        self.write(username + ', Coisini User!')

    def post(self):
        username = self.get_argument('username', 'Hello')
        self.write(username + ', Coisini User!')


def main():
    tornado.options.parse_command_line()
    # 注册eureka服务
    eureka_client.init_registry_client(eureka_server="http://localhost:31091/eureka/,http://localhost:8761/eureka/",
                                       app_name="tornado-server",
                                       instance_port=3000)
    app = tornado.web.Application(handlers=[(r"/test", IndexHandler), (r"/main", MainHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()