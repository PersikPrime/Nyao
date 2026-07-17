import disnake
import random
from disnake.ext import commands

ANSWERS = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

class EightBall(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="8ball", description="Ask the magic 8-ball a question 🎱")
    async def eight_ball(self, inter: disnake.ApplicationCommandInteraction, question: str):
        answer = random.choice(ANSWERS)
        embed = disnake.Embed(
            title="🎱 Magic 8-Ball",
            description=f"**Question:** {question}\n**Answer:** {answer}",
            color=0xFFB6C1
        )
        await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(EightBall(bot))