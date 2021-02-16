import typing as t
from json import loads, JSONDecodeError
from pprint import pprint


from CHP_api.CHP_lowlevel_api import Api
from CHP_api.utils.Meta import SmartClientSingleton
from CHP_api.CHPExceptions import (
    ApiConnectionError,
    ApiRequestException
)


def jsonify(data: str) -> t.Dict:
    try:
        res = loads(data)
    except JSONDecodeError as e:
        raise ApiRequestException('Пришел не json', data=data)
    return res


class ChpClient(
    # metaclass=SmartClientSingleton
):

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

        self._token: str = token
        self._login: str = login
        self._password: str = password
        self._mode = mode

        self._api = Api(host=host, port=port, ssh=False)

        self._listening_quotes: t.List[str] = []
        self._listening_ticks: t.List[str] = []
        self._listening_bid_ask: t.List[str] = []
        self._listening_portfolios: t.List[str] = []

    @property
    def Token(self) -> str:
        return self._token

    @property
    def Login(self) -> str:
        return self._login

    @property
    def Password(self) -> str:
        return self._password

    @property
    def Mode(self) -> int:
        return self._mode

    @property
    def listening_quotes(self) -> t.List[str]:
        return self._listening_quotes.copy()

    @listening_quotes.setter
    def listening_quotes(self, value: t.List[str]) -> None:
        if not isinstance(value, list):
            raise ValueError(f"{value} must be List[str] instance")
        self._listening_quotes = value

    @listening_quotes.deleter
    def listening_quotes(self) -> None:
        self._listening_quotes = []


    @property
    def listening_ticks(self) -> t.List[str]:
        return self._listening_ticks.copy()

    @listening_ticks.setter
    def listening_ticks(self, value: t.List[str]) -> None:
        if not isinstance(value, list):
            raise ValueError(f"{value} must be List[str] instance")
        self._listening_ticks = value

    @listening_ticks.deleter
    def listening_ticks(self) -> None:
        self._listening_ticks = []


    @property
    def listening_bid_ask(self) -> t.List[str]:
        return self._listening_bid_ask.copy()

    @listening_bid_ask.setter
    def listening_bid_ask(self, value: t.List[str]) -> None:
        if not isinstance(value, list):
            raise ValueError(f"{value} must be List[str] instance")
        self._listening_bid_ask = value

    @listening_bid_ask.deleter
    def listening_bid_ask(self) -> None:
        self._listening_bid_ask = []


    @property
    def listening_portfolios(self) -> t.List[str]:
        return self._listening_portfolios.copy()

    @listening_portfolios.setter
    def listening_portfolios(self, value: t.List[str]) -> None:
        if not isinstance(value, list):
            raise ValueError(f"{value} must be List[str] instance")
        self._listening_portfolios = value

    @listening_portfolios.deleter
    def listening_portfolios(self) -> None:
        self._listening_portfolios = []


    @staticmethod
    def _check_response(resp):

        for key in ('data', 'result'):
            if key not in resp:
                raise ApiRequestException(f'У ответа сервера нет поля {key}', data=resp)

        try:
            if not resp['result']:
                raise ApiRequestException(resp['reason'], data=resp)
        except KeyError:
            raise ApiRequestException('У ответа сервера нет поля result')

    def Connect(self):

        connect_resp = self._api.Connected(login=self._login, password=self._password, token=self._token, mode=self._mode)
        connect_resp = jsonify(connect_resp.text)

        if not connect_resp['result']:
            raise ApiConnectionError(connect_resp['reason'], data=connect_resp)

        return connect_resp

    def Reconnect(self):
        resp = self._api.Reconnection(login=self._login, password=self._password, token=self._token,
                                      mode=self._mode)

        resp = jsonify(resp.text)

        if not resp['result']:
            raise ApiConnectionError(resp['reason'], data=resp)
        else:
            return True

    def Disconnect(self):
        disconnect_resp = self._api.Disconnected(
            login=self._login,
            password=self._password,
            token=self._token
        )

        disconnect_resp = jsonify(disconnect_resp.text)

        if not disconnect_resp['result']:
            raise ApiConnectionError('Ошибка отключения от api, Сообщите о проблеме разработчикам',
                                     data=disconnect_resp)

        print(f"Client with token {self._token} disconnected")

    def GetBars(self, since: str, interval: int, symbol: str, count: int):
        """

        :param since:
        :param interval:
        :param symbol:
        :param count:
        :return:
        """
        resp = self._api.GetBars( # Отправляем запрос с параметрами на сервер
            token=self._token,
            since=since,
            interval=interval,
            symbol=symbol,
            count=count
        )
        resp = jsonify(resp.text)  # достаём из http Ответа json
        self._check_response(resp)  # проверяем json

        return resp['data']  #  возвращаем

    def GetSymbols(self):  # TODO
        """

        :return:
        """
        resp = self._api.GetSymbols(token=self._token)
        resp = jsonify(resp.text)
        self._check_response(resp)

        return resp['data']

    def GetTrades(self, since: str, symbol: str, count: int):  # TODO
        """

        :param since:
        :param symbol:
        :param count:
        :return:
        """
        resp = self._api.GetTrades(
            token=self._token,
            since=since,
            symbol=symbol,
            count=count
        )
        resp = jsonify(resp.text)
        self._check_response(resp)

        return resp['data']

    def ListenQuotes(self, symbols: t.Union[t.List[str], str]) -> t.Dict[str, t.Dict]:
        """
        Listening on the quotes by symbols
        :param symbols: list of symbols  like ['GAZP'] or ['GAZP', 'SBER']
        :return:
        """
        if isinstance(symbols, str):
            symbols = [symbols]

        results = {}
        for symbol in symbols:
            resp = self._api.ListenQuotes(token=self._token, symbol=symbol)
            resp = jsonify(resp.text)

            results[symbol] = resp

            try:
                if resp['result']:
                    self._listening_quotes.append(symbol)
            except KeyError:
                pass  # server response hove no key result

        return results

    def UpdateQuote(self):
        """
        get quotes for all listening symbols
        :return:
        """
        resp = self._api.UpdateQuote(token=self._token)
        resp = jsonify(resp.text)

        self._check_response(resp)


        return resp['data']


    def CancelQuotes(self, symbols: t.Optional[t.Union[t.List[str], str]] = None):
        """
        Unsubscribe from the specified quotes (if nothing is passed, unsubscribe from all quotes)
        :param symbols: [Optional] if None Cancel all listening Quotes. else list of symbols  like ['GAZP']
        or ['GAZP', 'SBER']
        :return:
        """

        if symbols is None or \
                not symbols:
            symbols = self._listening_quotes.copy()
        elif isinstance(symbols, str):
            symbols = [symbols]

        results = {}
        for symbol in symbols:
            resp = self._api.CancelQuotes(token=self._token, symbol=symbol)
            resp = jsonify(resp.text)

            results[symbol] = resp

            if resp['result'] and symbol in self._listening_quotes:
                self._listening_quotes.remove(symbol)

        return results

    def ListenTicks(self, symbols: t.List[str]):
        """
        Listening on the ticks by symbols
        :param symbols: list of symbols  like ['GAZP'] or ['GAZP', 'SBER']
        :return:
        """
        if isinstance(symbols, str):
            symbols = [symbols]

        results = {}
        for symbol in symbols:

            resp = self._api.ListenTicks(token=self._token, symbol=symbol)
            resp = jsonify(resp.text)

            results[symbol] = resp

            try:
                if resp['result']:
                    self._listening_ticks.append(symbol)
            except KeyError:
                pass  # server response hove no key result

        return results

    def UpdateTicks(self):
        """
        get ticks for all listening symbols
        :return:
        """
        resp = self._api.AddTick(token=self._token)
        resp = jsonify(resp.text)

        self._check_response(resp)

        return resp['data']

    def CancelTicks(self, symbols: t.Optional[t.List[str]] = None) -> t.Dict[str, t.Dict]:
        """
        Unsubscribe from the specified ticks (if nothing is passed, unsubscribe from all quotes)
        :param symbols: [Optional] if None Cancel all listening ticks. else list of symbols  like ['GAZP']
        or ['GAZP', 'SBER']
        :return:
        """
        if symbols is None or \
                not symbols:
            symbols = self._listening_ticks.copy()
        elif isinstance(symbols, str):
            symbols = [symbols]

        results = {}
        for symbol in symbols:
            resp = self._api.CancelTicks(token=self._token, symbol=symbol)
            resp = jsonify(resp.text)

            results[symbol] = resp

            if resp['result'] and symbol in self._listening_ticks:
                self._listening_ticks.remove(symbol)

        return results

    def ListenBidAsks(self, symbols: t.Union[t.List[str], str]):

        if isinstance(symbols, str):
            symbols = [symbols]

        results = {}
        for symbol in symbols:

            resp = self._api.ListenBidAsks(token=self._token, symbol=symbol)
            resp = jsonify(resp.text)


            results[symbol] = resp

            try:
                if resp['result'] :
                    self._listening_bid_ask.append(symbol)
            except KeyError:
                pass  # server response hove no key result

        return results

    def UpdateBidAsks(self):
        resp = self._api.UpdateBidAsk(token=self._token)
        resp = jsonify(resp.text)
        self._check_response(resp)
        return resp['data']

    def CancelBidAsks(self, symbols: t.Optional[t.Union[t.List[str], str]] = None) -> t.Dict[str, t.Dict]:  # todo str support
        if symbols is None or \
                not symbols:
            symbols = self._listening_bid_ask.copy()
        elif isinstance(symbols, str):
            symbols = [symbols]

        results = {}
        for symbol in symbols:
            resp = self._api.CancelBidAsks(token=self._token, symbol=symbol)
            resp = jsonify(resp.text)

            results[symbol] = resp

            if resp['result'] and symbol in self._listening_bid_ask:
                self._listening_bid_ask.remove(symbol)

        return results

    def GetMyPortfolioData(self, portfolio: str, mode: int):
        """

        :param portfolio:
        :param mode:
        :return:
        """
        resp = self._api.GetMyPortfolioData(token=self._token, mode=mode, portfolio=portfolio)
        resp = jsonify(resp.text)
        self._check_response(resp)

        return resp['data']

    def GetPortfolioList(self):
        resp = self._api.GetPortfolioList(token=self._token)
        resp = jsonify(resp.text)
        self._check_response(resp)

        return resp['data']

    def ListenPortfolio(self, portfolios: t.Union[t.List[str], str]):

        if isinstance(portfolios, str):
            portfolios = [portfolios]

        results = {}
        for prt in portfolios:

            resp = self._api.ListenPortfolio(token=self._token, portfolio=prt)
            resp = jsonify(resp.text)

            results[prt] = resp

            try:
                if resp['result']:
                    self._listening_portfolios.append(prt)
            except KeyError:
                pass  # server response hove no key result

        return results

    def CancelPortfolio(self, portfolios: t.Optional[t.Union[t.List[str], str]] = None):
        if portfolios is None or \
                not portfolios:
            portfolios = self._listening_portfolios.copy()
        elif isinstance(portfolios, str):
            portfolios = [portfolios]

        results = {}

        for prt in portfolios:
            resp = self._api.CancelPortfolio(token=self._token, portfolio=prt)
            resp = jsonify(resp.text)

            results[prt] = resp

            if resp['result'] and prt in self._listening_portfolios:
                self._listening_portfolios.remove(prt)

        return results


    def PlaceOrder(self, portfolio, symbol, action, type_, validity, price, amount, stop, cookie):
        """
        :param portfolio: portfolio name on the trading platform. Like "ST125465-MO-01"
        :param symbol: Код ЦБ из таблицы котировок TC Matrix
        :param action: Вид торговой операции. Принимает следующие значения:
                    1 - Купить
                    2 - Продать
                    3 - Открыть «короткую позицию»
                    4 – Закрыть «короткую» позицию
        :param type_: Тип приказа. Принимает следующие значения:
                    1 - Приказ по рынку
                    2 - Лимитированный приказ
                    3 - Стоп приказ
                    4 – приказ Стоп-Лимит
        :param validity: Срок действия приказа. Принимает следующие значения:
                    1 - День
                    2 – GTC (до отмены, макс. 30 дней)
        :param price: Цена Лимит - для заявок типа Лимит и Стоп-Лимит
                    0 - для приказа: По рынку или Стоп
        :param amount: Объем, ЦБ в приказе
        :param stop: Цена СТОП для приказа типа Стоп и Стоп-Лимит
                    0 - для приказа: По рынку или Лимит
        :param cookie: Ваш уникальный номер приказа, используется для
                    определения Id приказа через события OrderSucceeded/
                    OrderFailed и UpdateOrders
        :return:
        """

        resp = self._api.PlaceOrder(
            token=self._token,
            portfolio=portfolio,
            symbol=symbol,
            action=action,
            type_=type_,
            price=price,
            amount=amount,
            validity=validity,
            stop=stop,
            cookie=cookie
        )
        resp = jsonify(resp.text)
        self._check_response(resp)

        return resp['data']

    def MoveOrder(self, portfolio: str, symbol: str, orderid: str, targetprice: float):

        resp = self._api.MoveOrder(
            token=self._token,
            portfolio=portfolio,
            symbol=symbol,
            orderid=orderid,
            targetprice=targetprice
        )
        resp = jsonify(resp.text)
        self._check_response(resp)

        return resp['data']

    def CancelOrder(self, portfolio: str, symbol: str, orderid: str):

        resp = self._api.CancelOrder(
            token=self._token,
            portfolio=portfolio,
            symbol=symbol,
            orderid=orderid
        )
        resp = jsonify(resp.text)
        self._check_response(resp)

        return resp['data']

    def UpdateOrder(self):
        resp = self._api.UpdateOrder(
            token=self._token
        )
        resp = jsonify(resp.text)
        self._check_response(resp)
        return resp['data']

    def UpdatePosition(self):
        resp = self._api.UpdatePosition(
            token=self._token
        )
        resp = jsonify(resp.text)
        self._check_response(resp)

        return resp['data']

    def AddTrade(self):
        resp = self._api.AddTrade(
            token=self._token
        )
        resp = jsonify(resp.text)
        self._check_response(resp)

        return resp['data']

    def SetPortfolio(self):
        resp = self._api.SetPortfolio(
            token=self._token
        )
        resp = jsonify(resp.text)
        self._check_response(resp)

        return resp['data']

    # def __del__(self):
    #     disconnect_resp = self._api.Disconnected(
    #         login=self._login,
    #         password=self._password,
    #         token=self._token
    #     )
    #     disconnect_resp = jsonify(disconnect_resp.text)
    #     if not disconnect_resp['result']:
    #         raise ApiConnectionError('Ошибка отключения от api, Сообзите о проблеме разработчикам',
    #                                  data=disconnect_resp)
    #
    #     print(f"Client with token {self._token} deleted")
