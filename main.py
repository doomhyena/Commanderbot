import nextcord
from nextcord.ext import commands
import os

bot = commands.Bot(command_prefix='!', intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} online van!')
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            bot.load_extension(f'commands.{filename[:-3]}')

bot.run('TOKEN')
