from configparser import ConfigParser

class Settings:
    def __init__(self, config_file='config.ini'):
        self.config = ConfigParser()
        self.config_file = config_file
        self.load_settings()

    def load_settings(self):
        self.config.read(self.config_file)
        # 설정 파일에서 설정 불러오기

    def save_settings(self):
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
        # 설정 파일에 설정 저장하기
