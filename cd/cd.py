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
        while secondint < 0:
            message = await self.bot.say("```css" + "\nTimer: " + seconds + "```")
            secondint = secondint - 1
            if secondint == 0:
                await self.bot.edit_message(message, new_content=("```Ended!```"))
                break
            await self.bot.edit_message(message, new_content=("```css" + "\nTimer: {0}```".format(secondint)))
            await asyncio.sleep(1)
        await self.bot.send_message(ctx.message.channel, ctx.message.author.mention + " Your countdown " + "[TITLE]"  + " Has ended!")

def setup(bot):
    bot.add_cog(cd(bot))
