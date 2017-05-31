import discord
from discord.ext import commands
import asyncio
import time

class cd:
    """Countdown test"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def cd(self):
        """This does stuff!"""
        seconds = 15
        secondint = int(seconds)
        tbody = "TITLE\n body body body \n"
        while secondint < 0:
            await asyncio.sleep(1)
            await self.bot.say("```css" + "\nTimer: " + secondsint + "```")
        await self.bot.say("```css" + "\nDONE: " + secondsint + "```")

def setup(bot):
    n = cd(bot)
    bot.add_cog(n)
