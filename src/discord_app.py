import discord
from rs_controller import RuneScapeData
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    if channel:
        await channel.send(f"Welcome to clan DKK, {member.mention}! Any questions? Hit up Chairboy, icepick or tiger")


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

    if message.content == '!runescape -delta':
        rc = RuneScapeData()
        await message.channel.send("All stat changes in the past 24 hours from 12pm est to 12pm est")
        await message.channel.send(f"```\n{rc.get_delta()}\n```")

    if message.content == '!help':
        rc = RuneScapeData()
        await message.channel.send("All current DKK bot commands\n'!runescape'\n'!runescape -combat'\n'!runescape -delta'\n '!champions'\n")
    
    if message.content == '!champions':
        rc = RuneScapeData()
        await message.channel.send(f"```\n{rc.get_champions()}\n```")

    if message.content == '!icebreaker':
        pass

discord_token =  os.environ.get('discord_token')
client.run(discord_token)