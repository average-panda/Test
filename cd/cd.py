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
        seconds = 90
        secondint = int(seconds)
        tbody = "TITLE\n body body body \n"
        while secondint < 0:
            message = await self.bot.say("```css" + "\nTimer: " + seconds + "```")
            secondint = secondint - 1
            await self.bot.edit_message(message, new_content=("```css" + "\nTimer: {0}```".format(secondint)))
            await asyncio.sleep(1)

def setup(bot):
    bot.add_cog(cd(bot))
