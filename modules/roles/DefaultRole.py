import discord
from discord.ext import commands
from config.settings import default_role


class DefaultRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name=default_role)
        await self.bot.add_roles(member, role)
