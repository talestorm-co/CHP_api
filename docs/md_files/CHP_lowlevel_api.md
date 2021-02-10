# [🏠 Home](../../README.md)

# Lowlevel api for ITI invest

Оглавление:
 - [Конструктор](###Конструктор)
 - [Connected](###Connected)
 - [Reconnection](###Reconnection)
 - [Disconnected](###Disconnected)
 - [GetBars](###GetBars)
 - [GetSymbols](###GetSymbols)
 - [GetMyPortfolioData](###GetMyPortfolioData)
 - [GetPortfolioList](###GetPortfolioList)
 - [GetTrades](###GetTrades)
 - [ListenQuotes](###ListenQuotes)
 - [UpdateQuote](###UpdateQuote)
 - [CancelQuotes](###CancelQuotes)
 - [ListenTicks](###ListenTicks)
 - [AddTick](###AddTick)
 - [CancelTicks](###CancelTicks)
 - [ListenBidAsks](###ListenBidAsks)
 - [UpdateBidAsk](###UpdateBidAsk)
 - [CancelBidAsks](###CancelBidAsks)
 - [ListenPortfolio](###ListenPortfolio)
 - [PlaceOrder](###PlaceOrder)
 - [MoveOrder](###MoveOrder)
 - [](###)
 - [](###)
 - [](###)
 - [](###)
 - [](###)
 - [](###)
 - [](###)
 - [](###)
 - [](###)
 - [](###)
 - [](###)
 - [](###)
 - [](###)

---

# class Api

### Конструктор

Инициализирует объект, не выполняя запросов.
Заполняется URL сервера

#### Параметры:
 - host: str - Хост сервера
 - port: [str | int] - Порт сервера
 - ssh: bool (default=False) - подключаться ли по https

```python
from CHP_api.CHP_lowlevel_api import Api

api = Api(host='server_host', port='server_port')

```

## Методы

### Connected

<https://github.com/talestorm-com/CHP_Rest#connected>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Auth/Connected
Все переданные параметры формируются в json

#### Параметры:
 - login: str - Логин на ITI Capital
 - password: str - Пароль на ITI Capital
 - token: str - Токен доступа сервера
 - mode: int - Тип подключения [0 - demo | 1 - real connection] **(Не используется)**

#### Возвращает 

Объект Response из пакета requests 

```python
api.Connected(login='user_login', password='user_password', token='user_token')
```

### Reconnection

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Auth/Reconnection
Все переданные параметры формируются в json

#### Параметры:
 - login: str - Логин на ITI Capital
 - password: str - Пароль на ITI Capital
 - token: str - Токен доступа сервера
 - mode: int - Тип подключения [0 - demo | 1 - real connection] **(Не используется)**

#### Возвращает 

Объект Response из пакета requests 

```python
api.Reconnection(login='user_login', password='user_password', token='user_token')
```

### Disconnected

<https://github.com/talestorm-com/CHP_Rest#disconnected>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Auth/Disconnected
Все переданные параметры формируются в json

#### Параметры:
 - login: str - Логин на ITI Capital
 - password: str - Пароль на ITI Capital
 - token: str - Токен доступа сервера

#### Возвращает 

Объект Response из пакета requests 

```python
api.Disconnected(login='user_login', password='user_password', token='user_token')
```

### GetBars

<https://github.com/talestorm-com/CHP_Rest#getbars>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Instruments/GetBars
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера
 - since: str - Дата начала значений 
 - interval: int - Интервал времени ([Из перечисленных](https://github.com/talestorm-com/CHP_Rest#barinterval))
 - symbol: str - Короткое имя котировки
 - count: int - Количество "столбцов" 

#### Возвращает 

Объект Response из пакета requests 

```python
api.GetBars(token='user_token', since="2020-10-10T10:10:10.000", interval=6, symbol="GAZP", count=10)
```

### GetSymbols

<https://github.com/talestorm-com/CHP_Rest#getsymbols>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Instruments/GetSymbols
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера

#### Возвращает 

Объект Response из пакета requests 

```python
api.GetSymbols(token='user_token')
```



### GetMyPortfolioData

<https://github.com/talestorm-com/CHP_Rest#getmyportfoliodata>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: HistoricalData/GetMyPortfolioData
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера
 - mode: int - Тип приложения [1 - Active | 2 - All]
 - portfolio: str - имя портфеля на "трейдинг" платформе

#### Возвращает 

Объект Response из пакета requests 

```python
api.GetMyPortfolioData(token='user_token', mode=2, portfolio="ST123456-MO-01")
```


№№№

### GetPortfolioList

<https://github.com/talestorm-com/CHP_Rest#getportfoliolist>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: AccountInformation/GetPortfolioList
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера

#### Возвращает 

Объект Response из пакета requests 

```python
api.GetPortfolioList(token='user_token')
```

### GetTrades

<https://github.com/talestorm-com/CHP_Rest#gettrades>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Instruments/GetTrades
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера
 - since: str - Дата начала значений
 - symbol: str - Короткое имя котировки
 - count: int - Количество трейдов 

#### Возвращает 

Объект Response из пакета requests 

```python
api.GetTrades(token='user_token', since="2020-10-10T10:10:10.000", symbol="GAZP", count=10)
```


### ListenQuotes

<https://github.com/talestorm-com/CHP_Rest#listencancel>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Instruments/ListenQuotes
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера
 - symbol: str - Короткое имя котировки

#### Возвращает 

Объект Response из пакета requests 

```python
api.ListenQuotes(token='user_token', symbol="GAZP")
```

### UpdateQuote

<https://github.com/talestorm-com/CHP_Rest#updatequote>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Instruments/UpdateQuote
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера

#### Возвращает 

Объект Response из пакета requests 

```python
api.UpdateQuote(token='user_token')
```

### CancelQuotes

<https://github.com/talestorm-com/CHP_Rest#listencancel>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Instruments/CancelQuotes
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера
 - symbol: str - Короткое имя котировки

#### Возвращает 

Объект Response из пакета requests 

```python
api.CancelQuotes(token='user_token', symbol="GAZP")
```

### ListenTicks

<https://github.com/talestorm-com/CHP_Rest#listencancel>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Instruments/ListenTicks
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера
 - symbol: str - Короткое имя котировки

#### Возвращает 

Объект Response из пакета requests 

```python
api.ListenTicks(token='user_token', symbol="GAZP")
```

### AddTick

<https://github.com/talestorm-com/CHP_Rest#addtick>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Instruments/AddTick
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера

#### Возвращает 

Объект Response из пакета requests 

```python
api.AddTick(token='user_token')
```

### CancelTicks

<https://github.com/talestorm-com/CHP_Rest#listencancel>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Instruments/CancelTicks
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера
 - symbol: str - Короткое имя котировки

#### Возвращает 

Объект Response из пакета requests 

```python
api.CancelTicks(token='user_token', symbol="GAZP")
```

### ListenBidAsks

<https://github.com/talestorm-com/CHP_Rest#listencancel>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Instruments/ListenBidAsks
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера
 - symbol: str - Короткое имя котировки

#### Возвращает 

Объект Response из пакета requests 

```python
api.ListenBidAsks(token='user_token', symbol="GAZP")
```

### UpdateBidAsk

<https://github.com/talestorm-com/CHP_Rest#updatebidask>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Instruments/UpdateBidAsk
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера

#### Возвращает 

Объект Response из пакета requests 

```python
api.UpdateBidAsk(token='user_token')
```

### CancelBidAsks

<https://github.com/talestorm-com/CHP_Rest#listencancel>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Instruments/CancelBidAsks
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера
 - symbol: str - Короткое имя котировки

#### Возвращает 

Объект Response из пакета requests 

```python
api.CancelBidAsks(token='user_token', symbol="GAZP")
```


### ListenPortfolio

<https://github.com/talestorm-com/CHP_Rest#listencancelportfolio>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: AccountInformation/ListenPortfolio
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера
 - portfolio: str - имя портфеля на "трейдинг" платформе

#### Возвращает 

Объект Response из пакета requests 

```python
api.ListenPortfolio(token='user_token', portfolio="ST123456-MO-01")
```

### PlaceOrder

<https://github.com/talestorm-com/CHP_Rest#placeorder>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Order/Place
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера
 - portfolio: str - имя портфеля на "трейдинг" платформе
 - symbol: str - Короткое имя котировки
 - action: int -  Вид торговой операции. Принимает следующие значения:
    - 1 – Купить
    - 2 – Продать
    - 3 – Открыть «короткую позицию»
    - 4 – Закрыть «короткую» позицию
 - type_: int – Тип приказа. Принимает следующие значения:
    - 1 – Приказ по рынку
    - 2 – Лимитированный приказ
    - 3 – Стоп приказ
    - 4 – приказ Стоп-Лимит
 - validity: int – Срок действия приказа. Принимает следующие значения:
    - 1 – День
    - 2 – GTC (до отмены, макс. 30 дней)
 - price: float – Цена Лимит - для заявок типа Лимит и Стоп-Лимит
    - 0 - для приказа: По рынку или Стоп
 - amount: float – Объем, ЦБ в приказе
 - stop: float – Цена СТОП для приказа типа Стоп и Стоп-Лимит
    - 0 - для приказа: По рынку или Лимит
 - cookie: float – Ваш уникальный номер приказа, используется для определения Id приказа через события OrderSucceeded/OrderFailed и UpdateOrders

#### Возвращает 

Объект Response из пакета requests 

```python
api.PlaceOrder(token="user_token",
            portfolio="ST123456-MO-01",
            symbol="GAZP",
            action=2,
            type_=1,
            price=12.2,
            amount=30,
            validity=1,
            stop=0.1,
            cookie=12
        )
```


### MoveOrder

<https://github.com/talestorm-com/CHP_Rest#listencancelportfolio>

Выполняет post запрос на CHP_Rest с вложением json из параметров
URN запроса: Order/Move
Все переданные параметры формируются в json

#### Параметры:
 - token: str - Токен доступа сервера
 - portfolio: str - имя портфеля на "трейдинг" платформе
 - symbol: str - 
 - irderid: str - 
 - targetprice: str

#### Возвращает 

Объект Response из пакета requests 

```python
api.MoveOrder(token='user_token', portfolio="ST123456-MO-01")
```



