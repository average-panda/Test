import discord
from discord.ext import commands
import asyncio
import urllib.request, json

class CR:
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
        
    @commands.command()
    async def cr(self):
        """This does stuff!"""
        await self.bot.say("Test")

def setup(bot):
    n = cr(bot)
    bot.add_cog(n)
