import discord
from discord.ext import commands
import asyncio
import urllib.request, json

class CRYPTO:
    """Crypto Test"""

    def __init__(self, bot):
        self.bot = bot
        
    def getReadableCoinName(coin):
        url = "https://bittrex.com/api/v1.1/public/getcurrencies"

        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
            currencies = data["result"]
            for currency in currencies:
                if currency["Currency"] == coin:
                    return currency["CurrencyLong"]
              
        return None
    
    def getTickerData(pair):
        pair = pair.replace("_", "-")
        url = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=" + pair

        with urllib.request.urlopen(url) as url:
            ticker = json.loads(url.read().decode())
            if ticker["success"] == True:
                return ticker["result"]

        return None
    
    def getTickerDataNEO():
        pair = ("BTC-Neo")
        url = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=" + pair

        with urllib.request.urlopen(url) as url:
            ticker = json.loads(url.read().decode())
            if ticker["success"] == True:
                return ticker["result"]

        return None
    
    @commands.command()
    async def CRYPTO(self):
        """This does stuff!"""
        ticker = getTickerDataNEO()
        ticker = ticker[0]
        pair = ticker["MarketName"]
        coin = getReadableCoinName(pair.split("-")[1])
        header = "**" + coin + " (" + pair.replace("-", "_") + ") - Bittrex**\n"
        seperator = "-----------------------\n"
        price = "Current Price: `" + "{:.8f}".format(ticker["Last"]) + "`\n"
        high = "24hr High: `" + "{:.8f}".format(ticker["High"]) + "`\n"
        low = "24hr Low: `" + "{:.8f}".format(ticker["Low"]) + "`\n"
        volume = "24hr Volume: `" + "{:.8f}".format(ticker["BaseVolume"]) + "`\n"

        changeNum = round(((ticker["Last"] - ticker["PrevDay"]) / ticker["PrevDay"]) * 100, 2)
        sign = "+" if changeNum > 0 else ""
        change = "Percent Change: ```diff\n" + sign + str(changeNum) + "%\n```"

        message = header + seperator + price + volume + high + low + change
        await self.bot.say(message)

def setup(bot):
    n = CRYPTO(bot)
    bot.add_cog(n)
