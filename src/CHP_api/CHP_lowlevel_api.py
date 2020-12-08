import requests
import typing as t


# http://85.143.79.6:5001

class Api:

    def __init__(self, host: str, port: t.Union[int, str] = 5001, ssh: bool = False) -> None:
        """
        Initialise Api instance with address to connection remote api.
        :param host: API host address (IP address or url domain)
        :param port: port to connect. Default: 5001
        :param ssh: if ssh is True connection by https, else by http. Default: False
        """
        if port:
            self._host_url = f"{'https://' if ssh else 'http://'}{host}"
            if port:
                self._host_url += f":{port}"

    def _req_method(self, method_url: str, method_data: t.Optional[t.Dict] = None) -> requests.Response:
        """
        Sending post request to <full_host_address>/<method_url> with json context: <method_data>
        For example:
            _req_method(
                method_url='Trade',
                method_data={
                    "token":'12345'
                }
            )
            is sending post to http://127.0.0.1:5001/Trade
            with json {"token":"12345"}

        :param method_url:
        :param method_data:
        :return:
        """
        resp = requests.post(
            f'{self._host_url}/{method_url}',
            json=method_data,
            headers={'Content-Type': 'application/json'}
        )
        return resp

    def Connected(self, login: str, password: str, token: str, mode: int) -> requests.Response:
        """
        Sending request to connecting to remote api with your auth data

        :param login: user login into ITI Capital
        :param password: user password into ITI Capital
        :param token: user auth token
        :param mode: mode to connect [0 - demo | 1 - real connection]
        :return:
        """
        resp = self._req_method(
            method_url='Auth/Connected',
            method_data={
                'login': login,
                'password': password,
                'token': token
                # 'mode': mode, # TODO Узнать что там с модом
            }
        )
        return resp

    def Reconnection(self, login: str, password: str, token: str, mode: int) -> requests.Response:
        """
        Sending request to connecting to remote api with your auth data

        :param login: user login into ITI Capital
        :param password: user password into ITI Capital
        :param token: user auth token
        :param mode: mode to connect [0 - demo | 1 - real connection]
        :return:
        """
        resp = self._req_method(
            method_url='Auth/Reconnection',
            method_data={
                'login': login,
                'password': password,
                'token': token
                # 'mode': mode, # TODO Узнать что там с модом
            }
        )
        return resp

    def Disconnected(self, login: str, password: str, token: str) -> requests.Response:
        """
        Sending request to disconnect user from API, and close thread connection
        :param login: user login into ITI Capital
        :param password: user password into ITI Capital
        :param token: user auth token
        :return:
        """
        resp = self._req_method(
            method_url='Auth/Disconnected',
            method_data={
                'login': login,
                'password': password,
                'token': token
            }
        )
        return resp

    def GetBars(self, token: str, since: str, interval: int, symbol: str, count: int) -> requests.Response:

        """

        :param token: user auth token
        :param since: since date like "2020-10-10T10:10:10.000"
        :param interval: bar interval
        :param symbol: symbol like "GAZP"
        :param count: count of bars since "since" parameter
        :return:
        """
        resp = self._req_method(
            method_url='Instruments/GetBars',
            method_data={
                "token": token,
                "since": since,
                "interval": interval,
                "symbol": symbol,
                "count": count,
            }
        )

        return resp

    def GetSymbols(self, token: str) -> requests.Response:
        """

        :param token: user auth token
        :return:
        """
        resp = self._req_method(
            method_url='Instruments/GetSymbols',
            method_data={
                "token": token
            }
        )
        return resp

    def GetMyPortfolioData(self, token: str, mode: int, portfolio: str) -> requests.Response:
        """

        :param token: user auth token
        :param mode: Application type [1 - Active | 2 - All]
        :param portfolio: portfolio name on the trading platform. Like "ST125465-MO-01"
        :return:
        """
        resp = self._req_method(
            method_url='HistoricalData/GetMyPortfolioData',
            method_data={
                "token": token,
                "mode": mode,
                "portfolio": portfolio
            }
        )
        return resp

    def GetPortfolioList(self, token: str) -> requests.Response:
        """

        :param token: user auth token
        :return:
        """
        resp = self._req_method(
            method_url='AccountInformation/GetPortfolioList',
            method_data={
                "token": token
            }
        )

        return resp

    def GetTrades(self, token: str, since: str, symbol: str, count: int) -> requests.Response:
        # TODO Проверить работу (doesn't tested)
        """

        :param token:
        :param since:
        :param symbol:
        :param count:
        :return:
        """
        resp = self._req_method(
            method_url='Instruments/GetTrades',
            method_data={
                "from": since,
                "symbol": symbol,
                "count": count,
                "token": token
            }
        )
        return resp

    def ListenQuotes(self, token: str, symbol: str) -> requests.Response:
        """

        :param token: user auth token
        :param symbol: symbol like "GAZP"
        :return:
        """
        resp = self._req_method(
            method_url='Instruments/ListenQuotes',
            method_data={
                'token': token,
                'symbol': symbol,
            }
        )
        return resp

    def UpdateQuote(self, token: str) -> requests.Response:
        """

        :param token: user auth token
        :return:
        """
        resp = self._req_method(
            method_url='Instruments/UpdateQuote',
            method_data={
                'token': token,
            }
        )
        return resp

    def CancelQuotes(self, token: str, symbol: str) -> requests.Response:
        """

        :param token: user auth token
        :param symbol: symbol like "GAZP"
        :return:
        """
        resp = self._req_method(
            method_url='Instruments/CancelQuotes',
            method_data={
                "token": token,
                "symbol": symbol
            }
        )
        return resp

    def ListenTicks(self, token: str, symbol: str) -> requests.Response:
        """

        :param token: user auth token
        :param symbol: symbol like "GAZP"
        :return:
        """
        resp = self._req_method(
            method_url='Instruments/ListenTicks',
            method_data={
                "token": token,
                "symbol": symbol
            }
        )
        return resp

    def AddTick(self, token: str) -> requests.Response:
        """

        :param token: user auth token
        :return:
        """

        resp = self._req_method(
            method_url='Instruments/AddTick',
            method_data={
                'token': token,
            }
        )
        return resp

    def CancelTicks(self, token: str, symbol: str) -> requests.Response:
        """

        :param token: user auth token
        :param symbol: symbol like "GAZP"
        :return:
        """
        resp = self._req_method(
            method_url='Instruments/CancelTicks',
            method_data={
                "token": token,
                "symbol": symbol
            }
        )
        return resp

    def ListenBidAsks(self, token: str, symbol: str) -> requests.Response:
        """

        :param token: user auth token
        :param symbol: symbol like "GAZP"
        :return:
        """
        resp = self._req_method(
            method_url='Instruments/ListenBidAsks',
            method_data={
                "token": token,
                "symbol": symbol,
            }
        )
        return resp

    def UpdateBidAsk(self, token: str) -> requests.Response :
        """
        :param token: user auth token
        :return:
        """

        resp = self._req_method(
            method_url='Instruments/UpdateBidAsk',
            method_data={
                'token': token,
            }
        )
        return resp

    def CancelBidAsks(self, token: str, symbol: str) -> requests.Response:
        """

        :param token: user auth token
        :param symbol: symbol like "GAZP"
        :return:
        """
        resp = self._req_method(
            method_url='Instruments/CancelBidAsks',
            method_data={
                "token": token,
                "symbol": symbol
            }
        )
        return resp

    def ListenPortfolio(self, token: str, portfolio: str) -> requests.Response:
        """

        :param token: user auth token
        :param portfolio: portfolio name on the trading platform. Like "ST125465-MO-01"
        :return:
        """
        resp = self._req_method(
            method_url='AccountInformation/ListenPortfolio',
            method_data={
                "token": token,
                "portfolio": portfolio
            }
        )
        return resp

    def PlaceOrder(self, token: str, portfolio: str, symbol: str, action: int, type_: int, validity: int,
                   price: float, amount: float, stop: float,
                   cookie: float) -> requests.Response:
        """

        :param token: user auth token
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
        resp = self._req_method(
            method_url='Order/Place',
            method_data={
                "token": token,
                "portfolio": portfolio,
                "symbol": symbol,
                "action": action,
                "type": type_,
                "validity": validity,
                "price": price,
                "amount": amount,
                "stop": stop,
                "cookie": cookie

            }
        )
        return resp

    def MoveOrder(self, token: str, portfolio:str, symbol: str, orderid: str, targetprice: int) -> requests.Response:
        """

        :param token:
        :param portfolio:
        :param symbol:
        :param orderid:
        :param targetprice:
        :return:
        """
        resp = self._req_method(
            method_url='Order/Move',
            method_data={
                'token': token,
                'portfolio': portfolio,
                'symbol': symbol,
                'orderid': orderid,
                'targetprice': targetprice
            }
        )
        return resp

    def CancelOrder(self, token: str, portfolio: str, symbol: str, orderid: str) -> requests.Response:
        """

        :param token:
        :param portfolio:
        :param symbol:
        :param orderid:
        :return:
        """
        resp = self._req_method(
            method_url='Order/Cancel',
            method_data={
                'token': token,
                'portfolio': portfolio,
                'symbol': symbol,
                'orderid': orderid,
            }
        )
        return resp

    def UpdateOrder(self, token: str) -> requests.Response:
        """

        :param token:
        :return:
        """
        resp = self._req_method(
            method_url='AccountInformation/UpdateOrder',
            method_data={
                'token': token,
            }
        )
        return resp

    def UpdatePosition(self, token: str) -> requests.Response:
        """

        :param token:
        :return:
        """
        resp = self._req_method(
            method_url='AccountInformation/UpdatePosition',
            method_data={
                'token': token,
            }
        )
        return resp

    def AddTrade(self, token: str) -> requests.Response:
        """

        :param token:
        :return:
        """
        resp = self._req_method(
            method_url='AccountInformation/AddTrade',
            method_data={
                'token': token,
            }
        )
        return resp

    def SetPortfolio(self, token: str) -> requests.Response:
        """

        :param token:
        :return:
        """
        resp = self._req_method(
            method_url='AccountInformation/SetPortfolio',
            method_data={
                'token': token,
            }
        )
        return resp

    def CancelPortfolio(self, token: str, portfolio: str) -> requests.Response:
        """
        
        :param token:
        :param portfolio:
        :return:
        """
        resp = self._req_method(
            method_url='AccountInformation/CancelPortfolio',
            method_data={
                'token': token,
                'portfolio': portfolio
            }
        )
        return resp


