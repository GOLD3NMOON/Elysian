import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ping", description= "veja o ping do bot", guild_ids=[1078379189100626000])
    async def ping_slash(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f'🏓Pong! Latência: {latency}ms',ephemeral=True)

    @commands.command(name="ping")
    async def ping_prefix(self, ctx: commands.Context):
        latency = round(self.bot.latency * 1000)
        await ctx.send(content=f"🏓Pong! Latência: {latency}ms")

def setup(bot):
    bot.add_cog(Ping(bot))