import requests
import typing


# http://85.143.79.6:5001

class Api:

    def __init__(self, url, port, ssh=False):

        if port:
            self.url = f"{'https://' if ssh else 'http://'}{url}"
            if port:
                self.url += f":{port}"

    def _req(self, sub_url: str, data: typing.Dict = {}) -> requests.Response:
        json_data = self._get_json_data(data)

        resp = requests.post(
            f'{self.url}/{sub_url}',
            json=json_data,
            headers={'Content-Type': 'application/json'}
        )
        return resp

    def Connect(self, login, password, token, mode):
        resp = self._req(
                        'Auth/Connected',
                        data={
                            'login': login,
                            'password': password,
                            'token': token,
                            'mode': mode,
                        }
                    )

        return resp

    def GetBars(self, token, symbol, interval, since, count):
        resp = self._req(
            sub_url='Instruments/GetBars',
            data={
                'token': token,
                'symbol': symbol,
                'interval': interval,
                'since': since,
                'count': count,
            }
        )
        return resp

    def GetSymbols(self, token):
        resp = self._req(
            sub_url='Instruments/GetSymbols',
            data={
                'token': token,
            }
        )
        return resp

    def GetMyPotfolioData(self, token, mode, portfolio):
        resp = self._req(
            sub_url='HistoricalData/GetMyPortfolioData',
            data={
                'token': token,
                'mode': mode,
                'portfolio': portfolio,
            }
        )
        return resp

    def GetPortfolioList(self, token):
        resp = self._req(
            sub_url='AccountInformation/GetPortfolioList',
            data={
                'token': token,
            }
        )
        return resp

    def GetTrades(self, token, symbol, interval, count):
        resp = self._req(
            sub_url='Instruments/GetTrades',
            data={
                'token': token,
                'symbol': symbol,
                'from': interval,
                'count': count,
            }
        )
        return resp

    def AddTickHistory(self, token):
        resp = self._req(
            sub_url='Instruments/AddTickHistory',
            data={
                'token': token,
            }
        )
        return resp

    def ListenQuotes(self, token, symbol):
        resp = self._req(
            sub_url='Instruments/ListenQuotes',
            data={
                'token': token,
                'symbol': symbol,
            }
        )
        return resp

    def UpdateQuotes(self, token):
        resp = self._req(
            sub_url='Instruments/UpdateQuote',
            data={
                'token': token,
            }
        )
        return resp

    def CancelQuotes(self, ):  # Todo
        pass

    def ListenTicks(self, ):  # Todo
        pass

    def UpdateTicks(self, ):  # Todo
        pass

    def AddTick(self, token):
        resp = self._req(
            sub_url='Instruments/AddTick',
            data={
                'token': token,
            }
        )
        return resp

    def CancelTicks(self, ):  # Todo
        pass

    def ListenBidAsks(self, ):  # Todo
        pass

    def UpdateBidAsks(self, ):  # Todo
        pass

    def CancelBidAsks(self, ):  # Todo
        pass

    def ListenPortfolio(self, token, portfolio):
        resp = self._req(
            sub_url='AccountInformation/ListenPortfolio',
            data={
                'token': token,
                'portfolio': portfolio
            }
        )
        return resp

    def PlaceOrder(self, token, portfolio, symbol, action, type, validity, price, amount, stop, cookie):
        resp = self._req(
            sub_url='Order/Place',
            data={
                'token': token,
                'portfolio': portfolio,
                'symbol': symbol,
                'action': action,
                'type': type,
                'validity': validity,
                'price': price,
                'amount': amount,
                'stop': stop,
                'cookie': cookie
            }
        )
        return resp

    def MoveOrder(self, token, portfolio, symbol, orderid, targetprice):
        resp = self._req(
            sub_url='Order/Move',
            data={
                'token': token,
                'portfolio': portfolio,
                'symbol': symbol,
                'orderid': orderid,
                'targetprice': targetprice
            }
        )
        return resp

    def CancelOrder(self, token, portfolio, symbol, orderid):
        resp = self._req(
            sub_url='Order/Cancel',
            data={
                'token': token,
                'portfolio': portfolio,
                'symbol': symbol,
                'orderid': orderid,
            }
        )
        return resp

    def UpdateOrder(self, token):
        resp = self._req(
            sub_url='AccountInformation/UpdateOrder',
            data={
                'token': token,
            }
        )
        return resp

    def UpdatePosition(self, token):
        resp = self._req(
            sub_url='AccountInformation/UpdatePosition',
            data={
                'token': token,
            }
        )
        return resp

    def AddTrade(self, token):
        resp = self._req(
            sub_url='AccountInformation/AddTrade',
            data={
                'token': token,
            }
        )
        return resp

    def SetPortfolio(self, token):
        resp = self._req(
            sub_url='AccountInformation/SetPortfolio',
            data={
                'token': token,
            }
        )
        return resp

    def CancelPortfolio(self, token, portfolio):
        resp = self._req(
            sub_url='AccountInformation/CancelPortfolio',
            data={
                'token': token,
                'portfolio': portfolio
            }
        )
        return resp

    def Disconnected(self, login, password, token):
        resp = self._req(
            sub_url='AccountInformation/CancelPortfolio',
            data={
                'login': login,
                'password': password,
                'token': token
            }
        )
        return resp



if __name__ == '__main__':
    api = Api(url="fdfdfd", port=5000)