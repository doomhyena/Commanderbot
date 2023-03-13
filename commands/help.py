import nextcord
from nextcord.ext import commands
import datetime

class Segitsegcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def segitseg(self, ctx):
        embed = nextcord.Embed(title="Ez a segítség menü. tt találod meg a parancsaimat!", description = "Minden parancs elé tegyél !-et hogy működjön a parancs!", color = 0xff0000)

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(icon_url=ctx.author.avatar_url, name=f'{ctx.author}')
        embed.add_field(name="!segitseg", value="Ez a menü rendszer Itt a találod a parancsaimat!", inline=False)
        embed.add_field(name="!globalchatstart", value="Ezzel tudod elérni, hogy más szerverekre tudj üzeneteket küldeni.", inline=False)
        embed.add_field(name="!globalchatstop", value= "Ezzel a paranccsal törlöd azt a funkciót, hogy más szerverekről tudjanak egy adott csatornába üzeneteket küldeni a szerverre illetve te küldj más szerverekre üzenetet.", inline=False)
        embed.set_footer(icon_url=ctx.guild.icon_url, text=ctx.guild.name)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Segitsegcommand(bot))