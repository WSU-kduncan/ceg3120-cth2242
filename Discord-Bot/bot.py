# Based on example https://discordpy.readthedocs.io/en/stable/quickstart.html
import os

import discord
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    arnold_quotes = [
        'Let off some steam, Bennett',
        'You\'ve just been erased',
        'I eat Green Berets for Breakfast, and right now, I\'m very hungry',
        'Get to the choppa!',
        'I\'ll be back',
        'Come with me if you want to live',
        'If it bleeds, we can kill it',
        'Dillion, you son of a bitch',
        'Hasta la vista, baby',
        'Let\'s kick some ice',
        'Freeze in Hell, Batman',
     ]    
    if message.content == 'arnold!':
        response = random.choice(arnold_quotes)
        await message.channel.send(response)

client.run(TOKEN)
