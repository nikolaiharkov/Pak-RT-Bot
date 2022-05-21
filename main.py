import discord
from discord import client
import os
from discord.ext import commands

activity = discord.Activity(type=discord.ActivityType.listening, name=">help | for more info")

# bot prefix
intents=discord.Intents.default()
intents.members=True
client = commands.Bot(command_prefix=">", intents=intents, activity=activity, status=discord.Status.online)


# loading all the cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and not filename.startswith("_"):
        client.load_extension(f"cogs.{filename[:-3]}")
    

token=""
client.run(token)
