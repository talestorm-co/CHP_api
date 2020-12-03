from .CHP_lowlevel_api import Api


class ChpClient:

    def __init__(self, host, port, login, password, token, mode):
        self.api = Api(host, port)  # Todo

        resp = self.api.connect()
        