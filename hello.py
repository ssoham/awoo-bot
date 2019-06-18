import discord
from discord.ext import commands

class hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="greet", alias=['hello'])
    async def greet(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.blue()
        )
        embed.description = "hello"
        embed.set_author(name=bot.user)

        await ctx.send(embed=embed)
        # await ctx.send("hello !")

    @commands.command()
    # async def members(self, ctx):
    #     guild =

def setup(bot):
    bot.add_cog(hello(bot))
