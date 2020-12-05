import requests
import typing as t


# http://85.143.79.6:5001

class Api:

    def __init__(self, host: str, port: t.Union[int, str], ssh=False) -> None:

        if port:
            self._host_url = f"{'https://' if ssh else 'http://'}{host}"
            if port:
                self._host_url += f":{port}"

    def _req_method(self, method_url: str, method_data: t.Optional[t.Dict] = None) -> requests.Response:

        resp = requests.post(
            f'{self._host_url}/{method_url}',
            json=method_data,
            headers={'Content-Type': 'application/json'}
        )
        return resp

    def Connect(self, login, password, token, mode):
        resp = self._req_method(
                        'Auth/Connected',
                        method_data={
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
    api = Api(host="fdfdfd", port=5000)