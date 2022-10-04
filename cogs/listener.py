import asyncio
import discord
from discord.ext import commands

class Listener(commands.Cog):
    """
    Listens for specific messages
    
    """
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('.verify'):
            try:
                account = message.author
                embedVar = discord.Embed(color = 0xe74c3c)
                embedVar.set_author(name=(account), icon_url=account.avatar.url)
                embedVar.add_field(name="Error!", value="Please use slash command /verify to verify your wallet")
                return await message.channel.send(embed=embedVar)
            except Exception:
                account = message.author
                embedVar = discord.Embed(color = 0xe74c3c)
                embedVar.set_author(name=(account))
                embedVar.add_field(name="Error!", value="Please use slash command /verify to verify your wallet")
                return await message.channel.send(embed=embedVar)
        if message.content.startswith('.wallets'):
            try:
                account = message.author
                embedVar = discord.Embed(color = 0xe74c3c)
                embedVar.set_author(name=(account), icon_url=account.avatar.url)
                embedVar.add_field(name="Error!", value="Please use slash command /verify to verify your wallet")
                return await message.channel.send(embed=embedVar)
            except Exception:
                account = message.author
                embedVar = discord.Embed(color = 0xe74c3c)
                embedVar.set_author(name=(account))
                embedVar.add_field(name="Error!", value="Please use slash command /verify to verify your wallet")        
                return await message.channel.send(embed=embedVar)
        if message.content.startswith('/verify'):
            try:
                account = message.author
                embedVar = discord.Embed(color = 0xe74c3c)
                embedVar.set_author(name=(account), icon_url=account.avatar.url)
                embedVar.add_field(name="Error!", value="Please use slash command /verify to verify your wallet")
                return await message.channel.send(embed=embedVar)
            except Exception:
                account = message.author
                embedVar = discord.Embed(color = 0xe74c3c)
                embedVar.set_author(name=(account))
                embedVar.add_field(name="Error!", value="Please use slash command /verify to verify your wallet")
                return await message.channel.send(embed=embedVar)
        if message.content.startswith('/wallets'):
            try:
                account = message.author
                embedVar = discord.Embed(color = 0xe74c3c)
                embedVar.set_author(name=(account), icon_url=account.avatar.url)
                embedVar.add_field(name="Error!", value="Please use slash command /verify to verify your wallet")
                return await message.channel.send(embed=embedVar)
            except Exception:   
                account = message.author
                embedVar = discord.Embed(color = 0xe74c3c)
                embedVar.set_author(name=(account))
                embedVar.add_field(name="Error!", value="Please use slash command /verify to verify your wallet")
                return await message.channel.send(embed=embedVar)
def setup(bot):
    bot.add_cog(Listener(bot))