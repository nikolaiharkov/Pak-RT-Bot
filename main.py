import discord
from discord import client
import os
from discord.ext import commands

# bot prefix
intents=discord.Intents.default()
intents.members=True
client = commands.Bot(command_prefix=">", intents=intents)

# loading all the cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and not filename.startswith("_"):
        client.load_extension(f"cogs.{filename[:-3]}")

token="OTU4NjY4MDc4ODc3NjcxNDU0.YkQrOQ.1XrlTTNMYupoNr0lv0MAFlYuSio"
client.run(token)
