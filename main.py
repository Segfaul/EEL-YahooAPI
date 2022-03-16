import eel
import yfinance as yf
import matplotlib.pyplot as plt
def stock_info(tag):
    try:
        stock = yf.Ticker(tag.upper())
        stats = stock.history(period="100d")
        stats['Close'].plot(figsize=(16, 9))
        plt.show()
    except:
        print("Incorrect input")
        return -1
eel.init("web")
@eel.expose
def get_stats(stock_n):
    stock_info(stock_n)
eel.start("start.html", size = (500, 500))