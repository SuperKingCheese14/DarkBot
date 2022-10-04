import discord
from discord import default_permissions
from bot_functions import *
import os

bot = discord.Bot(intents=intents.all())


# loading all cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")



bot.run('PUT YOUR TOKEN HERE')
