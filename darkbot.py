import discord
from discord import default_permissions
from bot_functions import *
import os

intents = discord.Intents.default()
intents.messages = True
intents.members = True
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
bot = discord.Bot(intents=intents, members = True, guilds = True, messages = True, guild_messages = True, message_content = True)


# loading all cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")



bot.run('MTAyMDYzMDU3Mzg0MjE4MjIxNQ.GA-vG5.ZxhWBlxFcI5RIigrBJfBtGUddo883Xr7GpLaxo')
