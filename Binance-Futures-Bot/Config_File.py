##fill in your API keys here to be accessed by other scripts
API_KEY = '3I5mWkcakr4vmVWAndAg3nrcDDv4VkwQp7s2aNrtD5iHMZ3yksxsxc074mECNjbL'
API_SECRET = 'q4vZ6ZLHYRC2sYlB39g8fZtiXo5SPGReD3bqdOkXsqgjYp0g6vvmTtyO6ob6eBcf'

################## settings, these are very strategy dependant ensure you have enough data for your chosen strategy ##################################
order_Size = 90  ## As % of account, i.e 2.5 = 2.5%
leverage = 20
buffer = '30 day ago'  ## Buffer of candle sticks be careful if you don't provide enough the bot will throw an error
Interval = '1m'  ##candle sticks you want to trade
Max_Number_Of_Trades = 1  ## How many positions we can have open at once
use_trailing_stop = 1  ##If on we will use our TP value as the Activation price for a trailing stop loss
trailing_stop_callback = 0.2  ##trailing stop percent, this is .1% range is [.1% - 5%] .ie [0.1 - 5] (increments of .1 only)**
use_market_orders = True
trading_threshold = 0.1  ## %, i.e 0.1 = 0.1%

## New vars needed for the gui, running script from terminal will also need these now
strategy = 'tripleEMAStochasticRSIATR'
TP_SL_choice = '%'
SL_mult = 50
TP_mult = 1.0

##Trade All Coins if True, can also specify a list of coins to trade instead. Example: symbol = ['ETHUSDT','BTCUSDT'] & set Trade_All_Coins = False
Trade_All_Coins = False
symbol = ['XRPUSDT']  ## If Trade_All_Coins is False then we list the coins we want to trade here, otherwise the bot will automatically get all coins and trade them

