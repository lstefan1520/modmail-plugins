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
        categoryitsin = discord.utils.get(537807191042949131) # here you put the category the message is already in (waiting for staff)
        categorytomoveto = discord.utils.get(667604143413788672) # here you put the category you want the channel to get moved to (waiting for client)
        if discord.utils.get(user.roles, name="staff"): # checks if a staff member sent that message (do not give staff rank to a bot)
            if message.TextChannel.category_id == categoryitsin: # here it checks if the channel message was sent in the category (waiting for staff)
                channel.edit(category=categorytomoveto) # here it moves it to (waiting for client)
                
            



        

def setup(bot):
    bot.add_cog(MyCog(bot))
