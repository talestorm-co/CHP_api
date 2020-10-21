# CHP_api
Python module for interacting with ITI Capital.

## Usage
Required parameters:
- [Authorization in the system](#Authorization): Required parameters for making API requests.

Available request:
- [cancel_order](#CancelOrder): Cancels an order placed on the market using the PlaceOrder method.
- [Mmove_order](#MoveOrder): Sets a new price for the order, RTS.
- [place_order](#PlaceOrder): Submits a new order to the exchange.
- [GetSymbols](#GetSymbols): Order a reference book of the Central Bank.
- [ListenQuotes](#ListenQuotes): Subscribe to receive quotes.
- [CancelQuotes](#CancelQuotes): Cancellation of receiving quotes.
- [ListenTicks](#ListenTicks): Subscribe to receive all deals.
- [CancelTicks](#CancelTicks): Canceling the receipt of all trades.
- [ListenBidAsks](#ListenBidAsks): Order a queue of applications.
- [CancelBidAsks](#CancelBidAsks): Cancels receiving a queue of applications.
- [GetTrades](#GetTrades): Request the history of all transactions.
- [GetBars](#GetBars): Request history.
- [GetPrortfolioList](#GetPrortfolioList): Request a list of available accounts.
- [SetPortfolio](#SetPortfolio): Information on funds.
- [AddTrade](#AddTrade): New deal.
- [UpdateOrder](#UpdateOrder): The order has changed.
- [UpdatePosition](#UpdatePosition): Position has changed.
- [CancelPortfolio](#CancelPortfolio): Canceling the receipt of account information.
- [SetMyTrade](#SetMyTrade): All transactions for the current session.
- [SetMyClosePos](#SetMyClosePos): All closed positions for the current session.
- [SetMyOrder](#SetMyOrder): All orders for the current session.

### Authorization
Options:
* `Login`: Your login from the ITI Capital system.
* `Password`: Your password from the ITI Capital system.
* `Key`: Your API key to use the system.

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey"
}
```
If authorization is not successful, following message will appear:
```json5
[{
error: "Error connected"
}]
```


### PlaceOrder
Used in conjunction with [Authorization](#Authorization)

URL : `https://localhost:5001/api/order/place`
* `Portfolio`: Trading account number on the trading floor.
* `Symbol`: Central Bank code from the TC Matrix quotes table.
* `Action`: Trade operation type. It takes the following values: [OrderAction](#OrderAction)
* `Type`: Order type. It takes the following values: [OrderType](#OrderType)
* `Validity`: The validity period of the order. It takes the following values: [OrderValidity](#OrderValidity)
* `Price`: Price Limit - for orders of the Limit and Stop-Limit types. Price 0 - for an order: By Market or Stop. The data type is Double.
* `Amount`: Volume, Bank Center in the order. The data type is Double.
* `Stop`: Stop price - for a Stop and Stop Limit order. Price 0 - for an order: By market or Limit. The data type is Double.
* `Cookie`: Your unique order number is used to determine the Id of the order. The data type is Integer

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey",
  portfolio: "testPortfolio",
  symbol: "GAZP",
  action: 1,
  Type: 1,
  validity: 1,
  price: 100.25,
  amount: 21.6,
  stop: 110.76,
  cookie: 80
}
```

Result if succes:
```json5
[{
  Cookie:80,
  Orderid: "GAZP"
}]
```
Result if failure:
```json5
[{
  Cookie:80,
  Orderid: "GAZP",
  reason: "reason"
}]
```

### MoveOrder
Used in conjunction with [Authorization](#Authorization)

URL : `https://localhost:5001/api/order/move`

Options:
* `Portfolio`: Trading account number on the trading floor.
* `Symbol`: Central Bank code from SmartTrade quotes table.
* `OrderId`: Application number in TS Matrix.
* `TargetPrice`: New order price. The data type is Double.

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey",
  portfolio: "testPortfolio",
  symbol: "testSymbol",
  orderid: "testOrderId",
  targetprice: 100.25
}
```
Result if succes:
```json5
[{
  OrderId:"testOrderId",
  Result: true
}]
```
Result if failure:
```json5
[{
  OrderId:"testOrderId",
  Result: false
}]
```

### CancelOrder
Used in conjunction with [Authorization](#Authorization)

URL : `https://localhost:5001/api/order/cancel`

Options:
* `Portfolio`: Trading account number on the trading floor.
* `Symbol`: Central Bank code from the TC Matrix quotes table.
* `OrderId`: Id of the order on the quote server.

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey",
  portfolio: "testPortfolio",
  symbol: "testSymbol",
  orderid: "testOrderId"
}
```
Result if succes:
```json5
[{
  OrderId:"testOrderId",
  Result: true
}]
```
Result if failure:
```json5
[{
  OrderId:"testOrderId",
  Result: false
}]
```

### GetSymbols
Used in conjunction with [Authorization](#Authorization)

URL : `https://localhost:5001/api/instruments/getsymbols`

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey"
}
```
Result:
```json5
[{
  row: 0,
  nrows: 46618,
  symbol: "6A.CME.H2015",
  short_name: "6A.CME-03.15",
  long_name: "6A",
  type: "FUT",
  decimals: 4,
  lot_size: 1,
  punkt: 0.0001,
  step: 0.0001,
  sec_ext_id: null,
  sec_exch_name: "CME",
  expiryDate: "2015-03-19T00:00:00",
  days_before_expiry: 0,
  strike: 0
}]
```

### ListenQuotes
Used in conjunction with [Authorization](#Authorization)

URL : `https://localhost:5001/api/instruments/listenquotes`

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey",
  Symbol:"GAZP"
}
```

Result:
```json5
[
    {
        symbol: "GAZP",
        datetime: "2020-10-16T23:49:55",
        open: 167.31,
        high: 167.31,
        low: 163.46,
        close: 167.16,
        last: 163.93,
        volume: 51565250,
        size: 49,
        bid: 163.9,
        ask: 163.92000000000002,
        bidSize: 800411,
        askSize: 922633,
        open_Int: 0,
        go_Buy: 0,
        go_Sell: 0,
        go_Base: 0,
        go_Base_Backed: 0,
        high_Limit: 0,
        low_Limit: 0,
        trading_Status: 0,
        volat: 0,
        theor_Price: 0,
        step_Price: 1
    }
]
```
### CancelQuotes

Used in conjunction with [Authorization](#Authorization)

URL : `https://localhost:5001/api/instruments/cancelquotes`

Options:
* `Symbol`: Central Bank code from the TC Matrix quotes table.

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey",
  Symbol:"GAZP"
}
```

Result:
```json5
[{
Result: "Запрос отправлен"
}]
```
### ListenTicks
Used in conjunction with [Authorization](#Authorization)

URL : `https://localhost:5001/api/instruments/listenticks`

Options:
* `Symbol`: Central Bank code from the TC Matrix quotes table.

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey",
  Symbol:"GAZP"
}
```

Result:
```json5
[{
  Symbol: "symbol",
  DateTime: "datetime",
  Price: "price",
  Volume: "volume",
  TradeNo: "tradeno",
  Action: "action"
}]
```

### CancelTicks
Used in conjunction with [Authorization](#Authorization)

URL : `https://localhost:5001/api/instruments/cancelticks`

Options:
* `Symbol`: Central Bank code from the TC Matrix quotes table.

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey",
  Symbol:"GAZP"
}
```
Result:
```json5
[{
  Result: "Запрос отправлен"
}]
```
### ListenBidAsks
Used in conjunction with [Authorization](#Authorization)

URL : `https://localhost:5001/api/instruments/listenbidasks`

Options:
* `Symbol`: Central Bank code from the TC Matrix quotes table.

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey",
  Symbol:"GAZP"
}
```
Result:
```json5
[{
   Symbol: "testLogin",
   Row: 0,
   NRows: 100,
   Bid:100.25,
   BidSize:25.25,
   Ask:150.79,
   AskSize:25.79
 }]
```

### CancelBidAsks
Used in conjunction with [Authorization](#Authorization)

URL : `https://localhost:5001/api/instruments/cancelbidasks`

Options:
* `Symbol`: Central Bank code from the TC Matrix quotes table.

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey",
  Symbol:"GAZP"
}
```
Result:
```json5
[{
  Result: "Запрос отправлен"
}]
```

### GetTrades
Used in conjunction with [Authorization](#Authorization)

URL : `https://localhost:5001/api/instruments/gettrades`

Options:
* `Symbol`: Central Bank code from the TC Matrix quotes table.
* `From`: Time. Used by YYYY-MM-DD hh:mm:ss
* `Count`: Number of requested ticks. The data type is Integer.

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey",
  Symbol:"GAZP"
}
```
Result:
```json5
[{
  row: 0,
  nrows: 46618,
  symbol: "6A.CME.H2015",
  DateTime: "2020-10-10",
  Price: 100.25,
  volume: 100.25,
  tradeNo: "idTrade",
  Action: 1
}]
```

### GetBars
Used in conjunction with [Authorization](#Authorization)

URL : `https://localhost:5001/api/instruments/getbars`

Options:
* `Symbol`: Central Bank code from the TC Matrix quotes table.
* `interval`: Time interval. It takes the following values: [BarInterval](#BarInterval)
* `since`: Start date of the requested interval. Used by YYYY-MM-DD
* `Count`: The number of intervals requested. If the number of requested intervals is positive, the collection goes back in time to the past from the specified date; if negative, then "forward".

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey",
  symbol:"GAZP",
  interval:3,
  since:"2020-10-15",
  count:10
}
```

Result:
```json5
[
    {
        row: 0,
        nrows: 10,
        symbol: "GAZP",
        interval: 3,
        datetime: "2020-10-14T18:50:00",
        open: 166.82000000000002,
        high: 167.58,
        low: 166.44,
        close: 166.46,
        volume: 790760,
        openInt: 0
    }
]
```
### GetPrortfolioList
Used in conjunction with [Authorization](#Authorization)

Additional portfolioStatus: Account status. It takes the following values: [PortfolioStatus](#PortfolioStatus)

URL : `https://localhost:5001/api/accountinformation/getprortfoliolist`

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey",
}
```

Result:
```json5
[{
    row: 0,
    nrows: 10,
    portfolioName: "namePortfolio",
    portfolioExch: "portfolioExch",
    portfolioStatus: 0
}]
```

### SetPortfolio
Used in conjunction with [Authorization](#Authorization)

URL : `https://localhost:5001/api/accountinformation/listenportfolio/setportfolio`

Options:
* `Portfolio`: Trading account number on the trading floor.

Example:
```json5
{
  login: "testLogin",
  password: "testPassword",
  key: "testKey",
  portfolio: "testPortfolio",
}
```
Result:
```json5
[{
  
}]
```
### AddTrade

### UpdateOrder

### UpdatePosition

### CancelPortfolio

### SetMyTrade

### SetMyClosePos

### SetMyOrder

#### OrderAction
* Accepts the following values: Buy : `1`
* Sell : `2`
* Open a "short position" : `3`
* Close "short position" : `4`

#### OrderType
* By market : `1`
* Limited : `2`
* Stop order : `3`
* Stop-Limit : `4`

#### OrderValidity
* Day : `1`
* GTC (until canceled, max. 30 days) : `2`

#### BarInterval
* 1 Min : `1`
* 5 Min : `2`
* 10 Min : `3`
* 15 Min : `4`
* 30 Min : `5`
* 60 Min : `6`
* 2 Hour : `7`
* 4 Hour : `8`
* Day : `9`
* Week : `10`
* Month : `11`
* Quarter : `12`
* Year : `13`

#### PortfolioStatus
* Broker : `0`
* TrustedManagement : `1`
* ReadOnly : `2`
* Blocked : `3`
* Restricted : `4`
* AutoRestricted : `5`
* OrderNotSigned : `6`