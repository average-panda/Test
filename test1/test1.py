import discord
from discord.ext import commands
import asyncio

class test:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def mbc(self):
        """This does stuff!"""

        Tembed = discord.Embed(title="🎶 MUSIC BOT CONTROLS 🎶", colour=discord.Colour(0xffbe00), description="Please refer to the following list of commands for the music bot:\n")

        Tembed.set_author(name="※ VOICE OF KEK ※", icon_url="https://cdn.discordapp.com/app-icons/284962616361877507/0a82d11f51b37ca2d500eff675a41b51.jpg")
        Tembed.set_footer(text="🎧 ※ VOICE OF KEK ※ | Music Bot v0.0.5 | Updated May 20th, 2017")

        Tembed.add_field(name="Music:", value="*`⚪ these controls are available to everyone`*\n```fix\n*nowplaying = shows the song that is currently playing``````fix\n*play <title|URL|subcommand> = plays the provided song``````fix\n*playlists = shows the available playlists``````fix\n*queue [pagenum] = shows the current queue``````fix\n*remove <position|ALL> = removes a song from the queue``````fix\n*shuffle = shuffles songs you have added``````fix\n*skip = votes to skip the current song```\n`search commands` ```fix\n*search <query> = searches Youtube for a provided query``````fix\n*scsearch <query> = searches Soundcloud for a provided query```")
        Tembed.add_field(name="DJ:", value="*`⚪ these controls are available to ❖ LORDS OF KEK ❖`*```fix\n*forceskip = skips the current song``````fix\n*skipto <position> = skips to the specified song``````fix\n*stop = stops the current song and clears the queue``````fix\n*volume [0-150] = sets or shows volume```\n\n\n")

        Tembed.add_field(name="`❔`", value="For additional information type `*help`")
        Tembed.add_field(name="`⚠️`", value="If you are experiencing issues with the\nmusic bot, or if the bot is unavailable,\ncontact `average.panda`")

        #Your code will go here
        await self.bot.say(embed=Tembed)
             
def setup(bot):
    bot.add_cog(test(bot))
