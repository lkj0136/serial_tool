from configparser import ConfigParser

def load_config(file='config.ini'):
    config = ConfigParser()
    config.read(file)
    return config

def save_config(config, file='config.ini'):
    with open(file, 'w') as configfile:
        config.write(configfile)
