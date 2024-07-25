import discord
from discord.ext import commands
import os
import requests


def run():

    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    intents.voice_states = True

    client = commands.Bot(command_prefix='!', intents=intents)

    cogsExtensions = []
    


    @client.event
    async def on_ready():      #function informing about bot being ready to receive commands
        await client.change_presence(activity = discord.Game('Subscribe'))      ## albo activity = discord.Activity(type = discord.ActivityType.listening, name= 'song name') ### activity=discord.Streaming(name='nazwa np. Minecraft', url='link streama np. na YT') jesli na twitch to daje guzik do przeniesienia na twitch
        for extension in cogsExtensions:
            await client.load_extension(extension)
        print("The bot is ready to work.")
        print("------------------")
    
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            cogsExtensions.append("cogs." + filename[:-3])
            
        
     
    client.run('MTI2MTMzOTQ4MjgxMzEwNDEzOQ.GXQhVh.0XgmlFBVuDbIe4LJzxg-JcQ4cQ-0W_R_3DxuqQ')
        
if __name__ == "__main__":
    run()

    

