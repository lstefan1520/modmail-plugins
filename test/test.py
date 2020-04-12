import discord
from discord.ext import commands, tasks, guild, context

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)

    @command.command()
    @commands.has_permissions(manage_roles=True)
    async def say(self, ctx, *, arg):
        await ctx.send(arg)


def setup(bot):
    bot.add_cog(MyCog(bot)) 
