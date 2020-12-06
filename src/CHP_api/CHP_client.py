import typing as t
from json import loads

from CHP_api.CHP_lowlevel_api import Api
from CHP_api.utils.Meta import SmartClientSingleton
from CHP_api.CHPExceptions import (
    ApiConnectionError
)


class ChpClient(metaclass=SmartClientSingleton):

    def __init__(
            self,
            host: str,
            port: t.Union[str, int],
            login: str,
            password: str,
            token: str,
            mode: int = 0
    ) -> None:
        """

        :param host: host url of api server.
            For example: '127.0.0.1'
        :param port: port to connect to api server.
            For example: 5001
        :param login: your ITI Capital account login.
        :param password: your ITI Capital account password
        :param token: your access token
        :param mode: connect mode [0 - demo | 1 - production]
        """

        self._api = Api(host=host, port=port, ssh=False)

        connect_resp = self._api.Connect(login=login, password=password, token=token, mode=mode)
        connect_resp = loads(connect_resp.text)[0]
        if not connect_resp['result']:
            raise ApiConnectionError(connect_resp['reason'])

        self._token: str = token
        self._login: str = login
        self._password: str = password

    @property
    def token(self) -> str:
        return self._token

    @property
    def login(self) -> str:
        return self._login

    @property
    def password(self) -> str:
        return self._password

    def GetBars(self, since: str, interval: int, symbol: str, count: int):
        """

        :param since:
        :param interval:
        :param symbol:
        :param count:
        :return:
        """
        resp = self._api.GetBars(token=self._token, since=since, interval=interval,
                                 symbol=symbol, count=count)

    def GetSymbols(self):  # TODO
        pass

    def GetMyPortfolioData(self):  # TODO
        pass

    def GetPortfolioList(self):  # TODO
        pass

    def GetTrades(self):  # TODO
        pass

    def AddTickHistory(self):  # TODO
        pass

    def __del__(self):
        disconnect_resp = self._api.Disconnected(login=self._login, password=self._password,
                                                 token=self._token)
        disconnect_resp = loads(disconnect_resp.text)[0]
        if not disconnect_resp['result']:
            raise ApiConnectionError('Ошибка отключения от api, Сообзите о проблеме разработчикам')

        print(f"Client with token {self._token} deleted")
