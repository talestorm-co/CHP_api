import requests, json


class CHP_api():
    def __init__(self, login, password, key):
        self.login = login
        self.password = password
        self.key = key

    def cancel_bid_ask(self):
        pass

    def cancel_order(self):
        pass

    def cancel_portfolio(self):
        pass

    def cancel_quotes(self):
        pass

    def cancel_ticks(self):
        pass

    def connected(self):
        pass

    def disconnected(self):
        pass

    def get_bars(self, company: str, interval: int, since: str, count: int) -> dict:
        """
        :param company: Код ЦБ из таблицы котировок TC Matrix
        :param interval: Интервал времени.
            1 - минута
            2 - 5 минут
            3 - 10 минут
            4 - 15 минут
            5 - 30 минут
            6 - час
            7 - 2 часа
            8 - 4 часа
            9 - день
            10 - неделя
            11 - месяц
            12 - квартал
            13 - год
        :param since: Дата начала запрашиваемого интервала
        :param count: Количество запрашиваемых интервалов. Если количество
            запрашиваемых интервалов положительно, сбор идет
            «назад» по времени в прошлое от указанной даты; если
            отрицательно – то «вперед»
        :return:
        """
        json_data = {"login": self.login, "password": self.password, "key": self.key, "symbol": company,
                     "interval": interval, "since": since, "count": count}
        resp = requests.post('http://localhost:5000/api/instruments/getbars', json=json_data,
                             headers={'Content-Type': 'application/json'})
        return json.loads(resp.text)

    def get_my_portfolio_data(self):
        pass

    def get_trades(self):
        pass

    def get_portfolio_list(self):
        pass

    def get_symbols(self):
        pass

    def is_connected(self):
        pass

    def listen_bid_asks(self):
        pass

    def listen_portfolio(self):
        pass

    def listen_quotes(self):
        pass

    def listen_ticks(self):
        pass

    def move_order(self):
        pass

    def place_order(self):
        pass



    ## aliases
    cancelBidAsk = cancel_bid_ask
    cancelOrder = cancel_order
    cancelPortfolio = cancel_portfolio
    cancelQuotes = cancel_quotes
    cancelTicks = cancel_ticks
    getBars = get_bars
    getMyPortfolioData = get_my_portfolio_data
    getTrades = get_trades
    getPortfolioList = get_portfolio_list
    getSymbols = get_symbols
    isConnected = is_connected
    listenBidAsks = listen_bid_asks
    listenPortfolio = listen_portfolio
    listenQuotes = listen_quotes
    listenTicks = listen_ticks
    moveOrder = move_order
    placeOrder = place_order