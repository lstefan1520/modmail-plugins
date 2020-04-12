import discord
from discord.ext import commands
from discord import guild

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.send(message)
    
    @commands.Cog.listener()
    # this is where it checks when a message is sent if the message is in one of the channels under waiting for staff and if the message sent is from a staff channel will be moved to waiting for client
    async def on_message(self, message):
        channel = message.channel
        user = message.author
        categoryitsin = discord.utils.get(discord.Guild.categories, id=698826755397648414)
        categorytomoveto = discord.utils.get(discord.Guild.categories, id=698826780798222386)
        if discord.utils.get(user.roles, name="staff"):
            if message.channel.category == categoryitsin:
                channel.edit(category=categorytomoveto)
                
            



        

def setup(bot):
    bot.add_cog(MyCog(bot))
