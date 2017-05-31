import discord
from discord.ext import commands
import asyncio

class cd2:
    """Countdown test"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def cd2(self):
        """This does stuff!"""
        seconds = 75
        secondint = int(seconds)
        message = "TITLE TITLE TITLE\ntest test test\ntest test test\n"
        tbody = await self.bot.say(message)
        while secondint > 0:
            mins, secs = divmod(secondint, 60)
            timeformatm = '{:02d}:{:02d}'.format(mins, secs)
            if mins >= 1:
                await asyncio.sleep(5)
                secondint = secondint - 5
                await self.bot.edit_message(tbody, new_content=(message + "\nTime remaining:```glsl\n- " + timeformatm + "```"))
            else:
                await asyncio.sleep(1)
                secondint = secondint - 1
                await self.bot.edit_message(tbody, new_content=(message + "\nTime remaining:```diff\n- " + timeformatm + "```"))

        await self.bot.say("```css" + "\nDONE: {0}```".format(secondint))

def setup(bot):
    n = cd2(bot)
    bot.add_cog(n)
