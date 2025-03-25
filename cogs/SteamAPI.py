import os
import discord
from discord.ext import commands
import requests
import json
from dotenv import load_dotenv

# Commands related to Steam API
# Cog - Discord.py class that allows to group commands together
class Steam(commands.Cog):
    def __init__(self, client):
        self.client = client  # Initialize the class with the Discord client

    # Search for a specific game on Steam - returns game details - command: !steamsearch <game_name>
    @commands.command()  
    async def steamsearch(self, ctx, *term: str):  # Asynchronous function to handle the command
        term = ' '.join(term)  # Join the search terms into a single string
        url_search = f"https://steam2.p.rapidapi.com/search/{term}/page/1"  # Steam API URL for searching games

        load_dotenv()
        
        STEAM_KEY = os.getenv('STEAM_API_KEY')  # Load the Steam API key from the .env file

        headers = {
            "x-rapidapi-key": f"{STEAM_KEY}",  # Custom Steam API key
            "x-rapidapi-host": "steam2.p.rapidapi.com"  # Steam API host
        }

        try:
            # Make a GET request to the search URL with the headers
            search_response = requests.get(url_search, headers=headers)
            search_data = json.loads(search_response.text)  # Parse the JSON response

            # Construct the URL for the game detail endpoint using the appId from the search data
            url_game_detail = f"https://steam2.p.rapidapi.com/appDetail/{search_data[0]['appId']}"  # show first best fitting game
            detail_response = requests.get(url_game_detail, headers=headers)  # Make a GET request to the game detail URL
            detail_data = json.loads(detail_response.text)  # Parse the JSON response
        
            # Construct the URL for the game's header image
            img_url = f"https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/{search_data[0]['appId']}/header.jpg"
        
            # Create a Discord embed message with the game details
            embed = discord.Embed(
                colour = 0xffffff, 
                title = search_data[0]['title'], 
                url = f"https://store.steampowered.com/app/{search_data[0]['appId']}", 
                description = detail_data['description']
            )
            embed.set_author(name = "Steam", icon_url = "https://cdn.icon-icons.com/icons2/2428/PNG/512/steam_black_logo_icon_147078.png")
            embed.set_image(url = img_url)
            embed.add_field(name = "Studio", value = detail_data['developer']['name'], inline = True)
            embed.add_field(name = "Price", value = detail_data['price'], inline = True)
            embed.add_field(name = "Publisher", value = detail_data['publisher']['name'], inline=True)
            embed.add_field(name = "Release Date", value = detail_data['released'], inline=True)
            embed.add_field(name = "Steam Review", value = search_data[0]['reviewSummary'], inline = False)
        
            await ctx.send(embed=embed)  # Send the embed message to the Discord channel
        except IndexError:
            await ctx.send("Game not found. Maybe there's spelling mistake")  # Handle IndexError if the game is not found - search_data[] is empty
        except UnboundLocalError:
            await ctx.send("Game not found. Maybe there's spelling mistake")  # No value bound to the variable referenced in funciton
        except Exception:
            await ctx.send("Game not found. Unknown error")  # Handle any other exceptions

# Asynchronous function to add the Steam cog to the Discord bot
async def setup(client):
    await client.add_cog(Steam(client))
