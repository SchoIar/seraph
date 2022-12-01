from discord.ext import commands
class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='clear', aliases=['clr'], pass_context=True)
    async def clear(self, ctx, username=None):
        print("Called clear")

def setup(bot):
    bot.add_cog(Clear(bot))
