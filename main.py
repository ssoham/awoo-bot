import discord
import json
import os
path = os.path.abspath('awoo\TOKEN.json')
bot = discord.Client()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        print(message.author + ": " + message.content)


with open(path, 'r') as f:
    data = json.load(f)
token = data['api']
print('Files loaded! Bot is being launched! <o/')
bot.run(token)
