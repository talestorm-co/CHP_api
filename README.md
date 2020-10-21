# CHP_api

Python module for interacting with ITI Capital.

## Installation:
`pip install git+https://github.com/talestorm-com/CHP_api.git`

## Example
```python
from CHP_api import CHP_api

api = CHP_api("localhost", 5000)
api.login("login", "password", "key")

api.get_bars("GAZP", 3, "2020-10-15", 2)

>>> [{'row': 0, 'nrows': 2, ... 'volume': 790760,'openInt': 0}, 
    {'row': 1, 'nrows': 2, ... 'volume': 439310, 'openInt': 0}]
```

## All Methods
[add_trade](#add_trade)  
[cancel_bid_ask](#cancel_bid_ask)  
[cancel_order](#cancel_order)  
[cancel_portfolio](#cancel_portfolio)  
[cancel_quotes](#cancel_quotes)  
[cancel_ticks](#cancel_ticks)  
[get_bars](#get_bars)  
[get_trades](#get_trades)  
[get_portfolio_list](#get_portfolio_list)  
[get_symbols](#get_symbols)  
[listen_bid_asks](#listen_bid_asks)  
[listen_quotes](#listen_quotes)  
[listen_ticks](#listen_ticks)  
[move_order](#move_order)  
[place_order](#place_order)  
[set_my_close_pos](#set_my_close_pos)  
[set_my_order](#set_my_order)  
[set_my_trade](#set_my_trade)  
[set_portfolio](#set_portfolio)  
[update_order](#update_order)  
[update_position](#update_position)  


### add_trade
Lorem huipsum

### cancel_bid_ask
Отменяет получение очереди заявок по инструменту.
* company - Код ЦБ из таблицы котировок TC Matrix (Пример Газпром: "GAZP", Яндекс: "YNDX")
```python
api.cancel_bid_ask(company)
```
### cancel_order
Отменяет приказ, выставленный на рынок методом PlaceOrder.
* company - Номер торгового счёта на торговой площадке.
* portfolio - Номер торгового счёта на торговой площадке.
* order_id - Id приказа на сервере котировок
```python
api.cancel_order(company, portfolio, order_id)
```
### cancel_portfolio      

### cancel_quotes
Отменяет получение очереди заявок по инструменту.
* company - Код ЦБ из таблицы котировок TC Matrix (Пример Газпром: "GAZP", Яндекс: "YNDX")
```python
api.cancel_quotes(company)
```
### cancel_ticks
Отменяет получение очереди заявок по инструменту.
* company - Код ЦБ из таблицы котировок TC Matrix (Пример Газпром: "GAZP", Яндекс: "YNDX")
```python
api.cancel_ticks(company)
```
### get_bars
- company - Код ЦБ из таблицы котировок TC Matrix (Пример Газпром: GAZP, Яндекс: YNDX)
- interval - Интервал времени.
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
- since - Дата начала запрашиваемого интервала
- count - Количество запрашиваемых интервалов. Если количество
    запрашиваемых интервалов положительно, сбор идет
    «назад» по времени в прошлое от указанной даты; если
    отрицательно – то «вперед»
```python
api.get_bars(company, interval, since, count)
```

### get_trades
Заказать тиковую историю сделок по инструменту. 
- company - Код ЦБ из таблицы котировок TC Matrix 
- count - Количество запрашиваемых тиков
- time_from - Время
```python
api.get_trades(symbol, count, time_from)
```

### get_portfolio_list
Заказать справочник доступных счетов.
```python
api.get_portfolio_list()
```

### get_symbols
Заказать справочник ЦБ.
```python
api.get_symbols()
```
### listen_bid_asks
Заказать очередь заявок по инструменту.
- company - Код ЦБ из таблицы котировок TC Matrix
```python
api.listen_bid_asks(company)
```
### listen_quotes
Заказать котировки по инструменту.
- company - Код ЦБ из таблицы котировок TC Matrix
```python
api.listen_quotes(company)
```
### listen_ticks
Заказать все сделки на рынке по инструменту.
- company - Код ЦБ из таблицы котировок TC Matrix
```python
api.listen_ticks(company)
```
### move_order
Заказать все сделки на рынке по инструменту.
- company - Код ЦБ из таблицы котировок TC Matrix (Пример Газпром: GAZP, Яндекс: YNDX)
- portfolio - Номер торгового счёта на торговой площадке.
- order_id - Номер заявки в ТС Matrix
- targetprice - Новая цена приказа
```python
api.move_order(company, portfolio, order_id, targetprice)
```
### place_order
Выставить приказ. 
- portfolio - Номер торгового счёта на торговой площадке.

- company - Код ЦБ из таблицы котировок TC Matrix

- action - Вид торговой операции. Принимает следующие значения:
            1 - Купить
            2 - Продать
            3 - Открыть «короткую позицию»
            4 – Закрыть «короткую» позицию
- _type - Тип приказа. Принимает следующие значения:
            1 - Приказ по рынку
            2 - Лимитированный приказ
            3 - Стоп приказ
            4 – приказ Стоп-Лимит

- validity - Срок действия приказа. Принимает следующие значения:
            1 - День
            2 – GTC (до отмены, макс. 30 дней)

- price - Цена Лимит - для заявок типа Лимит и Стоп-Лимит
            0 - для приказа: По рынку или Стоп

- amount - Объем, ЦБ в приказе

- stop - Цена СТОП для приказа типа Стоп и Стоп-Лимит
            0 - для приказа: По рынку или Лимит

- cookie - Ваш уникальный номер приказа, используется для
            определения Id приказа через события OrderSucceeded/
            OrderFailed и UpdateOrders
```python
api.place_order(portfolio, company, action, _type, validity, price, amount, stop, cookie):
```
### set_my_close_pos

### set_my_order

### set_my_trade

### set_portfolio
Изменился торговый счёт.
- portfolio - Номер торгового счёта на торговой площадке
```python
api.set_portfolio(portfolio)
```
### update_order

### update_position
