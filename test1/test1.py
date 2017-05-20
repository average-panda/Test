import discord
from discord.ext import commands
import asyncio

class test:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        
        Tembed = discord.Embed(title="test", colour=discord.Colour(0xffbe00), url="https://discordapp.com", description="```test```")
        Tembed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
        Tembed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")

    @commands.command()
    async def punch(self, user : discord.Member):
        """I will puch anyone! >.<"""

        #Your code will go here
        await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")
        
    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")
        
    @commands.command()
    async def embed(self):
        """This does stuff!"""

        Tembed = discord.Embed(title="test", colour=discord.Colour(0x687508), url="https://discordapp.com", description="test")

        #Your code will go here
        await self.bot.say(embed=Tembed)
             
def setup(bot):
    bot.add_cog(test(bot))
