# [🏠 Home](../../README.md)

# CHP_client

Документация с описанием и назначением методов [ITI invest](https://iticapital.ru/assets/files/software/SmartCOM_manual_4_0_upd.pdf) используемых здесь

### Info:

Данный класс является клиентом для работы с сервером. Внутри себя использует класс [Api](CHP_lowlevel_api.md)

Все методы за исключением <ins>[Connect](#Connect) | [Reconnect](#Reconnect) | [Disconnect](#Disconnect)  </ins> Возвращают из тела запроса поле data, **если**:
 1. Ответ от сервера успешно десериализован в JSON (сервер вернул валидный JSON)  
 2. У тела ответа от сервера (в JSON которое вернул сервер) есть поля *result* и *data*
 3. В поле result вернулось значение *True*

⚠️ Если **хотя бы одно** условие нарушено, класс выкинет исключения, основанные на [ChpError](#ChpError)

### User Guide:
Для работы необходимо установить пакет с github:

> `pip install git+https://github.com/talestorm-com/CHP_api.git`

После чего импортируем ChpClient:

```python
   >>> from CHP_api.CHP_client import ChpClient
   >>>
   >>> chp = ChpClient(
   ...    host='server_host',
   ...    post='server_port',
   ...    login='user_login',
   ...    password='user_password',
   ...    token='user_token')
   ...
   >>>
```

Подключаемся к серверу:

```python
    >>> chp.Connect()
    {"method": "Connected","result": true,"data": [{"token": "user_token","work": 0,"exchange": 1,"login": "user_login", "password": "user_password"}]}
    >>>
```

⚠️ После работы обязательно отключитесь от сервера:

```python
    >>> chp.Disconnect()
    # TODO: дописать
```




<a name="exceptions"></a>

### Отлов исключений:

ChpClient выкидывает 3 вида исключений, все они унаследованы от ChpError:

Сервер выкинул не json:
```python
   >>> from CHP_api.CHPExceptions import ChpError
   >>> from CHP_api.CHP_client import ChpClient
   >>>
   >>> chp = ChpClient(
   ...    host='server_host',
   ...    post='server_port',
   ...    login='user_login',
   ...    password='user_password',
   ...    token='user_token')
   ...
   >>> try:
   ...     connection_response = chp.Connect()
   ... except ChpError as e:
   ...     print(e)
   ...     print(e.resp_data)
   ...
    Пришел не json
    '<h1> это не json </h1>'
    >>>
```

В JSON нет поля `result` или `data`:
```python
   >>> from CHP_api.CHPExceptions import ChpError
   >>> from CHP_api.CHP_client import ChpClient
   >>>
   >>> chp = ChpClient(
   ...    host='server_host',
   ...    post='server_port',
   ...    login='user_login',
   ...    password='user_password',
   ...    token='user_token')
   ...
   >>> try:
   ...     connection_response = chp.Connect()
   ... except ChpError as e:
   ...     print(e)
   ...     print(e.resp_data)
   ...
    У ответа сервера нет поля result
    {'method':'Connected', 'data': {"token": "user_token","work": 0,"exchange": 1,"login": "user_login", "password": "user_password"}}
    >>>
```

В поле `result` false
```python
   >>> from CHP_api.CHPExceptions import ChpError
   >>> from CHP_api.CHP_client import ChpClient
   >>>
   >>> chp = ChpClient(
   ...    host='server_host',
   ...    post='server_port',
   ...    login='user_login',
   ...    password='user_password',
   ...    token='user_token')
   ...
   >>> try:
   ...     connection_response = chp.Connect()
   ... except ChpError as e:
   ...     print(e)
   ...     print(e.resp_data)
   "Error #3

    {
        "method": "Connected",
        "result": false,
        "reason": "Error #3",
        "additional": "Не удалось подключиться к серверу",
        "dataParam": [
            {
            "token": "user_token",
            "work": 0,
            "exchange": 1,
            "login": "user_login",
            "password": "user_password"
            }
        ],
        "dataError": [
            {
            "method": "Connect",
            "reason": "Error #2",
            "additional": "Вы уже авторизованы в системе."
            }
        ]
    }
    >>>
```


## Список методов и свойств:




|Свойство                                       |Тип      | Описание |
|-----------------------------------------------|---------|---------------------------------------------------------------------------------------------------------------|
|[Token](#Token)                                |str      |`readonly` свойство с информацией о токене (по какому токену отправляются запросы)                             |
|[Login](#Login)                                |str      |`readonly` свойство с информацией о логине (по какому логину отправляются запросы)                             |
|[Password](#Password)                          |str      |`readonly` свойство с информацией о пароле (по какому паролю отправляются запросы)                             |
|[Mode](#Mode)                                  |int      |`readonly` свойство с информацией о типе подключения [0 - demo \| 1 - production] ⚠️ Warn: не используется      |
|[listening_quotes](#listening_quotes)          |list[str]| свойство с информацией на какие "quotes" подписан клиент. ⚠️ Warn: может быть рассинхронизация с сервером     |
|[listening_ticks](#listening_ticks)            |list[str]| свойство с информацией на какие "ticks" подписан клиент. ⚠️ Warn: может быть рассинхронизация с сервером      |
|[listening_bid_ask](#listening_bid_ask)        |list[str]| свойство с информацией на какие "bid/ask" подписан клиент. ⚠️ Warn: может быть рассинхронизация с сервером    
|[listening_portfolios](#listening_portfolios)  |list[str]| свойство с информацией на какие "портфели" подписан клиент. ⚠️ Warn: может быть рассинхронизация с сервером   |

----

|Метод                                      | Описание          | Метод lowlevel_api    |
|-------------------------------------------|-------------------|-----------------------|
|[Конструктор](#Конструктор)                | Создаёт объект клиента, не отправляет никаких запросов на сервер  |                       |
|[Connect](#Connect)                        | Отправляет запрос с подключение к серверу                         |                       |
|[Reconnect](#Reconnect)                    | |
|[Disconnect](#Disconnect)                  | |
|[GetBars](#GetBars)                        | |
|[GetSymbols](#GetSymbols)                  | |
|[GetTrades](#GetTrades)                    | |
|[ListenQuotes](#ListenQuotes)              | |
|[UpdateQuote](#UpdateQuote)                | |
|[CancelQuotes](#CancelQuotes)              | |
|[ListenTicks](#ListenTicks)                | |
|[UpdateTicks](#UpdateTicks)                | |
|[CancelTicks](#CancelTicks)                | |
|[ListenBidAsks](#ListenBidAsks)            | |
|[UpdateBidAsks](#UpdateBidAsks)            | |
|[CancelBidAsks](#CancelBidAsks)            | |
|[GetMyPortfolioData](#GetMyPortfolioData)  | |
|[GetPortfolioList](#GetPortfolioList)      | |
|[ListenPortfolio](#ListenPortfolio)        | |
|[CancelPortfolio](#CancelPortfolio)        | |
|[PlaceOrder](#PlaceOrder)                  | |
|[MoveOrder](#MoveOrder)                    | |
|[CancelOrder](#CancelOrder)                | |
|[UpdateOrder](#UpdateOrder)                | |
|[UpdatePosition](#UpdatePosition)          | |
|[AddTrade](#AddTrade)                      | |
|[SetPortfolio](#SetPortfolio)              | |


### Token
Свойство экземпляра ChpClient с информацией о токене. 

Свойство только для чтения (его нельзя поменять после инициализации объекта)
```python
   >>> from CHP_api.CHP_client import ChpClient
   >>>
   >>> chp = ChpClient(
   ...    host='server_host',
   ...    post='server_port',
   ...    login='user_login',
   ...    password='user_password',
   ...    token='user_token')
   ...
   >>> chp.Token # Ok
   'user_token'
   >>>
   >>> chp.Token = '123' # Error
   >>>
   >>> del chp.Token # Error
   >>>
```

----
 
### Login
Свойство экземпляра ChpClient с информацией о логине. 

Свойство только для чтения (его нельзя поменять после инициализации объекта)
```python
   >>> from CHP_api.CHP_client import ChpClient
   >>>
   >>> chp = ChpClient(
   ...    host='server_host',
   ...    post='server_port',
   ...    login='user_login',
   ...    password='user_password',
   ...    token='user_token')
   ...
   >>> chp.Login # Ok
   'user_login'
   >>>
   >>> chp.Login = 'user_login_23' # Error
   >>>
   >>> del chp.Login # Error
   >>>
```

----
 
### Password
Свойство экземпляра ChpClient с информацией о пароле. 

Свойство только для чтения (его нельзя поменять после инициализации объекта)
```python
   >>> from CHP_api.CHP_client import ChpClient
   >>>
   >>> chp = ChpClient(
   ...    host='server_host',
   ...    post='server_port',
   ...    login='user_login',
   ...    password='user_password',
   ...    token='user_token')
   ...
   >>> chp.Password # Ok
   'user_password'
   >>>
   >>> chp.Password = 'new_user_password' # Error
   >>>
   >>> del chp.Password # Error
   >>>
```

----
 
### Mode
Свойство экземпляра ChpClient с информацией о типе подключения. 

Допутимые значения:
 - 0 (default): demo режим подключения
 - 1: production режим подключения

> ⚠️ Warn: Временно не используется, значение не влияет ни на что


Свойство только для чтений (нельзя поменять его после инициализации обьъекта)
```python
   >>> from CHP_api.CHP_client import ChpClient
   >>>
   >>> chp = ChpClient(
   ...    host='server_host',
   ...    post='server_port',
   ...    login='user_login',
   ...    password='user_password',
   ...    token='user_token')
   ...
   >>> chp.Mode # Ok
   0
   >>>
   >>> chp.Mode = 1 # Error
   >>>
   >>> del chp.Mode # Error
   >>>
```

----
 
### listening_quotes
Свойство экземпляра ChpClient с информацией о подписанных "quotes". 

Тип: список строк с именами quotes

Свойство имеет доступ к записи и удалению
```python
   >>> chp.listening_quotes
   ['SBER']
   >>>
```

Для записи тип передаваемого значения должен быть список

```python   
   >>> chp.listening_quotes = ['GAZP'] # Ok
   >>> chp.listening_quotes
   ['GAZP']
   >>>
   >>> chp.listening_quotes = 'GAZP' # Error
```

При удалении список очищается

```python   
   >>> chp.listening_quotes
   ['GAZP']
   >>>
   >>> del chp.listening_quotes
   >>>
   >>> chp.listening_quotes
   []
```

----
 

### listening_ticks
Свойство экземпляра ChpClient с информацией о подписанных "ticks". 

Тип: список строк с именами ticks

Свойство имеет доступ к записи и удалению
```python
   >>> chp.listening_ticks
   ['SBER']
   >>>
```

Для записи тип передаваемого значения должен быть список

```python   
   >>> chp.listening_ticks = ['GAZP'] # Ok
   >>> chp.listening_ticks
   ['GAZP']
   >>>
   >>> chp.listening_ticks = 'GAZP' # Error
```

При удалении список очищается

```python   
   >>> chp.listening_ticks
   ['GAZP']
   >>>
   >>> del chp.listening_ticks
   >>>
   >>> chp.listening_ticks
   []
```

----
 
### listening_bid_ask
Свойство экземпляра ChpClient с информацией о подписанных "bid\ask". 

Тип: список строк с именами bid\ask

Свойство имеет доступ к записи и удалению
```python
   >>> chp.listening_bid_ask
   ['SBER']
   >>>
```

Для записи тип передаваемого значения должен быть список

```python   
   >>> chp.listening_bid_ask = ['GAZP'] # Ok
   >>> chp.listening_bid_ask
   ['GAZP']
   >>>
   >>> chp.listening_bid_ask = 'GAZP' # Error
```

При удалении список очищается

```python   
   >>> chp.listening_bid_ask
   ['GAZP']
   >>>
   >>> del chp.listening_bid_ask
   >>>
   >>> chp.listening_bid_ask
   []
```

----
 
### listening_portfolios
Свойство экземпляра ChpClient с информацией о подписанных "portfolios". 

Тип: список строк с именами portfolios

Свойство имеет доступ к записи и удалению
```python
   >>> chp.listening_portfolios
   ['ST123456-MO-01']
   >>>
```

Для записи тип передаваемого значения должен быть список

```python   
   >>> chp.listening_portfolios = ['ST123456-MO-01'] # Ok
   >>> chp.listening_portfolios
   ['ST123456-MO-01']
   >>>
   >>> chp.listening_portfolios = 'ST123456-MO-01' # Error
```

При удалении список очищается

```python   
   >>> chp.listening_portfolios
   ['ST123456-MO-01']
   >>>
   >>> del chp.listening_portfolios
   >>>
   >>> chp.listening_portfolios
   []
```

----
 

### Конструктор

Параметры:
 - host: str - ip сервера для подключения
 - port: [str | int] - порт сервера для подключения
 - login: str - логин пользвателя в ITI Capital
 - password: str - пароль пользвателя в ITI Capital
 - token: str - **key-only** (можно передать только по ключу `token=''`. Токен подключеничения к серверу) 
 - mode: int - **key-only** (можно передать только по ключу `mode=0` (default = 0).Тип подключения к серверу [0 - demo | 1 - production]. ⚠️ Warn: Временно не используется, значение не влияет ни на что

```python
   >>> from CHP_api.CHP_client import ChpClient
   >>>
   >>> chp = ChpClient(             # Ok
   ...    host='server_host',
   ...    post='server_port',
   ...    login='user_login',
   ...    password='user_password',
   ...    token='user_token') 
   ...
   >>>
   >>> chp = ChpClient(             # Ok
   ...    'server_host',
   ...    'server_port',
   ...    'user_login',
   ...    'user_password',
   ...    token='user_token') 
   ...
   >>>
   >>> chp = ChpClient(             # Error
   ...    'server_host',
   ...    'server_port',
   ...    'user_login',
   ...    'user_password',
   ...    'user_token')
   ...
   >>>
```

----
 
### Connect

Параметры:
   - нет

Возвращает весь ответ от сервера, при удачном вызове, иначе выкидывает исключение [ChpError](#exceptions)

----
 
### Reconnect

Параметры:
   - нет

Возвращает весь ответ от сервера, при удачном вызове, иначе выкидывает исключение [ChpError](#exceptions)

----
 
### Disconnect

Параметры:
   - нет

Возвращает весь ответ от сервера, при удачном вызове, иначе выкидывает исключение [ChpError](#exceptions)


----
 
### GetBars

Параметры:
 - since: str - Дата начала значений (в формате "YYYY-MM-DDThh:mm:ss.000")
 - interval: int - Интервал времени
   * 1 Мин : `1`
   * 5 Мин : `2`
   * 10 Мин : `3`
   * 15 Мин : `4`
   * 30 Мин : `5`
   * 60 Мин : `6`
   * 2 Часа : `7`
   * 4 Часа : `8`
   * День : `9`
   * Неделя : `10`
   * Месяц : `11`
   * Квартал : `12`
   * Год : `13`

 - symbol: str - Короткое имя котировки
 - count: int - Количество "столбцов"

Возвращает в **случае успеха**:
    Список баров по указаным условиям

Иначе выкидывает исключение [ChpError](#exceptions)



----
 
### GetSymbols
 
Параметры:
   - нет

Возвращает в **случае успеха**:
   Список всех возможных имён котировок 

Иначе выкидывает исключение [ChpError](#exceptions)


----
 
### GetTrades

Параметры:
 - since: str - Дата начала значений (в формате "YYYY-MM-DDThh:mm:ss.000")
 - symbol: str - Короткое имя котировки
 - count: int - Количество трейдов


Возвращает в **случае успеха**:
    Список трейдов по указаным условиям

Иначе выкидывает исключение [ChpError](#exceptions)

----
 
### ListenQuotes

Параметры:
 - symbols - имя или список котировок для подписки
   * list[str] - список нескольких котировок (Пример: ['SBER', 'GAZP'])
   * str - одна котировка для подписки (Пример: 'SBER')


Возвращает в **случае успеха**:
   словарь в формате {'symbol': 'ответ сервера на подписку на эту "quotes"'}
   > если в ответе на подписку на котировку в поле result было True, она добавлена в [listening_quotes](#listening_quotes)
   > если в ответе на подписку на котировку в поле result было False или поля result не было, она не добавлена в [listening_quotes](#listening_quotes)

Выкидывает исключение [ChpError](#exceptions) если результат не приводится в JSON

```python
   >>> chp.ListenQuotes('SBER') # Ok
   {'SBER': {"""Полный ответ сервера на подписку от SBER"""...}}
   >>> """
   ... Например:
   ...     Ошибка
   ...      {'SBER': {'additional': 'Ошибка ListenQuotes',
   ...    'dataParam': [{'symbol': 'SBER', 'token': '16'}],
   ...    'errorData': [{'additional': 'Подписка оформлена.',
   ...                   'message': 'Подписка на SBER уже оформлена.',
   ...                   'method': 'ListenQuotes',
   ...                   'reason': 'Error #20'}],
   ...    'method': 'ListenQuotes',
   ...    'reason': 'Error #12',
   ...    'result': False}}
   ... """
   >>> """
   ... Например:
   ...     Ok
   ...      {'GAZP': {'data': [{'description': 'Подписка на GAZP успешно оформлена'}],
   ...    'method': 'ListenQuotes',
   ...    'result': True}}
   ... """
   
   >>> chp.ListenQuotes(['SBER', 'GAZP']) # Ok
   {'SBER': {"""Полный ответ сервера на подписку от SBER"""...}, 'GAZP': {"""Полный ответ сервера на подписку от GAZP"""...} }
   >>>

```

----
 

### UpdateQuote
 
Параметры:
   - нет

Возвращает в **случае успеха**:
   Информацию по всем подписаным котировкам
   > Поле `data` из ответа от сервера

Выкидывает исключение [ChpError](#exceptions) если:
   - результат не приводится в JSON
   - в поле `result` - False
   - нет поля `result` или `data`


----
 

### CancelQuotes

Параметры:
 - symbols - пустое или имя/список котировок для подписки
   * пустое (не переданы параметры) - отправит запрос на отписку от всех котировак из [listening_quotes](#listening_quotes)
   * list[str] - список нескольких котировок (Пример: ['SBER', 'GAZP'])
   * str - одна котировка для подписки (Пример: 'SBER')


Возвращает в **случае успеха**:
   словарь в формате {'symbol': 'ответ сервера на подписку на эту "quotes"'}
   > если в ответе на подписку на котировку в поле result было True, она удалена из [listening_quotes](#listening_quotes)

Выкидывает исключение [ChpError](#exceptions) если результат не приводится в JSON

```python
   >>> chp.CancelQuotes('SBER') # Ok
   {'SBER': {"""Полный ответ сервера на отписку от SBER"""...}}
   >>>
   >>> chp.CancelQuotes(['SBER', 'GAZP']) # Ok
   {'SBER': {"""Полный ответ сервера на отписку от SBER"""...}, 'GAZP': {"""Полный ответ сервера на отписку от GAZP"""...} }
   >>>
   >>> chp.CancelQuotes() # OK  #Note отписка от всего что было в listening_quotes
   {'котировка': {'ответ сервера'...}}
   >>>
```

----
 

### ListenTicks

Аналогично [ListenQuotes](#ListenQuotes)

----
 
### UpdateTicks

Аналогично [UpdateQuote](#UpdateQuote)

----
 
### CancelTicks

Аналогично [CancelQuotes](#CancelQuotes)

----
 

### ListenBidAsks

Аналогично [ListenQuotes](#ListenQuotes)

----
 
### UpdateBidAsks

Аналогично [UpdateQuote](#UpdateQuote)

----
 
### CancelBidAsks

Аналогично [CancelQuotes](#CancelQuotes)

----

### GetMyPortfolioData

Параметры:
 - portfolio: str - имя портфеля на "трейдинг" платформе
 - mode: int - Тип приложения [1 - Active | 2 - All]

Возвращает в **случае успеха**:
   поле `data` ответа от сервера

Иначе выкидывает исключение [ChpError](#exceptions)

----


### GetPortfolioList

Параметры:
 - нет

Возвращает в **случае успеха**:
   поле `data` ответа от сервера

Иначе выкидывает исключение [ChpError](#exceptions)

----

### ListenPortfolio

Аналогично [ListenQuotes](#ListenQuotes)

----

### CancelPortfolio

Аналогично [CancelQuotes](#CancelQuotes)

----

### PlaceOrder

Параметры:
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
 - amount: int – Объем, ЦБ в приказе
 - stop: float – Цена СТОП для приказа типа Стоп или Стоп-Лимит
    - 0 - для приказа: По рынку или Лимит
 - cookie: int – Ваш уникальный номер приказа, используется для определения Id приказа через события OrderSucceeded/OrderFailed и UpdateOrders

Возвращает в **случае успеха**:
   Информацию по всем подписаным котировкам
   > Поле `data` из ответа от сервера

Выкидывает исключение [ChpError](#exceptions) если:
   - результат не приводится в JSON
   - в поле `result` - False
   - нет поля `result` или `data`
 
----


### MoveOrder

Параметры:
 - portfolio: str - Имя портфеля на "трейдинг" платформе
 - symbol: str - Короткое имя котировки
 - orderid: str - Номер приказа на сервере котировок.
 - targetprice: float - Новая цена приказа. Тип данных float

Возвращает в **случае успеха**:
   Информацию по всем подписаным котировкам
   > Поле `data` из ответа от сервера

Выкидывает исключение [ChpError](#exceptions) если:
   - результат не приводится в JSON
   - в поле `result` - False
   - нет поля `result` или `data`
 
----


### CancelOrder

Параметры:
 - portfolio: str - Имя портфеля на "трейдинг" платформе
 - symbol: str - Короткое имя котировки
 - orderid: str - Номер приказа на сервере котировок.

Возвращает в **случае успеха**:
   Информацию по всем подписаным котировкам
   > Поле `data` из ответа от сервера

Выкидывает исключение [ChpError](#exceptions) если:
   - результат не приводится в JSON
   - в поле `result` - False
   - нет поля `result` или `data`
 
----

### UpdateOrder

Параметры:
 - нет

Возвращает в **случае успеха**:
   Информацию по всем подписаным котировкам
   > Поле `data` из ответа от сервера

Выкидывает исключение [ChpError](#exceptions) если:
   - результат не приводится в JSON
   - в поле `result` - False
   - нет поля `result` или `data`
 
----

### UpdatePosition

Параметры:
 - нет

Возвращает в **случае успеха**:
   Информацию по всем подписаным котировкам
   > Поле `data` из ответа от сервера

Выкидывает исключение [ChpError](#exceptions) если:
   - результат не приводится в JSON
   - в поле `result` - False
   - нет поля `result` или `data`
 
----

### AddTrade

Параметры:
 - нет

Возвращает в **случае успеха**:
   Информацию по всем подписаным котировкам
   > Поле `data` из ответа от сервера

Выкидывает исключение [ChpError](#exceptions) если:
   - результат не приводится в JSON
   - в поле `result` - False
   - нет поля `result` или `data`
 
----

### SetPortfolio

Параметры:
 - нет

Возвращает в **случае успеха**:
   Информацию по всем подписаным котировкам
   > Поле `data` из ответа от сервера

Выкидывает исключение [ChpError](#exceptions) если:
   - результат не приводится в JSON
   - в поле `result` - False
   - нет поля `result` или `data`
 
----

