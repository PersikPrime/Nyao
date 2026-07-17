import disnake
from disnake.ext import commands

class HelpView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=256)
    
    @disnake.ui.button(label="🖼️ Pics", style=disnake.ButtonStyle.blurple)
    async def pics_button(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        embed = disnake.Embed(
            title="Pics Commands",
            description="Here are the available commands for pics:",
            color=0xFFB6C1
        )
        embed.add_field(name="/neko", value="Get a random neko art ✨", inline=False)
        embed.add_field(name="/kitsune", value="Get a random kitsune art ✨", inline=False)
        embed.add_field(name="/waifu", value="Get a random waifu art ✨", inline=False)
        
        await inter.response.edit_message(embed=embed, view=self)
    
    @disnake.ui.button(label="🎮 Fun", style=disnake.ButtonStyle.blurple)
    async def fun_button(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        embed = disnake.Embed(
            title="Fun Commands",
            description="Here are the available commands for fun:",
            color=0xFFB6C1
        )
        embed.add_field(name="/8ball", value="Ask the magic 8-ball a question 🎱", inline=False)
        embed.add_field(name="/random", value="Get a random number from a value 🎲", inline=False)

        await inter.response.edit_message(embed=embed, view=self)
    
    @disnake.ui.button(label="❌ Close", style=disnake.ButtonStyle.red)
    async def close_button(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await inter.response.edit_message(content="Help menu closed.", embed=None, view=None)
        self.stop()


class HelpCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="help", description="Get help with the bot commands")
    async def help(self, inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(
            title="Help Commands",
            description="Click the buttons below to see different command categories.",
            color=0xFFB6C1
        )
        view = HelpView()
        await inter.response.send_message(embed=embed, view=view)

def setup(bot: commands.Bot):
    bot.add_cog(HelpCommands(bot))