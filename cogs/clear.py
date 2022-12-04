from discord.ext import commands
import time;
class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''Clears all messages in selected channel'''
    @commands.command(name='clear', aliases=['clr','cleared my dms'], pass_context=True)
    async def clear(self, ctx):
        await ctx.message.delete()
        channel = ctx.channel
        print(f"Clearing messages in: {channel}")
        async for message in channel.history(limit=None).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
            try:
                await message.delete()
                time.sleep(1)#to avoid being ratelimited
            except:
                pass    

def setup(bot):
    bot.add_cog(Clear(bot))
