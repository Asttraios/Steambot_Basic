import discord
from discord.ext import commands
from discord import DiscordException

class ErrorHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
       if isinstance(error, commands.MissingPermissions):
           await ctx.send("You don't have permissions to do it!")
       elif isinstance(error, commands.MissingAnyRole):
           await ctx.send("You don't have required role to do this!")
       elif isinstance(error, commands.CommandNotFound):
           await ctx.send("Invalid command, try again!")
       elif isinstance(error, commands.MissingRequiredArgument):
           await ctx.send("Error. Missing argument in command. ")
       elif isinstance(error, commands.CommandInvokeError):
           await ctx.send("Failed to invoke the command, try again!")
       elif isinstance(error, discord.Forbidden):
           await ctx.send("Forbidden: code 403")
       elif isinstance(error, discord.DiscordServerError):
           await ctx.send("Server Error: code 404")
       elif isinstance(error, discord.DiscordException):
           await ctx.send("If you somehow get this error, it means something's really fu**** up...")
           
           
      
async def setup(client):
    await client.add_cog(ErrorHandler(client))




