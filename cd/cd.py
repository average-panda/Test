import discord
from discord.ext import commands
import asyncio

class cd:
    """Countdown test"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def cd(self):
        """This does stuff!"""
        seconds = 75
        secondint = int(seconds)
        message = "```TITLE TITLE TITLE\ntest test test\ntest test test\n"
        tbody = await self.bot.say(message)
        while secondint > 0:
            mins, secs = divmod(secondint, 60)
            timeformatm = '{:02d}:{:02d}s'.format(mins, secs)
            if mins >= 1
                await self.bot.edit_message(tbody, new_content=(message + "\nTime remaining:\n- " + timeformatm + "```"))
                await asyncio.sleep(5)
                secondint = secondint - 5
            break
            if mins < 1
                await self.bot.edit_message(tbody, new_content=(message + "\nTime remaining:\n- " + timeformatm + "```"))
                await asyncio.sleep(1)
                secondint = secondint - 1
            break
        await self.bot.say("```css" + "\nDONE: {0}```".format(secondint))

def setup(bot):
    n = cd(bot)
    bot.add_cog(n)
