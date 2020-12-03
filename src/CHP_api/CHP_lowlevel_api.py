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

    def GetBars(self, ):  # Todo
        pass

    def GetSymbols(self, ):  # Todo
        pass

    def GetMyPotfolioData(self, ):  # Todo
        pass

    def GetPortfolioList(self, ):  # Todo
        pass

    def GetTrades(self, ):  # Todo
        pass

    def AddTickHistory(self, ):  # Todo
        pass

    def ListenQuotes(self, ):  # Todo
        pass

    def UpdateQuotes(self, ):  # Todo
        pass

    def CancelQuotes(self, ):  # Todo
        pass

    def ListenTicks(self, ):  # Todo
        pass

    def UpdateTicks(self, ):  # Todo
        pass

    def AddTick(self, ):  # Todo
        pass

    def CancelTicks(self, ):  # Todo
        pass

    def ListenBidAsks(self, ):  # Todo
        pass

    def UpdateBidAsks(self, ):  # Todo
        pass

    def CancelBidAsks(self, ):  # Todo
        pass

    def ListenPortfolio(self, ):  # Todo
        pass

    def PlaceOrder(self, ):  # Todo
        pass

    def MoveOrder(self, ):  # Todo
        pass

    def CancelOrder(self, ):  # Todo
        pass

    def UpdateOrder(self, ):  # Todo
        pass

    def UpdatePosition(self, ):  # Todo
        pass

    def AddTrade(self, ):  # Todo
        pass

    def SetPortfolio(self, ):  # Todo
        pass

    def CancelPortfolio(self, ):  # Todo
        pass

    def Disconnected(self, ): # Todo
        pass



if __name__ == '__main__':
    api = Api(url="fdfdfd", port=5000)