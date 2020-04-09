import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')
token = '****'


@client.event
async def on_ready():
    print('Bot is online.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'reaction' in extensions:
        if message.author.id == ****:
            pass
        else:
            emote = '💩'
            await message.add_reaction(emote)
    
    
extensions = {'reaction'}

if __name__ == '__main__':
    client.run(token)
