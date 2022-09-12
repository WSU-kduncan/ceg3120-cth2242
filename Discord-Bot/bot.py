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

    hitchhiker_quotes = [
        'There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.',
        'It is a mistake to think you can solve any major problems just with potatoes.',
        'In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.',
        'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.',
    ]

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
    #if message.content.startswith('$towel'):
        response = random.choice(arnold_quotes)
        await message.channel.send(response)
#1234
client.run(TOKEN)
