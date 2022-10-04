import asyncio
import os
import discord
from discord import default_permissions
from discord.ext import commands
import json
import bot_functions
from bot_functions import *
from time import time
from requests import get
from tinydb import TinyDB, Query

member_messages = {}
q = Query()
db = TinyDB('./databases/discord_wallets_db.json')

class Chat2Earn(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
    
        global member_messages
        current_time = time()
        last_message_requirement = current_time - 15
    
        if int(message.channel.id) == 1020775165652631613:
            user = message.author.id
            result = db.search(q.Account_ID == user)
        
            if result == []:
                return
            else:
                wallet = result[0]['Wallet_Address']
                to_account = wallet
                if member_messages.get(message.author.id, 0) <= last_message_requirement:
                    with open("./databases/spam_check.json", "r") as f:
                        users = json.load(f)
                    try:
                        with open("./databases/chat_rewards.json") as f:
                            data = json.load(f)
                            amount = data[str(message.guild.id)]
                        reward = rewards(to_account, amount)
                    except Exception as e:
                        print(e)
                with open("./databases/spam_check.json", "w") as f:
                    json.dump(user, f)
                member_messages[message.author.id] = current_time
        
def setup(bot):
    bot.add_cog(Chat2Earn(bot))
        
        
         
            
    
    