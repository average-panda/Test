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
        message = discord.Embed(title="TEST TEST", description="test test test", color=0x0080ff)
        message.add_field(name="time here TITLE", value="time here", inline=False)
        tbody = await self.bot.say(embed=message)
        while secondint > 0:
            mins, secs = divmod(secondint, 60)
            timeformatm = '{:02d}:{:02d}'.format(mins, secs)
            if secondint > 60:
                message2 = discord.Embed(title="TEST TEST", description="test test test", color=0x0080ff)
                message2.add_field(name="Time remaining:", value="```glsl\n- " + timeformatm + "```", inline=True)
                await self.bot.edit_message(tbody, embed=(message2))
                await asyncio.sleep(5)
                secondint = secondint - 5
            else:
                message2 = discord.Embed(title="TEST TEST", description="test test test", color=0xff0000)
                message2.add_field(name="Time remaining:", value="```diff\n- " + timeformatm + "```", inline=True)
                await self.bot.edit_message(tbody, embed=(message2))
                await asyncio.sleep(1)
                secondint = secondint - 1

        message2 = discord.Embed(title="TEST TEST", description="test test test", color=0xff0000)
        message2.add_field(name="Giveaway complete", value="```fix\nWinner = " + "-winner- ```", inline=False)
        await self.bot.edit_message(tbody, embed=(message2))

def setup(bot):
    n = cd(bot)
    bot.add_cog(n)
