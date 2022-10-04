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

class Verification(commands.Cog):
    """
    User registers their WAX wallet and if they own specific NFT, verified role is given
    
    """
    def __init__(self, bot):
        self.bot = bot
        
    @discord.slash_command(name = "verify", description = "User verifies their wallet")
    async def verify(self, ctx, wallet):
        
        account_id = ctx.author.id
        wallet_address = wallet
        account_name = ctx.author
        result = db.search(q.Account_ID == account_id)
        atomic_API_response = requests.get('https://nodes.darkgalaxies.io/atomicassets/v1/assets?collection_name=darkgalaxies&owner='+str(wallet_address)+'&page=1&limit=100&order=desc')
        data = atomic_API_response.text
        parse_data = json.loads(data)
        
        try:
            val = parse_data['data'][0]['contract']
        except Exception as e:
            val = 0
            
        if result == [] and str(val) == "atomicassets":
            db.insert({'Account_ID': account_id, 'Wallet_Address': wallet_address})
            with open("./databases/verifiedrole.json") as f:
                data = json.load(f)
            if str(ctx.guild.id) not in data or str(ctx.guild.id) is None:
                return
            role = data[str(ctx.guild.id)]
            role = ctx.guild.get_role(role)
            await account_name.add_roles(role)
            
            with open("./databases/autorole.json") as f:
                data = json.load(f)
            if str(ctx.guild.id) not in data or str(ctx.guild.id) is None:
                return
            role = data[str(ctx.guild.id)]
            
            role = ctx.guild.get_role(role)
            await account_name.remove_roles(role)
            
            try:
                embedVar = discord.Embed(color=0x00ff00)
                embedVar.set_author(name=(account_name), icon_url=account_name.avatar.url)
                embedVar.add_field(name="Verification successful", value="Your wallet is now verified and you can also collect DTX token rewards for chatting in the DarkGalaxies Discord.")            
                return await ctx.channel.send(embed=embedVar)
            except Exception:
                embedVar = discord.Embed(color=0x00ff00)
                embedVar.set_author(name=(account_name))
                embedVar.add_field(name="Verification successful", value="Your wallet is now verified and you can also collect DTX token rewards for chatting in the DarkGalaxies Discord.")
                return await ctx.channel.send(embed=embedVar)
        elif result == [] and int(val) == 0:
            try:
                embedVar = discord.Embed(color=0xe74c3c)
                embedVar.set_author(name=(account_name), icon_url=account_name.avatar.url)
                embedVar.add_field(name="Validation Error!", value="You must own at least one Dark Galaxies NFT to be verified in this server.")            
                return await ctx.channel.send(embed=embedVar)
            except Exception:
                embedVar = discord.Embed(color=0xe74c3c)
                embedVar.set_author(name=(account_name))
                embedVar.add_field(name="Validation Error!", value="You must own at least one Dark Galaxies NFT to be verified in this server")
                return await ctx.channel.send(embed=embedVar)
        else:
            try:
                embedVar = discord.Embed(color=0xe74c3c)
                embedVar.set_author(name=(account_name), icon_url=account_name.avatar.url)
                embedVar.add_field(name="Error!", value="Wallet already registered in database, please contact an admin.")            
                return await ctx.channel.send(embed=embedVar)
            except Exception:
                embedVar = discord.Embed(color=0xe74c3c)
                embedVar.set_author(name=(account_name))
                embedVar.add_field(name="Error!", value="Wallet already registered in database, please contact an admin.")            
                return await ctx.channel.send(embed=embedVar)                
                
def setup(bot):
    bot.add_cog(Verification(bot))
    
            
            
            