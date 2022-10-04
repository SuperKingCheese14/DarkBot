import asyncio
import os
import discord
from discord.ext import commands
from discord import default_permissions
import json

class SetReward(commands.Cog):
    """
    Sets the rewards for chat to earn, requires amount, token symbol and decimal precision.
    
    """
    def __init__(self, bot):
        self.bot = bot
        
    @discord.slash_command(name = "setreward", description = "Sets the reward for chat 2 earn")
    @default_permissions(manage_messages=True)
    async def setreward(self, ctx, amount, symbol, decimals):
        
        guild_id = str(ctx.guild.id)
        
        if decimals == "1":
            amount = ("{0:.01f}".format(float(amount)))
            print(amount)  
        elif decimals == "2":
            amount = ("{0:.02f}".format(float(amount)))
            print(amount)
        elif decimals == "3":
            amount = ("{0:.03f}".format(float(amount)))
            print(amount)    
        elif decimals == "4":
            amount = ("{0:.04f}".format(float(amount)))
            print(amount)    
        elif str(decimals) == "5":
            amount = ("{0:.05f}".format(float(amount)))
            print(amount)    
        elif str(decimals) == "6":
            amount = ("{0:.06f}".format(float(amount)))
            print(amount)
        elif str(decimals) == "7":
            amount = ("{0:.07f}".format(float(amount)))
            print(amount)    
        elif decimals == "8":
            amount = ("{0:.08f}".format(float(amount)))
            print(amount)    
        elif str(decimals) == "9":
            amount = ("{0:.09f}".format(float(amount)))
            print(amount)    
        elif str(decimals) == "10":
            amount = ("{0:.10f}".format(float(amount)))
            print(amount)
        else:
            print("Token decimal precision not supported")

        if str(symbol).isupper():
            with open("./databases/chat_rewards.json", 'r') as f:
                data = json.load(f)
                data[guild_id] = amount+" "+str(symbol)
                with open("./databases/chat_rewards.json", 'w') as f:
                    json.dump(data, f, indent = 4)
        else:
            print("Enter symbol in uppercase")
            
        embedVar = discord.Embed(color = 0x00ff00)
        embedVar.add_field(name = "Chat to Earn rewards updated", value = "Rewards amount: "+str(amount)+" "+str(symbol))
        await ctx.send(embed=embedVar)
            
def setup(bot):
    bot.add_cog(SetReward(bot))