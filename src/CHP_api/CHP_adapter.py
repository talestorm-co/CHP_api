import json
import requests
import functools
import typing 
from .CHPExceptions import LoginException





class CHP_api:
    user_login: typing.Optional[str] = None
    password: typing.Optional[str] = None
    key: typing.Optional[str] = None

    def __init__(self, api_url: str, port: typing.Optional[typing.Union[str, int]] = None, *, enable_SSL: bool=False):
        """

        :param api_url: URL или IP сервера
        :param port: Порт сервера
        """

        self.url = f"{ 'https://' if enable_SSL else 'http://'}{api_url}"
        if port:
            self.url += f":{port}"

        self._user_data: typing.Dict[str, typing.Optional[str]] = {
            "login": None,
            "password": None,
            "key": None
        }

    def _get_json_data(self, spec_data: typing.Dict = {}) -> typing.Dict:
        return {**self._user_data, **spec_data}

    def _req(self, sub_url: str, data: typing.Dict = {}) -> requests.Response:

        json_data = self._get_json_data(data)
        
        resp = requests.post(
            f'{self.url}{sub_url}',
            json=json_data,
            headers={'Content-Type': 'application/json'}
        )
        return resp

    def login(self, user_login: str, password: str, key: str) -> None:
        """

        :param user_login: Логин пользователя
        :param password: Пароль пользователя
        :param key: Ключ пользователя
        """

        # self.user_login = user_login
        # self.password = password
        # self.key = key

        self._user_data = {
            "login": user_login,
            "password": password,
            "key": key
        }

    def _login_required(func: typing.Callable):
        """
            decorator who check what login, password and key are initialized
        """

        @functools.wraps(func)
        def _wrapper(self, *args, **kwargs):
            if not self._user_data['login']:
                raise LoginException('Нет логина. выполните метод login.')
            elif not self._user_data['password']:
                raise LoginException('Нет пароля. выполните метод login.')
            elif not self._user_data['key']:
                raise LoginException('Нет ключа. выполните метод login.')
            else:
                return func(self, *args, **kwargs)

        return _wrapper

    @_login_required
    def add_trade(self, portfolio: str):
        """
        Новая сделка
        :param portfolio: Номер торгового счёта на торговой площадке
        :return:
        """
        resp = self._req(
            sub_url='/api/accountinformation/listenportfolio/addtrade',
            data={"portfolio": portfolio}
        )

        return json.loads(resp.text)

    @_login_required
    def cancel_bid_ask(self, company: str):
        """
        Отменяет получение очереди заявок по инструменту.
        :param company: Код ЦБ из таблицы котировок TC Matrix (Пример Газпром: GAZP, Яндекс: YNDX)
        :return:
        """
        resp = self._req(
            sub_url='/api/instruments/cancelbidasks',
            data={"Symbol": company}
        )

        return json.loads(resp.text)

    @_login_required
    def cancel_order(self, company: str, portfolio: str, order_id: str):
        """
        Отменяет приказ, выставленный на рынок методом PlaceOrder.
        :param company: Код ЦБ из таблицы котировок TC Matrix (Пример Газпром: GAZP, Яндекс: YNDX)
        :param portfolio: Номер торгового счёта на торговой площадке.
        :param order_id: Id приказа на сервере котировок
        :return:
        """

        resp = self._req(
            sub_url='/api/order/cancel',
            data={
                "Symbol": company,
                "portfolio": portfolio,
                "orderid": order_id
            }
        )

        return json.loads(resp.text)

    @_login_required
    def cancel_portfolio(self, portfolio: str):
        """
        Отмена получения информации по счету
        :param portfolio: Номер торгового счёта на торговой площадке
        :return:
        """

        resp = self._req(
            sub_url='/api/accountinformation/listenportfolio/CancelPortfolio',
            data={"portfolio": portfolio}
        )

        return json.loads(resp.text)

    @_login_required
    def cancel_quotes(self, company: str):
        """
        Отменяет получение котировок по инструменту.
        :param company: Код ЦБ из таблицы котировок TC Matrix (Пример Газпром: GAZP, Яндекс: YNDX)
        :return:
        """

        resp = self._req(
            sub_url='/api/instruments/cancelquotes',
            data={"Symbol": company}
        )

        return json.loads(resp.text)

    @_login_required
    def cancel_ticks(self, company: str):
        """
        Отменяет получение всех сделок на рынке по инструменту.
        :param company: Код ЦБ из таблицы котировок TC Matrix (Пример Газпром: GAZP, Яндекс: YNDX)
        :return:
        """

        resp = self._req(
            sub_url='/api/instruments/cancelticks',
            data={"Symbol": company}
        )

        return json.loads(resp.text)

    @_login_required
    def get_bars(self, company: str, interval: int, since: str, count: int) -> typing.List[typing.Dict]:
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
        typing.List[Bar_t]
        """

        resp = self._req(
            sub_url='/api/instruments/getbars',
            data={
                "symbol": company,
                "interval": interval,
                "since": since,
                "count": count
            }
        )

        return json.loads(resp.text)

    @_login_required
    def get_trades(self, company: str, count: int, time_from: str):
        """
        Заказать тиковую историю сделок по инструменту.
        :param company: Код ЦБ из таблицы котировок TC Matrix
        :param count: Количество запрашиваемых тиков
        :param time_from: Время
        :return:
        """

        resp = self._req(
            sub_url='/api/instruments/gettrade',
            data={
                "symbol": company,
                "count": count,
                "from": time_from
            }
        )

        return json.loads(resp.text)

    @_login_required
    def get_portfolio_list(self):
        """
        Заказать справочник доступных счетов.
        :return:
        """

        resp = self._req(
            sub_url='/api/accountinformation/getprortfoliolist'
        )

        return json.loads(resp.text)

    @_login_required
    def get_symbols(self) -> typing.List[typing.Dict]:
        """
        Заказать справочник ЦБ.
        :return:
        """

        resp = self._req(
            sub_url='/api/instruments/getsymbols'
        )

        return json.loads(resp.text)

    @_login_required
    def listen_bid_asks(self, company: str):
        """
        Заказать очередь заявок по инструменту.
        :param company: Код ЦБ из таблицы котировок TC Matrix (Пример Газпром: GAZP, Яндекс: YNDX)
        :return:
        """

        resp = self._req(
            sub_url='/api/instruments/listenbidasks',
            data={"Symbol": company}
        )

        return json.loads(resp.text)

    @_login_required
    def listen_quotes(self, company: str):
        """
        Заказать котировки по инструменту.
        :param company: Код ЦБ из таблицы котировок TC Matrix (Пример Газпром: GAZP, Яндекс: YNDX)
        :return:
        """

        resp = self._req(
            sub_url='/api/instruments/listenquotes',
            data={"Symbol": company}
        )

        return json.loads(resp.text)

    @_login_required
    def listen_ticks(self, company: str):
        """
        Заказать все сделки на рынке по инструменту.
        :param company: Код ЦБ из таблицы котировок TC Matrix (Пример Газпром: GAZP, Яндекс: YNDX)
        :return:
        """

        resp = self._req(
            sub_url='/api/instruments/listenticks',
            data={"Symbol": company}
        )

        return json.loads(resp.text)

    @_login_required
    def move_order(self, company: str, portfolio: str, order_id: str, targetprice: float):
        """
        Заказать все сделки на рынке по инструменту.
        :param company: Код ЦБ из таблицы котировок TC Matrix (Пример Газпром: GAZP, Яндекс: YNDX)
        :param portfolio: Номер торгового счёта на торговой площадке.
        :param order_id: Номер заявки в ТС Matrix
        :param targetprice: Новая цена приказа
        :return:
        """

        resp = self._req(
            sub_url='/api/order/move',
            data={
                "portfolio": portfolio,
                "symbol": company,
                "orderid": order_id,
                "targetprice": targetprice
            }
        )

        return json.loads(resp.text)

    @_login_required
    def place_order(self, portfolio: str, company: str, action: int, _type: int,
                    validity: int, price: float, amount: float, stop: float, cookie: int):
        """
        Выставить приказ. 
        :param portfolio: Номер торгового счёта на торговой площадке.

        :param company: Код ЦБ из таблицы котировок TC Matrix

        :param action: Вид торговой операции. Принимает следующие значения:
                    1 - Купить
                    2 - Продать
                    3 - Открыть «короткую позицию»
                    4 – Закрыть «короткую» позицию
        :param _type: Тип приказа. Принимает следующие значения:
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

        resp = self._req(
            sub_url='/api/order/place',
            data={
                "portfolio": portfolio,
                "symbol": company,
                "action": action,
                "Type": _type,
                "validity": validity,
                "price": price,
                "amount": amount,
                "stop": stop,
                "cookie": cookie
            }
        )

        return json.loads(resp.text)

    @_login_required
    def set_my_close_pos(self, mode: int, portfolio: str):
        """
        Все закрытые позиции за текущую сессию
        Изменился торговый счёт.
        :param mode: 1 - Активные
                     2 - Все
        :param portfolio: Номер торгового счёта на торговой площадке
        :return:
        """

        resp = self._req(
            sub_url='/api/GetMyPortfolioData/SetMyClosePos',
            data={
                "portfolio": portfolio,
                "mode": mode
            }
        )

        return json.loads(resp.text)

    @_login_required
    def set_my_order(self, mode: int, portfolio: str):
        """
        Все приказы за текущую сессию
        :param mode: 1 - Активные
                     2 - Все
        :param portfolio: Номер торгового счёта на торговой площадке
        :return:
        """

        resp = self._req(
            sub_url='/api/GetMyPortfolioData/SetMyOrder',
            data={
                "portfolio": portfolio,
                "mode": mode
            }
        )

        return json.loads(resp.text)

    @_login_required
    def set_my_trade(self, mode: int, portfolio: str):
        """
        Все сделки за текущую сессию
        :param mode: 1 - Активные
                     2 - Все
        :param portfolio: Номер торгового счёта на торговой площадке
        :return:
        """

        resp = self._req(
            sub_url='/api/GetMyPortfolioData/SetMyTrade',
            data={
                "portfolio": portfolio,
                "mode": mode
            }
        )
        return json.loads(resp.text)

    @_login_required
    def set_portfolio(self, portfolio: str):
        """
        Изменился торговый счёт.
        :param portfolio: Номер торгового счёта на торговой площадке
        :return:
        """

        resp = self._req(
            sub_url='/api/accountinformation/listenportfolio/setportfolio',
            data={"portfolio": portfolio}
        )

        return json.loads(resp.text)

    @_login_required
    def update_order(self, portfolio: str):
        """
        Состояние приказа
        :param portfolio: Номер торгового счёта на торговой площадке
        :return:
        """

        resp = self._req(
            sub_url='/api/accountinformation/listenportfolio/UpdateOrder',
            data={"portfolio": portfolio}
        )

        return json.loads(resp.text)

    @_login_required
    def update_position(self, portfolio: str):
        """
        Изменилась позиция 
        :param portfolio: Номер торгового счёта на торговой площадке
        :return:
        """

        resp = self._req(
            sub_url='/api/accountinformation/listenportfolio/UpdatePosition',
            data={"portfolio": portfolio}
        )

        return json.loads(resp.text)

    # camelCase aliases
    addTrade = add_trade
    cancelBidAsk = cancel_bid_ask
    cancelOrder = cancel_order
    cancelPortfolio = cancel_portfolio
    cancelQuotes = cancel_quotes
    cancelTicks = cancel_ticks
    getBars = get_bars
    getTrades = get_trades
    getPortfolioList = get_portfolio_list
    getSymbols = get_symbols
    listenBidAsks = listen_bid_asks
    listenQuotes = listen_quotes
    listenTicks = listen_ticks
    moveOrder = move_order
    placeOrder = place_order
    setMyClosePos = set_my_close_pos
    setMyOrder = set_my_order
    setMyTrade = set_my_trade
    setPortfolio = set_portfolio
    updateOrder = update_order
    updatePosition = update_position
