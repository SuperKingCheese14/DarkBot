import asyncio
import os
import discord
from discord.ext import commands
from discord import default_permissions
import json

class WelcomeRoles(commands.Cog):
    """
    Assign roles to members on server join
    
    """
    def __init__(self, bot):
        self.bot = bot
        
    
    async def find_welcome_channel(self, guild: discord.Guild) -> discord.TextChannel or None:
        
        channels: list[discord.TextChannels] = await guild.fetch_channels()
        
        for channel in channels:
            if "welcome" in channel.name:
                return channel
                print(channel)
                
            return None
            
    @discord.slash_command(name = "defaultrole", description="Sets the default role for the server")
    @default_permissions(manage_messages=True)
    async def defaultrole(self, ctx, role:discord.Role):
        role_id = role.id
        guild_id = str(ctx.guild.id)
        
        with open("./databases/autorole.json", 'r') as f:
            data = json.load(f)
            #data['autorole'].append(role_id)
            data[guild_id] = role_id
            with open("./databases/autorole.json", 'w') as f:
                json.dump(data, f, indent = 4)
        print(role) 
        
        embedVar = discord.Embed(color = 0x00ff00)
        embedVar.add_field(name = "Default role set to: ", value = f"{role.mention}")
        await ctx.send(embed=embedVar)
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open("./databases/autorole.json") as f:
            data = json.load(f)
            
        if str(member.guild.id) not in data or str(member.guild.id) is None:
            return
        
        role = data[str(member.guild.id)]
        
        role = member.guild.get_role(role)
        await member.add_roles(role)
        
        
        
def setup(bot):
    bot.add_cog(WelcomeRoles(bot))