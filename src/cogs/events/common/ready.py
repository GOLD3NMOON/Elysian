from discord.ext import commands

class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        print(f"Conectei como: {self.bot.user.name}")

def setup(bot):
    bot.add_cog(OnReady(bot))
