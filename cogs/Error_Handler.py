import discord
from discord.ext import commands

class ErrorHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
       if isinstance(error, commands.MissingPermissions):
           await ctx.send("You don't have permissions to do it!")
           print("error handling works")
       else:
           print("error handling not working")
            
      
async def setup(client):
    await client.add_cog(ErrorHandler(client))




