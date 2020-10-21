import json
import requests
import functools
from typing import Optional, Union, Dict, Callable, List
from .CHPExceptions import LoginException


class CHP_api:
    user_login: Optional[str] = None
    password: Optional[str] = None
    key: Optional[str] = None

    def __init__(self, api_url: str, port: Optional[Union[str, int]] = None):
        """

        :param api_url: URL или IP сервера
        :param port: Порт сервера (опционально)
        """

        self.url = api_url
        if port:
            self.url += f":{port}"

    def login(self, user_login: str, password: str, key: str):
        """

        :param user_login: Логин пользователя
        :param password: Пароль пользователя
        :param key: Ключ пользователя
        """
        self.user_login = user_login
        self.password = password
        self.key = key

    @staticmethod
    def _login_required(func: Callable):
        """
            decorator who check what login, password and key are initialized
        """

        @functools.wraps(func)
        def _wrapper(self, *args, **kwargs):
            if not self.user_login or \
                    not self.password or \
                    not self.key:
                raise LoginException('Нет логина, пароля или ключа. выполните метод login.')
            return func(self, *args, **kwargs)

        return _wrapper

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

    @_login_required
    def get_bars(self, company: str, interval: int, since: str, count: int):
        """

        :param company: Код ЦБ из таблицы котировок TC Matrix (Пример Газпром: GAZP, Яндекс: YNDX)
        :param interval: Интервал времени.
            1 - минута,
            2 - 5 минут,
            3 - 10 минут,
            4 - 15 минут,
            5 - 30 минут,
            6 - час,
            7 - 2 часа,
            8 - 4 часа,
            9 - день,
            10 - неделя,
            11 - месяц,
            12 - квартал,
            13 - год
        :param since: Дата начала запрашиваемого интервала
        :param count: Количество запрашиваемых интервалов. Если количество
            запрашиваемых интервалов положительно, сбор идет
            «назад» по времени в прошлое от указанной даты; если
            отрицательно – то «вперед»
        :return:
        dict[str, str]
        """
        json_data = {"login": self.user_login, "password": self.password, "key": self.key, "symbol": company,
                     "interval": interval, "since": since, "count": count}
        resp = requests.post(f'http://{self.url}/api/instruments/getbars',
                             json=json_data,
                             headers={'Content-Type': 'application/json'})
        return json.loads(resp.text)

    def get_my_portfolio_data(self):
        raise NotImplementedError()

    @_login_required
    def get_trades(self, symbol: str, count: int, time_from: str):
        json_data = {"login": self.user_login, "password": self.password, "key": self.key, "symbol": symbol,
                     "count": count, "from": time_from}
        resp = requests.post(f'http://{self.url}/api/instruments/gettrade',
                             json=json_data,
                             headers={'Content-Type': 'application/json'})
        return json.loads(resp.text)

    @_login_required
    def get_portfolio_list(self):
        """
        Заказать справочник доступных счетов.
        :return:
        """
        my_data = {"login": self.user_login, "password": self.password, "key": "12345"}
        resp = requests.post(f'http://{self.url}/api/accountinformation/getprortfoliolist',
                             json=my_data,
                             headers={'Content-Type': 'application/json'})
        return json.loads(resp.text)

    @_login_required
    def get_symbols(self):
        """
        Заказать справочник ЦБ.
        :return:
        """
        json_data = {"login": self.user_login, "password": self.password, "key": self.key}
        resp = requests.post(f'http://{self.url}/api/instruments/getsymbols',
                             json=json_data,
                             headers={'Content-Type': 'application/json'})
        return json.loads(resp.text)

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

    @_login_required
    def set_portfolio(self, portfolio: str):
        my_data = {"login": self.user_login, "password": self.password, "key": "12345", "portfolio": portfolio}
        resp = requests.post(f'http://{self.url}/api/accountinformation/listenportfolio/setportfolio',
                             json=my_data,
                             headers={'Content-Type': 'application/json'})
        return json.loads(resp.text)

    def add_trade(self):
        raise NotImplementedError()

    def update_order(self):
        raise NotImplementedError()

    def update_position(self):
        raise NotImplementedError()

    def set_my_trade(self):
        raise NotImplementedError()

    def set_my_close_trade(self):
        raise NotImplementedError()

    def set_my_order(self):
        raise NotImplementedError()

    @_login_required
    def _test(self):
        return True

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
    setPortfolio = set_portfolio
