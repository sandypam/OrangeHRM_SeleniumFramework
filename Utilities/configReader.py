from configparser import ConfigParser
import os


def readConfig(section, key):
    config = ConfigParser()

    base_dir = os.path.dirname(__file__)  # .../Utilities
    ini_path = os.path.join(base_dir, "..", "ConfigurationData", "config.ini")  # adjust folder/name

    read_files = config.read(ini_path)
    if not read_files:
        raise FileNotFoundError(f"Config file not found or not readable: {ini_path}")

    if not config.has_section(section):
        raise KeyError(f"Missing section [{section}] in {ini_path}. Sections found: {config.sections()}")

    if not config.has_option(section, key):
        raise KeyError(f"Missing key '{key}' in section [{section}] in {ini_path}")

    return config.get(section, key)

    print("INI PATH", ini_path)
    print("SECTION:", config.sections())

# print(readConfig("Locators", "name_CSS"))




