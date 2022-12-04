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
        print(f"Clearing messages with {channel}")
        async for message in channel.history(limit=None).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
            try:
                time.sleep(1)#to avoid being ratelimited
                await message.delete()
            except:
                pass    

    '''Mass creates GCs with selected user'''
    @commands.command(name='seraph', aliases=['nuker','spammed'], pass_context=True)
    async def seraph(self, ctx):
        print('Called nuker')

    '''Direct messages all friends selected message'''
    @commands.command(name='dm', aliases=['massdm','told all my friends'])
    async def dmall(self, ctx, *, message):#args=None):
        await ctx.message.delete()
        for friend in self.bot.user.friends:
            try:
                await friend.send(message)#args)
            except:
                print(f"could not message: {friend.name} ")
                

def setup(bot):
    bot.add_cog(Clear(bot))
