import discord
from discord.ext import commands
import asyncio

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", description="Returns Pong!")
    async def ping(self, ctx):
        await ctx.send("Pong!")        

def setup(bot):
    bot.add_cog(ping(bot))