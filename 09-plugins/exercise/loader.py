import importlib


class PluginInterface:
    @staticmethod
    def initialize() -> None:
        """Initialize the plugin"""
        ...


def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name)  # type: ignore


def load_plugins(plugins: list[str]) -> None:
    """Load the plugins defined in the plugins list"""

    for plugin_name in plugins:
        print(f"Import plugin {plugin_name}")
        plugin = import_module(plugin_name)
        plugin.initialize()
