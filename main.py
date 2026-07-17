import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!", 
    intents=intents,
    activity=disnake.Activity(type=disnake.ActivityType.watching, name="your best friend | /help"),
    status=disnake.Status.online,
    test_guilds=[1458891042500776059]
)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and not filename.startswith("__"):
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"✅ Ready: {filename}")
        except Exception as e:
            print(f"❌ Error while loading module {filename}:")
            print(e)

@bot.event
async def on_ready():
    print(f'Login successful as {bot.user.name} ({bot.user.id})')
    print('--- LOG STARTING ---')

bot.run(TOKEN)