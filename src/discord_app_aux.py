from discord import ButtonStyle, Button
from discord.ext import commands
import discord
from rs_controller import RuneScapeData
import os


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    print(f"hi {member}, channel: {channel}")
    if channel:
        await channel.send(f"Welcome to clan DKK, {member.mention}! Any questions? Hit up: Chairboy, tiger or icepick.\n For more info about this server, head over to #clan-dkk-intro.")


client.run(os.environ.get('discord_token'))