from datetime import datetime, timedelta
from email.errors import MessageError
from http import client
import discord
from discord.ext.commands import MissingPermissions, has_permissions
from discord.ext import commands
from discord.gateway import DiscordClientWebSocketResponse
from functools import wraps



def has_kick_perm(func):                                              ### KICK
    @wraps(func)                                                                        
    async def wrapper(*args, **kwargs):
        if (args[1].message.author.guild_permissions.kick_members):   
            return await func(*args, **kwargs)
        else: await args[1].send("You don't have permissions to kick!")     ### raise commands.MissingPermissions(['kick_members'])
    return wrapper

def has_ban_unban_perm(func):
    @wraps(func)                                                                        ### BAN/UNBAN
    async def wrapper(*args, **kwargs):
        if (args[1].message.author.guild_permissions.ban_members):
            return await func(*args, **kwargs)
        else: await args[1].send("You don't have permissions to ban or unban!")
    return wrapper


def has_mute_perm(func):                                                    ### MUTE
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if (args[1].message.author.guild_permissions.mute_members):
            return await func(*args, **kwargs)
        else: await args[1].send("You don't have permissions to mute!")
    return wrapper

def has_timeout_perm(func):                                                 ### TIMEOUT
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if (args[1].message.author.guild_permissions.moderate_members):
            return await func(*args, **kwargs)
        else: await args[1].send("You don't have permissions to timeout!")
    return wrapper


class decorator_class(object):                                  ### CLASS DECORATOR - NOT USED
    def __init__(self, original_function):
        self.original_function = original_function
    
    async def __call__(self, *args, **kwargs):
        print("call method executed this")
        return await self.original_function(*args, **kwargs)


class Admin(commands.Cog):
    
    ### moderator, administrator 

    ### BAN
    ### UNBAN
    ### MUTE
    ### TIMEOUT

    ### ADD REASON ?
    ### ERROR HANDLING

    ### ADD CHECKING IF USER IS ACTIVE OR NOT -> TIMEOUTING NONACTIVE USERS     IDK YET
    ### NEXT UPDATE -> WELCOMING STEAM, PLAYING FUNNY BEZIMIENNY AUDIO :333 AAAAANNND MAKE FULL ERROR HANDLER
    
    

    def __init__(self, client):         ## HOW DOES IT KNOW WHAT CLIENT IS????
        self.client = client
        
    @commands.command()     
    @has_kick_perm
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        if reason is not None:
            await ctx.send(f"User {member} has been kicked for {reason}!")
        else:
            await ctx.send(f"User {member} has been kicked!")

        
    @commands.command()
    @has_ban_unban_perm
    async def ban(self, ctx, member: discord.Member, *, reason=None):       
        await member.ban(reason=reason)
        if reason is not None:
            await ctx.send(f"User {member} has been banned for {reason}!")
        else:
            await ctx.send(f"User {member} has been banned!")


    @commands.command()
    @has_ban_unban_perm
    async def unban(self, ctx, user: discord.User, *, reason=None):
        await ctx.guild.unban(user)
        await ctx.send(f"User {user} has been unbanned!")
        

    @commands.command()
    @has_mute_perm
    async def mute(self, ctx, member:discord.Member, *, reason=None):
        
        channel = member.voice
        
        if channel is not None:
            await member.edit(mute=True, reason=reason)
            if reason is not None:
                await ctx.send(f"User {member} has been muted for {reason}!")
            else:
                await ctx.send(f"User {member} has been muted!")
                print(channel)
        else:
            await ctx.send(f"User {member} is not in any voice channel at the moment!")         ### DELETE PRRINTS LATER
            print(channel)

    
    @commands.command()
    @has_timeout_perm
    async def timeout(self, ctx, member:discord.Member, *,  reason=None):
        new_time =timedelta(seconds=10)
        await member.timeout(new_time, reason=reason)
        if reason is not None:
            await ctx.send(f"User {member} has been timed out for {reason}!")
        else:
            await ctx.send(f"User {member} has been timed!")
    
    
    @commands.command()
    @has_kick_perm
    async def test(self, ctx): 
         await ctx.send("test")
    
        
async def setup(client):
    await client.add_cog(Admin(client))