from CHP_api.CHP_lowlevel_api import Api
import typing as t

from CHP_api.utils.Meta import SmartClientSingleton


class ChpClient(metaclass=SmartClientSingleton):

    def __init__(
            self,
            host: str,
            port: t.Union[str, int],
            login: str = '',
            password: str = '',
            token: str = '',
            mode: int = 0
    ) -> None:

        """


        :param host: host url of api server.
            For example: '127.0.0.1'
        :param port: port to connect to api server.
            For example: 5001
        :param login: your IT Capital account login.
        :param password: your IT Capital account password
        :param token: your access token
        :param mode: connect mode [0 - demo | 1 - production]
        """

        # self._api = Api(host, port)  # Todo

        self._token = token

    @property
    def token(self) -> str:
        return self._token

    def __del__(self):
        # self._api.disconnect(token=self._token) # Todo
        print(f"Client with token {self._token} deleted")
