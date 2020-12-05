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

    def Connect(self, login: str, password: str, token: str, mode: int) -> requests.Response:
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
                'token': token,
                "Since": since,
                "Interval": interval,
                'symbol': symbol,
                'count': count,
            }
        )

        return resp

    def GetSymbols(self, token: str, ):  # TODO
        pass

    def GetMyPortfolioData(self, token: str, ) -> requests.Response:  # TODO
        pass

    def GetPortfolioList(self, token):  # TODO
        pass

    def GetTrades(self, token, ):  # TODO
        pass

    def AddTickHistory(self, token):  # TODO
        pass

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

    def ListenTicks(self, token: str, symbol: str) -> requests.Response:  # Todo
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

    def UpdateTicks(self, ):  # Todo
        pass

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

    def CancelTicks(self, ):  # Todo
        pass

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

    def UpdateBidAsks(self, ):  # Todo
        pass

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

    def ListenPortfolio(self, token: str, ):
        pass

    def PlaceOrder(self, token, portfolio, symbol, action, type, validity, price, amount, stop, cookie):  # TODO
        pass

    def MoveOrder(self, token, portfolio, symbol, orderid, targetprice):  # TODO
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

    def CancelOrder(self, token, portfolio, symbol, orderid):  # TODO
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

    def UpdateOrder(self, token):  # TODO
        resp = self._req_method(
            method_url='AccountInformation/UpdateOrder',
            method_data={
                'token': token,
            }
        )
        return resp

    def UpdatePosition(self, token):  # TODO
        resp = self._req_method(
            method_url='AccountInformation/UpdatePosition',
            method_data={
                'token': token,
            }
        )
        return resp

    def AddTrade(self, token):  # TODO
        resp = self._req_method(
            method_url='AccountInformation/AddTrade',
            method_data={
                'token': token,
            }
        )
        return resp

    def SetPortfolio(self, token):  # TODO
        resp = self._req_method(
            method_url='AccountInformation/SetPortfolio',
            method_data={
                'token': token,
            }
        )
        return resp

    def CancelPortfolio(self, token, portfolio):  # TODO
        resp = self._req_method(
            method_url='AccountInformation/CancelPortfolio',
            method_data={
                'token': token,
                'portfolio': portfolio
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


if __name__ == '__main__':
    api = Api(host="fdfdfd", port=5000)
