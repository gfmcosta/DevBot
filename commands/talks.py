import discord
from discord.ext import commands

class Talks(commands.Cog):
    """Talks with user"""

    def __init__(self,bot):
        self.bot = bot
    
    #Command to say "Hi" to the users. Command -> !ola
    @commands.command(name="ola", help="Envia um Olá ao utilizador (Não requer Argumentos)")
    async def say_hello(self,ctx):
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

    #Command that shows to an user your own info
    @commands.command(name="minhainfo", help="Mostra informações úteis ao utilizador (Não requer Argumentos)")
    async def myinfo(self,ctx):
        date_format = "%d/%m/%Y às %H:%M:%S"
        url_image = "https://c.tenor.com/0ctrlakU1OUAAAAM/information-glitch.gif"
        embed_image = discord.Embed(
            title = "Informação",
            description = f"Perfil do {ctx.author.mention}",
            color= 0x6B66B2
        )
        embed_image.set_author(name=self.bot.user, icon_url= self.bot.user.avatar_url)
        embed_image.set_thumbnail(url=ctx.author.avatar_url)
        embed_image.set_footer(text="Feito por " + self.bot.user.name, icon_url= self.bot.user.avatar_url)
        embed_image.add_field(name="Cargos", value= "\n".join([str(r.mention) for r in ctx.author.roles if r.name != "@everyone"]))
        embed_image.add_field(name="Criado em: ", value={ctx.author.created_at.strftime(date_format)})
        embed_image.add_field(name="Entrou em: ", value={ctx.author.joined_at.strftime(date_format)})
        embed_image.set_image(url=url_image)
        await ctx.send(embed=embed_image)

    #Command that list all server roles
    @commands.command(name="cargos", help="Lista todos os Cargos do servidor. (Não requer Argumentos)")
    async def roles(self,ctx):
        url_image = "https://c.tenor.com/lUG1UTZfHOUAAAAM/roles.gif"
        embed_image = discord.Embed(
            title = "Cargos/Roles",
            description = "Lista todos os cargos do servidor",
            color= 0x6B66B2
        )
        embed_image.set_author(name=self.bot.user, icon_url= self.bot.user.avatar_url)
        embed_image.set_footer(text="Feito por " + self.bot.user.name, icon_url= self.bot.user.avatar_url)
        embed_image.add_field(name="Cargos", value= "\n".join([str(r.name) for r in ctx.guild.roles if r.name != "@everyone"]))
        embed_image.set_image(url=url_image)
        await ctx.send(embed=embed_image)


def setup(bot):
    bot.add_cog(Talks(bot))
