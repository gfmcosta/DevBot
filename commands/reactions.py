from discord.ext import commands

class Reactions(commands.Cog):
    """Works with Reactions"""
    
    def __init__(self,bot):
        self.bot = bot
    
    #Event to give roles with a default reaction
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "👍":
            print(user)
            role = user.guild.get_role(889280422364721152)
            await user.add_roles(role)

def setup(bot):
    bot.add_cog(Reactions(bot))
