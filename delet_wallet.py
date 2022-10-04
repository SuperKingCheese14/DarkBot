import asyncio
import os
import discord
from discord.ext import commands
import json
from discord import default_permissions
from tinydb import TinyDB, Query
import requests

q = Query()
db = TinyDB('./databases/discord_wallets_db.json')

class DeleteWallet(commands.Cog):
    """
    Allows the user to unlink/delete their WAX wallet from the database
    
    """
    def __init__(self, bot):
        self.bot = bot
        
    @discord.slash_command(name = "deletewallet", description = "Delete your linked wallet address")
    async def delete_wallet(self, ctx, wallet):
        
        account_id = ctx.author.id
        wallet_address = wallet
        account_name = ctx.author
        result = db.search(q.Account_ID == account_id)
        
        if result == []:
            try:
                embedVar = discord.Embed(color=0xe74c3c)
                embedVar.set_author(name=(account_name), icon_url=account_name.avatar.url)
                embedVar.add_field(name="Wallet Update Error!", value="Discord user not found in database.")            
                return await ctx.channel.send(embed=embedVar)
            except Exception:
                embedVar = discord.Embed(color=0xe74c3c)
                embedVar.set_author(name=(account_name))
                embedVar.add_field(name="Wallet Update Error!", value="Discord user not found in database.")            
        else:
            db.remove(q.Account_ID == account_id)
            try:
                embedVar = discord.Embed(color=0x00ff00)
                embedVar.set_author(name=(account_name), icon_url=account_name.avatar.url)
                embedVar.add_field(name="Wallet Deleted", value="Your wallet has been removed from our database.")            
                return await ctx.channel.send(embed=embedVar)
            except Exception:
                embedVar = discord.Embed(color=0x00ff00)
                embedVar.set_author(name=(account_name))
                embedVar.add_field(name="Wallet Deleted", value="Your wallet has been removed from our database.")                
                
def setup(bot):
    bot.add_cog(DeleteWallet(bot))