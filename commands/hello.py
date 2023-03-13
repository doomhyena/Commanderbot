import nextcord
from nextcord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Szia Natsuki#5480!')

def setup(bot):
    bot.add_cog(Hello(bot))