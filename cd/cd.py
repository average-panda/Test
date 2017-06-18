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
        ttl = "TITLE TEST"
        ttldsc = "description test test test"
        bdy1 = "title body body body"
        bdydsc = "body test test test"
        ins = "Instructions: "
        insdsc = "React with 🎁 to join the draw."
        
        message = discord.Embed(title=ttl, description=ttldsc, color=0x2aa198)
        message.add_field(name=bdy1, value=bdydsc, inline=False)
        tbody = await self.bot.say(embed=message)

        await self.bot.add_reaction(tbody, '🎁')

        while secondint > 0:
            mins, secs = divmod(secondint, 60)
            timeformatm = '{:02d}:{:02d}'.format(mins, secs)
            if secondint > 60:
                message2 = discord.Embed(title=ttl, description=ttldsc, color=0x2aa198)
                message2.add_field(name=bdy1, value=bdydsc, inline=False)
                message2.add_field(name=ins, value=insdsc, inline=False)
                message2.add_field(name="Time remaining:", value="```glsl\n- " + timeformatm + "```", inline=True)
                await self.bot.edit_message(tbody, embed=(message2))
                await asyncio.sleep(5)
                secondint = secondint - 5
            elif secondint > 30:
                message2 = discord.Embed(title=ttl, description=ttldsc, color=0xffb300)
                message2.add_field(name=bdy1, value=bdydsc, inline=False)
                message2.add_field(name=ins, value=insdsc, inline=False)
                message2.add_field(name="Time remaining:", value="```fix\n- " + timeformatm + "```", inline=True)
                await self.bot.edit_message(tbody, embed=(message2))
                await asyncio.sleep(1)
                secondint = secondint - 1
            else:
                message2 = discord.Embed(title=ttl, description=ttldsc, color=0xff0000)
                message2.add_field(name=bdy1, value=bdydsc, inline=False)
                message2.add_field(name=ins, value=insdsc, inline=False)
                message2.add_field(name="Time remaining:", value="```diff\n- " + timeformatm + "```", inline=True)
                await self.bot.edit_message(tbody, embed=(message2))
                await asyncio.sleep(1)
                secondint = secondint - 1

        message2 = discord.Embed(title=ttl, description=ttldsc, color=0xc0c0c0)
        message2.add_field(name=bdy1, value=bdydsc, inline=False)
        message2.add_field(name="Giveaway complete", value="```fix\nWinner = -winner- ```", inline=False)
        await self.bot.edit_message(tbody, embed=(message2))

def setup(bot):
    n = cd(bot)
    bot.add_cog(n)
