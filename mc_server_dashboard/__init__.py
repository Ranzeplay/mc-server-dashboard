from .web_server import *
from .config_manager import *
from mcdreforged.api.all import *


def on_load(server: PluginServerInterface, old):
    print('Plugin has been loaded')

    create_default_config(server)
    setup_server(server)


def on_unload(server: PluginServerInterface):
    stop_server()
