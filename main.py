import os
import discord
from discord.ext import commands
intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')


@bot.event
async def on_ready():
    print('Bejelentkezve mint: {0} ({0.id})'.format(bot.user))
    await bot.change_presence(activity=discord.Game(name="Kezdésnek írd be, hogy: !segitseg"))


bot.run('MTA3MjI0MzU5MjIxMjUyMTA0MA.Ga0osC._Dl7IuxXWYU24iUFoHD_JLX8xIc3xROTUep0iU')