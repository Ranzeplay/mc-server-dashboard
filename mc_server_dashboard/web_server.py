from http.server import SimpleHTTPRequestHandler, HTTPServer
from typing import Optional, Tuple, List

from mcdreforged.api.all import *
from minecraft_version_api import *

from .config_manager import get_config

global server
global data_api
global config
global webpage_content

@new_thread('WebServer')
def setup_server(instance: PluginServerInterface):
    global webpage_content
    webpage_content = get_webpage(instance)

    global config
    config = get_config(instance)

    global data_api
    data_api = instance.get_plugin_instance('minecraft_data_api')

    port = config.port
    host = "127.0.0.1"

    print('Starting up web server on port {}'.format(port))
    global server
    server = HTTPServer((host, port), HTTPRequestHandler)
    server.serve_forever()


def stop_server():
    print('Shutting down web server')
    server.shutdown()
    return


# Endpoints
class HTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == '/server-name':
            self.get_server_name()
        elif self.path == '/server-version':
            self.get_server_version()
        else:
            # Return webpage
            self.get_page()

    def get_server_name(self):
        global config
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(config.server_name.encode())

    def get_server_version(self):
        global config
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(config.server_version.encode())

    def get_page(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(webpage_content.encode())


# Get player count
def get_player_list(mpa):
    query_result: Optional[Tuple[int, int, List[str]]] = mpa.get_server_player_list()
    if query_result is not None:
        current_player_count = query_result[0]
        max_players = query_result[1]
        player_list = query_result[2]


def get_webpage(instance: PluginServerInterface) -> str:
    stream = instance.open_bundled_file('mc_server_dashboard/static/index.html')
    content = stream.read(-1).decode()
    stream.close()

    return content
