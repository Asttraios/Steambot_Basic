import discord
from discord.ext import commands
import requests
import json

class Steam(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.command()                                                                     ### CREATE EMBED
    async def steamsearch(self, ctx, *term: str):                             

        term = ' '.join(term)
        url_search = f"https://steam2.p.rapidapi.com/search/{term}/page/1"
        
        headers = {
	        "x-rapidapi-key": "89247a05dbmshdf91d7767882854p1e1144jsn856d0af8a875",         
	        "x-rapidapi-host": "steam2.p.rapidapi.com"
        }

        try:
            
            search_response = requests.get(url_search, headers=headers)
            search_data = json.loads(search_response.text)

            url_game_detail = f"https://steam2.p.rapidapi.com/appDetail/{search_data[0]['appId']}"             ### LIST INDEX OUT OF RANGE


            detail_response = requests.get(url_game_detail, headers=headers)

            detail_data = json.loads(detail_response.text)              ### UNBOUND ERROR 
        
            img_url = f"https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/{search_data[0]['appId']}/header.jpg"
        
            embed = discord.Embed(
                colour = 0xffffff, 
                title = search_data[0]['title'], 
                url = f"https://store.steampowered.com/app/{search_data[0]['appId']}", 
                description = detail_data['description']
                )
            embed.set_author(name = "Steam", icon_url = "https://cdn.icon-icons.com/icons2/2428/PNG/512/steam_black_logo_icon_147078.png")
            embed.set_image(url = img_url)
            embed.add_field(name = "Studio", value = detail_data['developer']['name'], inline = True)        ### CHANGE POSITION OF FIELDS TO MAKE IT MORE SYMMETRIC
            embed.add_field(name = "Price", value = detail_data['price'], inline = True)                      
            embed.add_field(name = "Publisher", value = detail_data['publisher']['name'], inline=True)
            embed.add_field(name = "Release Date", value = detail_data['released'], inline=True)
            embed.add_field(name = "Steam Review", value = search_data[0]['reviewSummary'], inline = False)
        
            await ctx.send(embed=embed)
        except IndexError:
            await ctx.send("Game not found. Maybe there's spelling mistake")
        except UnboundLocalError:
            await ctx.send("Game not found. Maybe there's spelling mistake")
        except Exception:
            await ctx.send("Game not found. Maybe there's spelling mistake")
            
        
        ### TO ADD
        ### METACRITIC 
        ### LINK TO YT TRAILER?
        

    
async def setup(client):
    await client.add_cog(Steam(client))
        
    



