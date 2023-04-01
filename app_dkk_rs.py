import discord
import runescape
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)


#managing ec2 server
#be in folder : 
#ssh -i .\runescape_kp.pem ec2-user@3.234.251.135

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!runescape':
        # Code to handle the command goes here
        await message.channel.send(':scroll: Current Runescape Random Stat for DKK Members :scroll:\n')
        for stream_log in runescape.get_rs_basic_data(is_random=True):
            await message.channel.send(stream_log)
    
    if message.content == '!runescape -combat':
        # Code to handle the command goes here
        #await message.channel.send("".join(runescape.get_rs_combat_data()))
        #await message.channel.send(':scroll: Current Runescape Random Stat for DKK Members :scroll:\n')
        #await message.channel.send(runescape.get_rs_combat_data())
        await message.channel.send(f"```\n{runescape.get_rs_combat_data()}\n```")

        #or stream_log in runescape.get_rs_basic_data(is_random=True):
         #   await message.channel.send(stream_log)


discord_token: str = os.environ.get('discord_token')
client.run(discord_token)