import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')
token = 'Njg2ODQ4MDU3OTQxMTY0MDMy.XmfvJg.XYZtcbwdC95pAMl7UuwcvxwYr_w'


@client.event
async def on_ready():
    print('Bot is online.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'reaction' in extensions:
        if message.author.id == 523312243698434084:
            pass
        else:
            emote = '💩'
            await message.add_reaction(emote)
    
    
extensions = {'reaction'}

if __name__ == '__main__':
    client.run(token)
