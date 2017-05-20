import discord
from discord.ext import commands
import asyncio

class test:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        
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

        Tembed = discord.Embed(title="**Music Bot Controls**", color=discord.Colour(0xffbe00), description="Please refer to the following list of commands for the music bot:")

        Tembed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
        Tembed.set_author(name="※ VOICE OF KEK ※", icon_url="https://cdn.discordapp.com/app-icons/284962616361877507/0a82d11f51b37ca2d500eff675a41b51.jpg")
        Tembed.set_footer(text="※ VOICE OF KEK ※ Music Bot v0.7 | Updated May 20th, 2017", icon_url="https://cdn.discordapp.com/app-icons/284962616361877507/0a82d11f51b37ca2d500eff675a41b51.jpg")
        Tembed.add_field(name="Music:", value="*(these controls are available to everyone)*\n\n```fix\n*nowplaying = Shows the song that is currently playing``````fix\n*play <title|URL|subcommand> = plays the provided song``````fix\n*playlists = shows the available playlists``````fix\n*queue [pagenum] = shows the current queue``````fix\n*remove <position|ALL> = removes a song from the queue``````fix\n*play <title|URL|subcommand> = plays the provided song``````fix\n*play <title|URL|subcommand> = plays the provided song```")
        Tembed.add_field(name="DJ:", value="```fix\n*nowplaying = Shows the song that is currently playing```")
        Tembed.add_field(name="🙄", value="an informative error should show up, and this view will remain as-is until all issues are fixed")
        Tembed.add_field(name="<:thonkang:219069250692841473>", value="???")

        #Your code will go here
        await self.bot.say(embed=Tembed)
             
def setup(bot):
    bot.add_cog(test(bot))
