import discord
from discord.ext import commands

class Images(commands.Cog):
    """Works with Images """
    
    def __init__(self,bot):
        self.bot = bot
    
    #Command to generate a Discord card with some informations. Command -> !foto
    @commands.command(name="foto", help="Mostra imagens random e algumas informações da mesma (Não requer Argumentos)")
    async def get_random_image(self, ctx):
        url_image = "https://picsum.photos/1920/1080"
        embed_image = discord.Embed(
            title = "Resultado da procura de imagem",
            description = "Esta procura é aleatória",
            color= 0x0000FF
        )
        embed_image.set_author(name=self.bot.user, icon_url= self.bot.user.avatar_url)
        embed_image.set_footer(text="Feito por " + self.bot.user.name, icon_url= self.bot.user.avatar_url)
        embed_image.add_field(name="API", value= "Estou a consumir uma api de imagens")
        embed_image.add_field(name="Parametros", value="{largura}/{altura}")
        embed_image.add_field(name="Exemplo xpto", value= url_image, inline=False)
        embed_image.set_image(url=url_image)
        await ctx.send(embed=embed_image)

def setup(bot):
    bot.add_cog(Images(bot))
