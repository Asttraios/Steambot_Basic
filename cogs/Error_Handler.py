import discord
from discord.ext import commands

class ErrorHandler(commands.Cog):
    def __init__(self, client):
        self.client = client  # Initialize the class with the Discord client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Handle specific command errors with appropriate messages
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions to do it!")
        elif isinstance(error, commands.MissingAnyRole):
            await ctx.send("You don't have the required role to do this!")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("Invalid command, try again!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Error. Missing argument in command.")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("Failed to invoke the command, try again!")
        elif isinstance(error, discord.Forbidden):
            await ctx.send("Forbidden: code 403")
        elif isinstance(error, discord.HTTPException):
            await ctx.send(f"HTTP Exception: {error.status}")
        else:
            await ctx.send("An unexpected error occurred.")

# Asynchronous function to add the ErrorHandler cog to the Discord bot
async def setup(client):
    await client.add_cog(ErrorHandler(client))
