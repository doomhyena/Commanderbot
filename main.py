import nextcord
from nextcord.ext import commands
import os

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} online van!')
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            bot.load_extension(f'commands.{filename[:-3]}')

bot.run('MTA3MjI0MzU5MjIxMjUyMTA0MA.Ga0osC._Dl7IuxXWYU24iUFoHD_JLX8xIc3xROTUep0iU')