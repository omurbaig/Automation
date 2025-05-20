import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin', 'admin_page_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('admin', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin', 'password')
        return password

    @staticmethod
    def get_invalid_password():
        invalid_password = config.get('admin', 'invalid_password')
        return invalid_password