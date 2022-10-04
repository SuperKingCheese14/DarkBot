import asyncio
import os
import discord
from discord.ext import commands
from discord import default_permissions
import requests
import json

class ActiveMiners(commands.Cog):
    """
    Fetches a list of active miners on the users planets
    
    """
    def __init__(self, bot):
        self.bot = bot
        
    @discord.slash_command(name = "miners", description = "Fetches a list of active miners on the users planets")
    async def miners(self, ctx, wallet):
        
        names = ctx.author
        wallet_add = wallet
        response_api = requests.get('https://nodes.darkgalaxies.io/atomicassets/v1/assets?collection_name=darkgalaxies&schema_name=dark.planets&owner='+str(wallet_add)+'&page=1&limit=100&order=desc&sort=asset_id')

        data = response_api.text
        val = json.loads(data)
        val2 = val['data']
        planets_list = []
        miners_list = []

        for planets in val2:
            planets_list.append(planets['asset_id'])
    
        for planets in planets_list:
            url = 'http://wax.greymass.com/v1/chain/get_table_rows'
            velesobj = {
                "json": True,
                "code": "darkminingsc",
                "scope": planets,
                "table": "slots",
                "table_key": "",
                "lower_bound": None,
                "upper_bound": None,
                "index_position": 1,
                "key_type": "",
                "limit": "10000",
                "reverse": False,
                "show_payer": False
            }  
            data = requests.post(url, json=velesobj).json()
            val = data['rows']
    
            for miners in val:
                miners_list.append(miners['miner'])
        
            stopwords = ['free']

            for word in list(miners_list):
                if word in stopwords:
                    miners_list.remove(word)

            active_miners_list = list(dict.fromkeys(miners_list))
            legnth = len(active_miners_list)
            active_miners = (', '.join(active_miners_list))

            if legnth >= 1:
                print(ctx.author)
                try:
                    embedVar = discord.Embed(color=0x00ff00)
                    embedVar.set_author(name=(names), icon_url=names.avatar.url)
                    embedVar.add_field(name="Total Miners", value="Your planets have "+str(legnth)+" Miners")
                    embedVar.add_field(name="Miners Wallets:", value=active_miners2, inline=False)
                    return await ctx.channel.send(embed=embedVar)
                except Exception:
                    embedVar = discord.Embed(color=0x00ff00)
                    embedVar.set_author(name=(names))
                    embedVar.add_field(name="Total Miners", value="Your planets have "+str(legnth)+" Miners")
                    embedVar.add_field(name="Miners Wallets:", value=active_miners2, inline=False)
                    return await ctx.channel.send(embed=embedVar)                    

            else:
                print(ctx.author)
                try:
                    embedVar = discord.Embed(color=0xe74c3c)
                    embedVar.set_author(name=(names), icon_url=names.avatar.url)
                    embedVar.add_field(name="No miners found", value="Your planets have 0 active miners")
                    return await ctx.channel.send(embed=embedVar)
                except Exception:
                    embedVar = discord.Embed(color=0xe74c3c)
                    embedVar.set_author(name=(names))
                    embedVar.add_field(name="No miners found", value="Your planets have 0 active miners")
                    return await ctx.channel.send(embed=embedVar)                    
def setup(bot):
    bot.add_cog(ActiveMiners(bot))
    
