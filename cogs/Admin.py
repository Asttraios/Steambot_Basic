from datetime import timedelta
import discord
from discord.ext import commands
from functools import wraps

# Decorator to check if the user has kick permissions
def has_kick_perm(func):                                           
    @wraps(func)                                                                        
    async def wrapper(*args, **kwargs):
        if (args[1].message.author.guild_permissions.kick_members):   
            return await func(*args, **kwargs)
        else:
            await args[1].send("You don't have permissions to kick!")  # Send error message if no permissions
    return wrapper

# Decorator to check if the user has ban/unban permissions
def has_ban_unban_perm(func):
    @wraps(func)                                                                        
    async def wrapper(*args, **kwargs):
        if (args[1].message.author.guild_permissions.ban_members):
            return await func(*args, **kwargs)
        else:
            await args[1].send("You don't have permissions to ban or unban!")  # Send error message if no permissions
    return wrapper

# Decorator to check if the user has mute permissions
def has_mute_perm(func):                                                    
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if (args[1].message.author.guild_permissions.mute_members):
            return await func(*args, **kwargs)
        else:
            await args[1].send("You don't have permissions to mute!")  # Send error message if no permissions
    return wrapper

# Decorator to check if the user has timeout permissions
def has_timeout_perm(func):                                                  
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if (args[1].message.author.guild_permissions.moderate_members):
            return await func(*args, **kwargs)
        else:
            await args[1].send("You don't have permissions to timeout!")  # Send error message if no permissions
    return wrapper

# Class decorator example (not used in this script)

class decorator_class(object):                                  
    def __init__(self, original_function):
        self.original_function = original_function
    
    async def __call__(self, *args, **kwargs):
        print("call method executed this")
        return await self.original_function(*args, **kwargs)

# Admin commands cog
class Admin(commands.Cog):
    def __init__(self, client):        
        self.client = client  # Initialize the class with the Discord client
        
    # Kick command
    @commands.command()     
    @has_kick_perm  # Check if the user has kick permissions
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)  # Kick the member
        if reason is not None:
            await ctx.send(f"User {member} has been kicked for {reason}!")
        else:
            await ctx.send(f"User {member} has been kicked!")

    # Ban command    
    @commands.command()
    @has_ban_unban_perm  # Check if the user has ban permissions
    async def ban(self, ctx, member: discord.Member, *, reason=None):       
        await member.ban(reason=reason)  # Ban the member
        if reason is not None:
            await ctx.send(f"User {member} has been banned for {reason}!")
        else:
            await ctx.send(f"User {member} has been banned!")

    # Unban command
    @commands.command()
    @has_ban_unban_perm  # Check if the user has unban permissions
    async def unban(self, ctx, user: discord.User, *, reason=None):
        await ctx.guild.unban(user)  # Unban the user
        await ctx.send(f"User {user} has been unbanned!")
        
    # Mute command
    @commands.command()
    @has_mute_perm  # Check if the user has mute permissions
    async def mute(self, ctx, member:discord.Member, *, reason=None):
        channel = member.voice  # Get the member's voice channel
        
        if channel is not None:
            await member.edit(mute=True, reason=reason)  # Mute the member
            if reason is not None:
                await ctx.send(f"User {member} has been muted for {reason}!")
            else:
                await ctx.send(f"User {member} has been muted!")
        else:
            await ctx.send(f"User {member} is not in any voice channel at the moment!")  # Send error message if not in voice channel

    # Timeout command
    @commands.command()
    @has_timeout_perm  # Check if the user has timeout permissions
    async def timeout(self, ctx, member: discord.Member, time: int = 10, *, timeout_reason: str = None):
        try:
            silence_time = timedelta(seconds=time) 
            await member.timeout(silence_time, reason=timeout_reason)  # Timeout
        
            if timeout_reason:
                await ctx.send(f"User {member} has been timed-out for {time} seconds for: {timeout_reason}!")
            else:
                await ctx.send(f"User {member} has been timed-out for {time} seconds!")
        except ValueError:
            await ctx.send("Error: Wrong arguments - specify time!")


    # Test command
    @commands.command()
    @has_kick_perm  # Check if the user has kick permissions
    async def test(self, ctx): 
         await ctx.send("test")  # Send a test message
    
# Asynchronous function to add the Admin cog to the Discord bot
async def setup(client):
    await client.add_cog(Admin(client))
