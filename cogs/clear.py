from discord.ext import commands
class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''Clears all messages in selected channel'''
    @commands.command(name='clear', aliases=['clr'], pass_context=True)
    async def clear(self, ctx, username=None):
        print("Called clear")

    '''Mass creates GCs with selected user'''
    @commands.command(name='seraph', aliases=['nuker'], pass_context=True)
    async def seraph(self, ctx, ):
        print('Called nuker')
        

    '''Direct messages all friends selected message'''
    @commands.command(name='dmall', aliases=['dm'])
    async def dmall(self, ctx, *, message):#args=None):
        await ctx.message.delete()
        for friend in self.bot.user.friends:
            try:
                await friend.send(message)#args)
            except:
                print(f"could not message: {friend.name} ")
                

def setup(bot):
    bot.add_cog(Clear(bot))
