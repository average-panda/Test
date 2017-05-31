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
                embed=discord.Embed(title="Game description:", description="Destiny 2 is an action shooter that takes you on an epic journey across the solar system. In the cinematic campaign, you’ll enter a world filled with compelling characters and fight to take back our home. Battle alongside friends with multiple cooperative modes or challenge others in intense multiplayer matches.", color=0x4787e7)
                embed.set_author(name="🎁 GIVEAWAY - Destiny 2 🎁", url='https://www.destinythegame.com/home')
                embed.set_thumbnail(url='http://www.product-reviews.net/wp-content/uploads/destiny-2-logo.jpg')
                embed.add_field(name="How to enter:", value="🎁🎁🎁🎁", inline=False)
                embed.set_footer(text="Give away | 31 May 2017")
                await asyncio.sleep(5)
                secondint = secondint - 5
                await self.bot.edit_message(tbody, new_content=(embed=embed))
            else:
                await asyncio.sleep(1)
                secondint = secondint - 1
                await self.bot.edit_message(tbody, new_content=(message + "\nTime remaining:```diff\n- " + timeformatm + "```"))

        await self.bot.say("```css" + "\nDONE: {0}```".format(secondint))

def setup(bot):
    n = cd2(bot)
    bot.add_cog(n)
