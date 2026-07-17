import disnake
from disnake.ext import commands
import aiohttp

class WaifuSend(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="waifu", description="Get a random waifu art ✨")
    async def waifu(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()
        
        api_url = "https://nekos.best/api/v2/waifu"
        
        headers = {
            "User-Agent": "NyaoMaster/Dev-71726 (Contact: insertyouremailhere@gmail.com)",
            "Accept": "application/json"
        }
    
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url, headers=headers) as response:
                    print(f"Статус ответа nekos.best: {response.status}")
                    
                    if response.status == 200:
                        data = await response.json()

                        image_info = data["results"][0]
                        image_url = image_info["url"] 
                        artist_name = image_info.get("artist_name", "Unknown Artist")
                        artist_href = image_info.get("artist_href", "")
                    
                        embed = disnake.Embed(
                            title="Here's your waifu! 🌸", 
                            color=0xFFB6C1
                        )
                        embed.set_image(url=image_url)
                        
                        if artist_href:
                            embed.set_footer(text=f"Artist: {artist_name} ({artist_href})")
                        else:
                            embed.set_footer(text=f"Artist: {artist_name}")
                    
                        await inter.edit_original_message(embed=embed)
                    else:
                        await inter.edit_original_message(
                            content=f"API returned an error. Status: {response.status} 😿"
                        )
        except Exception as e:
            await inter.edit_original_message(content="Error connecting to API 😿")
            print(f"Error in waifusend: {e}")

def setup(bot: commands.Bot):
    bot.add_cog(WaifuSend(bot))