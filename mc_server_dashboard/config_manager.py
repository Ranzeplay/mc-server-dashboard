import os.path

from mcdreforged.plugin.server_interface import PluginServerInterface

from mc_server_dashboard.config_model import PluginConfig


def create_default_config(server: PluginServerInterface):
    config_path = os.path.join(server.get_data_folder(), 'config.json')
    if not os.path.exists(config_path):
        # Extract default config file if not exist
        server.save_config_simple(config=PluginConfig())


def get_config(server: PluginServerInterface) -> PluginConfig:
    return server.load_config_simple(target_class=PluginConfig)
