import discord
from discord.ext import commands

class Talks(commands.Cog):
    """Talks with user"""

    def __init__(self,bot):
        self.bot = bot
    
    #Command to say "Hi" to the users. Command -> !ola
    @commands.command(name="ola", help="Envia um Olá ao utilizador (Não requer Argumentos)")
    async def say_hello(ctx):
        name =  ctx.author.name
        response= "Olá, " + name
        await ctx.send(response)

#Command send a default message to the person who call it. Command -> !jabu
    @commands.command(name="jabu", help="Envia mensagens pré definidas ao utilizador (Não requer Argumentos)")
    async def jabu(self, ctx):
        try:
            await ctx.author.send("És gay :D")
            await ctx.author.send("O atsoc24 é o melhor configurador do mundo :P")
            await ctx.author.send("IP sacado com sucesso. Have fun!")
        except discord.errors.Forbidden:
            await ctx.send("Não é possível enviar mensagem, " + ctx.author.name)

def setup(bot):
    bot.add_cog(Talks(bot))
