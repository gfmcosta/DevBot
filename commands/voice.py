from discord.ext import commands

class Voice(commands.Cog):
    """Voice channel commands"""
    
    def __init__(self,bot):
        self.bot = bot
    
    #Mute all member in a voice chat
    @commands.command(name="silenciartodos", help="Silencia todos os utilizadores no canal de voz. (Não requer Argumentos)")
    async def muteall(self,ctx):
        var=ctx.author.id
        if 490296006810796044 == var:
            vc = ctx.author.voice.channel
            for member in vc.members:
                await member.edit(mute=True)

            await ctx.send("Todos foram mutados, " +  ctx.author.mention +"!")
        else:
            await ctx.send('Não tens permissões suficientes.')

    #Unmute all member in a voice chat
    @commands.command(name="desmutartodos", help="Desmuta todos os utilizadores no canal de voz. (Não requer Argumentos)")
    async def unmuteall(self,ctx):
        var=ctx.author.id
        if 490296006810796044 == var:
            vc = ctx.author.voice.channel
            for member in vc.members:
                await member.edit(mute=False)

            await ctx.send("Todos foram desmutados, " +  ctx.author.mention +"!")
        else:
            await ctx.send('Não tens permissões suficientes.')


def setup(bot):
    bot.add_cog(Voice(bot))