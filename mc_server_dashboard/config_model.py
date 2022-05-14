from mcdreforged.utils.serializer import Serializable


class PluginConfig(Serializable):
    server_name: str = 'hServer'
    port: int = 2333
    server_version: str = '1.18.1'

