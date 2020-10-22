import discord
from discord.ext import commands

import random
from requests import get

class jack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="new")
    async def new(self, ctx):
        # try:
            html = "https://www.dropbox.com/" + "custom url"
            
            source = (get(html)).text
            xd = source.split(" ")
            embed = discord.Embed(colour=discord.Colour.blue(), description="holy shit qt")

            links = []
            for string in xd:
                if "previews.dropboxusercontent.com" in string:
                    h = string.find("https://")
                    x = string[h:]
                    if "/" in string:
                        slash = string.find("\\")
                        x = string[h:slash] + "g"
                    links.append(x)

            index = random.randint(0, len(links))

            # removing any messed up links
            while links[index] == "g" or get(links[index]).status_code != 200:
                index = random.randint(0, len(links))
            
            embed.set_image(url=links[index])
            await ctx.send(embed=embed)
               
def setup(bot):
    bot.add_cog(db(bot))
