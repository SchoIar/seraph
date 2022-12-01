import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')


bot = commands.Bot(command_prefix='.', self_bot=True, case_sensitive=False)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token, bot=False)
