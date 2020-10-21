import requests


class CHP_api():
    def __init__(self, login, password):
        self.login = login
        self.password = password

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

    def get_bars(self):
        pass

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