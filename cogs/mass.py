# Commands for Mass usage (ie. Mass DM)
from discord.ext import commands
import time;


class Mass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

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
    bot.add_cog(Mass(bot))