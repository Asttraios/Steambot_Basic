import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

def run():
    # Set up intents for the bot
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    intents.voice_states = True

    load_dotenv()

    DISCORD_KEY=os.getenv('DISCORD_CLIENT_KEY')

    # Initialize the bot with command prefix '!' and specified intents
    client = commands.Bot(command_prefix='!', intents=intents)

    # List to store the extensions (cogs) to be loaded
    cogsExtensions = []
    
    # Event handler for when the bot is ready
    @client.event
    async def on_ready():     



        await client.change_presence(activity=discord.Game('Real world'))  # Set the bot's status
        for extension in cogsExtensions:
            await client.load_extension(extension)  # Load all extensions from cogs folder
        print("The bot is ready to work.")
        print("------------------")
    
    # Load all cogs from the 'cogs' directory
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            cogsExtensions.append("cogs." + filename[:-3])
            
    # Run the bot with the specified token
    print(DISCORD_KEY)
    client.run(DISCORD_KEY)
        
if __name__ == "__main__":
    run()
