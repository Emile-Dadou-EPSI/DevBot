import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)
client = discord.Client()
DEFAUT_PREFIX = '!'
bot = commands.Bot(command_prefix='!')

@bot.command()
async def test(ctx):
    print("Command test")
    #channel = client.get_channel(644181580537004056)  # ID du chan "backup"
    await ctx.channel.send("My command works!")



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(644181580537004056)  # ID du chan "backup"
    await channel.send("Hello everyone i'm ready to work!")
    activity = discord.Activity(type=discord.ActivityType.playing, name="Prefix = {0}".format(DEFAUT_PREFIX))

bot.run(TOKEN)
