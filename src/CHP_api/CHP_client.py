import typing as t
from json import loads as jsonify

from CHP_api.CHP_lowlevel_api import Api
from CHP_api.utils.Meta import SmartClientSingleton
from CHP_api.CHPExceptions import (
    ApiConnectionError,
    ApiRequestException
)


class ChpClient(metaclass=SmartClientSingleton):

    def __init__(
            self,
            host: str,
            port: t.Union[str, int],
            login: str,
            password: str,
            *,
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
        :param token: your access token || Warn: token is key-only argument
        :param mode: connect mode [0 - demo | 1 - production] || Warn: token is key-only argument
        """

        self._api = Api(host=host, port=port, ssh=False)

        connect_resp = self._api.Connect(login=login, password=password, token=token, mode=mode)
        connect_resp = jsonify(connect_resp.text)
        if not connect_resp['result']:
            raise ApiConnectionError(connect_resp['reason'], data=connect_resp)

        self._token: str = token
        self._login: str = login
        self._password: str = password

        self.__listening_quotes: t.List = []

    @property
    def token(self) -> str:
        return self._token

    @property
    def login(self) -> str:
        return self._login

    @property
    def password(self) -> str:
        return self._password

    @property
    def listening_quotes(self) -> t.List[str]:
        return [*self.__listening_quotes]

    @staticmethod
    def _check_response(resp):
        if not resp['result']:
            raise ApiRequestException(resp['reason'], data=resp)

    def GetBars(self, since: str, interval: int, symbol: str, count: int):
        """

        :param since:
        :param interval:
        :param symbol:
        :param count:
        :return:
        """
        resp = self._api.GetBars(
            token=self._token,
            since=since,
            interval=interval,
            symbol=symbol,
            count=count
        )
        resp = jsonify(resp.text)
        self._check_response(resp)

        return resp['data']

    def GetSymbols(self):  # TODO
        """

        :return:
        """
        resp = self._api.GetSymbols(token=self._token)
        resp = jsonify(resp.text)
        self._check_response(resp)

        return resp['data']

    def GetTrades(self, since: str, symbol: str, count: int):  # TODO

        resp = self._api.GetTrades(
            token=self._token,
            since=since,
            symbol=symbol,
            count=count
        )
        resp = jsonify(resp.text)
        self._check_response(resp)

        return resp['data']

    def ListenQuotes(self, symbols: t.List[str]) -> t.Dict[str, bool]:
        """

        :param symbols: list of symbols  like ['GAZP'] or ['GAZP', 'SBER']
        :return:
        """
        if not isinstance(symbols, list):
            raise TypeError('the symbols must be list instance')

        results = {}
        for symbol in symbols:
            if symbol not in self.__listening_quotes:
                resp = self._api.ListenQuotes(token=self._token, symbol=symbol)
                resp = jsonify(resp.text)

                results[symbol] = resp['result']

                if resp['result']:
                    self.__listening_quotes.append(symbol)

        return results

    def UpdateQuote(self):
        resp = self._api.UpdateQuote(token=self._token)
        resp = jsonify(resp.text)


    def CancelQuotes(self, symbols: t.Optional[t.List[str]] = None) -> t.Dict[str, bool]:
        """

        :param symbols: [Optional] if None Cancel all listening Quotes. else list of symbols  like ['GAZP']
        or ['GAZP', 'SBER']
        :return:
        """
        if symbols is None:
            symbols = [*self.__listening_quotes]
        elif not isinstance(symbols, list):
            raise TypeError('the symbols must be list instance')

        results = {}
        for symbol in symbols:
            resp = self._api.CancelQuotes(token=self._token, symbol=symbol)
            resp = jsonify(resp.text)

            results[symbol] = resp['result']
            if resp['result']:
                self.__listening_quotes.remove()

        return results
















    def __del__(self):
        disconnect_resp = self._api.Disconnected(
            login=self._login,
            password=self._password,
            token=self._token
        )
        disconnect_resp = jsonify(disconnect_resp.text)
        if not disconnect_resp['result']:
            raise ApiConnectionError('Ошибка отключения от api, Сообзите о проблеме разработчикам',
                                     data=disconnect_resp)

        print(f"Client with token {self._token} deleted")
