from discord import ButtonStyle, Button
from discord.ext import commands
import discord
from rs_controller import RuneScapeData
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='>', intents=intents)

class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Confirmed, make me an Atheist!", style=discord.ButtonStyle.primary, emoji="👑") 
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        return await interaction.response.send_message(f'Welcome to the High IQ Atheist club', ephemeral=True)


@bot.command()
async def highiq(ctx):
    await ctx.send("Thanks for your interest in converting to an Atheist, please confirm 👇🏻", view=MyView())


@bot.command()
async def champions(ctx):
    rc = RuneScapeData()
    await ctx.send(f"Current wc3 tourny champions and number of wins for DKK\n```\n{rc.get_champions()}\n```")


@bot.command()
async def runescape(ctx):
    rc = RuneScapeData()
    await ctx.send(f"Combat stats```\n{rc.get_rs_combat_data()}\n```")

@bot.command()
async def info(ctx):
    rc = RuneScapeData()
    await ctx.send(f"Current DKK bot commands```\n>highiq\n>champions\n>runescape\n>info\n``` have ideas for other commands? DM icepick")


discord_token =  os.environ.get('discord_token')
bot.run(discord_token) # Run the bot

