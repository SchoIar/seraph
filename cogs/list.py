from discord.ext import commands
class List(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command(name='list', aliases=['commands'], pass_context=True)
    async def clear(self, ctx):
        print("List of commands:  \n")
        print('''
        
        
        ''')


def setup(bot):
    bot.add_cog(List(bot))
