import disnake
import random
from disnake.ext import commands

class Randomizer(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="random", description="Get a random number from a value 🎲")
    async def random_number(self, inter: disnake.ApplicationCommandInteraction, max_value: int):
        if max_value < 1:
            await inter.response.send_message("Please provide a positive integer greater than 0.", ephemeral=True)
            return
        
        random_num = random.randint(1, max_value)
        embed = disnake.Embed(
            title="🎲 Random Number Generator",
            description=f"Your random number between 1 and {max_value} is: **{random_num}**",
            color=0xFFB6C1
        )
        await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Randomizer(bot))