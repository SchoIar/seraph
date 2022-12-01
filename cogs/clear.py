from discord.ext import commands
class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''Clears all messages in selected channel'''
    @commands.command(name='clear', aliases=['clr'], pass_context=True)
    async def clear(self, ctx):
        print("Called clear")

    '''Grabs a cat picture '''

def setup(bot):
    bot.add_cog(Clear(bot))
