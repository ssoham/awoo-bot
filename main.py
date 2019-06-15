from discord.ext import commands
import discord
import json
import os
path = os.path.abspath('TOKEN.json')
bot = commands.Bot(command_prefix="~")
bot.remove_command('help')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        print(str(message.author) + ": " + str(message.content))
        await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    '''awooo'''
    lat = bot.latency
    await ctx.send(lat)

@bot.command()
async def hello(ctx):
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.description = "hello"
    embed.set_author(name=bot.user)

    await ctx.send(embed=embed)


with open(path, 'r') as f:
    data = json.load(f)
token = data['api']
print('Files loaded! Bot is being launched! <o/')
bot.run(token)
