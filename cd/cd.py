import discord
from discord.ext import commands
import asyncio
import time

class cd:
    """Countdown test"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def mbc(self):
        """This does stuff!"""
        def countdown(t):
            t = 5
            while t:
                mins, secs = divmod(t, 60)
                timeformat = '{:02d}:{:02d}'.format(mins, secs)
                print(timeformat, end='\r')
                time.sleep(1)
                t -= 1
        await self.bot.say(t + ' time')
             
def setup(bot):
    bot.add_cog(cd(bot))
