import discord
from discord.ext import commands
import os
from ..settings.config import settings

class Bot(commands.Bot):
    def __init__(self):
            super().__init__(
                command_prefix=settings["TOKEN"],
                intents=discord.Intents.all()
        )
bot = Bot()

def load_extensions(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(".py"):
                folder = os.path.relpath(root, path)
                cogs = f"src.cogs.{folder.replace(os.sep, '.')}.{filename[:-3]}"
                bot.load_extension(cogs)
                
load_extensions("./src/cogs")

bot.run(settings["TOKEN"])