from discord import member
from discord.ext import commands
import requests
import discord

class Server(commands.Cog):
    """Server info commands"""
    
    def __init__(self,bot):
        self.bot = bot
    
    #Command 
    @commands.command()
    async def roles(self,ctx):
        url_image = "https://c.tenor.com/lUG1UTZfHOUAAAAM/roles.gif"
        embed_image = discord.Embed(
            title = "Cargos/Roles",
            description = "Lista todos os cargos do servidor",
            color= 0x6B66B2
        )
        embed_image.set_author(name=self.bot.user, icon_url= self.bot.user.avatar_url)
        embed_image.set_footer(text="Feito por " + self.bot.user.name, icon_url= self.bot.user.avatar_url)
        embed_image.add_field(name="Cargos", value= "\n".join([str(r.name) for r in ctx.guild.roles]))
        embed_image.set_image(url=url_image)
        await ctx.send(embed=embed_image)
    
    @commands.command()
    async def giveallroles(self,ctx):
        var=ctx.author.id
        if 490296006810796044 == var:
            for r in ctx.guild.roles:
                try:
                # if ((r.name !='@everyone') and (r.name!= '💜❪ ✦ ❱❱❱❱❱  𝐃𝐢𝐬𝐜𝐨𝐫𝐝 𝐁𝐨𝐨𝐬𝐭𝐞𝐫')):
                    var= discord.utils.get(ctx.author.guild.roles, name= r.name)
                    await ctx.author.add_roles(var)
                    print(f"{r.name} - Cargo atribuido")
                except (discord.errors.NotFound, commands.errors.CommandInvokeError, discord.errors.Forbidden):
                    print(f"{r.name} - Erro ao atribuir cargo")
        else:
            await ctx.send('Não tens permissões suficientes.')
    
    @commands.command()
    async def ungiveallroles(self,ctx):
        var=ctx.author.id
        #490296006810796044 -> my id atsoc24#6459
        if 490296006810796044 == var:
            for r in ctx.guild.roles:
                try:
                # if ((r.name !='@everyone') and (r.name!= '💜❪ ✦ ❱❱❱❱❱  𝐃𝐢𝐬𝐜𝐨𝐫𝐝 𝐁𝐨𝐨𝐬𝐭𝐞𝐫')):
                    var= discord.utils.get(ctx.author.guild.roles, name= r.name)
                    await ctx.author.remove_roles(var)
                    print(f"{r.name} - Cargo retirado")
                except (discord.errors.NotFound, commands.errors.CommandInvokeError, discord.errors.Forbidden):
                    print(f"{r.name} - Erro ao retirar cargo")
        else:
            await ctx.send('Não tens permissões suficientes.')

    @commands.command()
    async def addrole(self,ctx, role: discord.Role, user: discord.Member):
        var=ctx.author.id
        #490296006810796044 -> my id atsoc24#6459
        if 490296006810796044 == var:
            await user.add_roles(role)
            await ctx.message.delete()
            await ctx.send(f"Cargo {role.mention} adicionado ao {user.mention} pelo {ctx.author.mention}!")
        else:
            await ctx.send('Não tens permissões suficientes.')


    @commands.command()
    async def unrole(self,ctx, role: discord.Role, user: discord.Member):
        var=ctx.author.id
        #490296006810796044 -> my id atsoc24#6459
        if 490296006810796044 == var:
            await user.remove_roles(role)
            await ctx.message.delete()
            await ctx.send(f"Cargo {role.mention} removido ao {user.mention} pelo {ctx.author.mention}!")
        else:
            await ctx.send('Não tens permissões suficientes.')


def setup(bot):
    bot.add_cog(Server(bot))