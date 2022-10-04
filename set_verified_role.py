import asyncio
import os
import discord
from discord.ext import commands
from discord import default_permissions
import json

class SetVerifiedRole(commands.Cog):
    """
    Sets the default role for verified members
    
    """
    def __init__(self, bot):
        self.bot = bot
            
    @discord.slash_command(name = "setverified", description="Sets the role for verified members")
    @default_permissions(manage_messages=True)
    async def autorole(self, ctx, role:discord.Role):
        role_id = role.id
        guild_id = str(ctx.guild.id)
        
        with open("./databases/verifiedrole.json", 'r') as f:
            data = json.load(f)
            data[guild_id] = role_id
            with open("./databases/verifiedrole.json", 'w') as f:
                json.dump(data, f, indent = 4)
        print(role) 
        
        embedVar = discord.Embed(color = 0x00ff00)
        embedVar.add_field(name = "Verified role set to: ", value = f"{role.mention}")
        await ctx.send(embed=embedVar)
        
def setup(bot):
    bot.add_cog(SetVerifiedRole(bot))