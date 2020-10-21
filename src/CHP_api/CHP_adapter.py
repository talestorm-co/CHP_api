import json
import requests


class CHP_api():
    def __init__(self, login, password, key):
        self.login = login
        self.password = password
        self.key = key

    def cancel_bid_ask(self):
        raise NotImplementedError()

    def cancel_order(self):
        raise NotImplementedError()

    def cancel_portfolio(self):
        raise NotImplementedError()

    def cancel_quotes(self):
        raise NotImplementedError()

    def cancel_ticks(self):
        raise NotImplementedError()

    def connected(self):
        raise NotImplementedError()

    def disconnected(self):
        raise NotImplementedError()

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
        raise NotImplementedError()

    def get_trades(self):
        raise NotImplementedError()

    def get_portfolio_list(self):
        raise NotImplementedError()

    def get_symbols(self):
        raise NotImplementedError()

    def is_connected(self):
        raise NotImplementedError()

    def listen_bid_asks(self):
        raise NotImplementedError()

    def listen_portfolio(self):
        raise NotImplementedError()

    def listen_quotes(self):
        raise NotImplementedError()

    def listen_ticks(self):
        raise NotImplementedError()

    def move_order(self):
        raise NotImplementedError()

    def place_order(self):
        raise NotImplementedError()

    # camelCase aliases
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
