import discord
from runescape import RuneScapeData
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!runescape':
        rc = RuneScapeData()
        await message.channel.send(':scroll: Current Runescape Random Stat for DKK Members :scroll:\n')
        for stream_log in rc.get_rs_basic_data(is_random=True):
            await message.channel.send(stream_log)
    
    if message.content == '!runescape -combat':
        rc = RuneScapeData()
        await message.channel.send(f"```\n{rc.get_rs_combat_data()}\n```")


discord_token =  os.environ.get('discord_token')
client.run(discord_token)