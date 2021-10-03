from discord import member
from discord.ext import commands
import requests
import discord

class Server(commands.Cog):
    """Server info commands"""
    
    def __init__(self,bot):
        self.bot = bot
    
    #Command to give all server roles to the user who use it
    @commands.command(name= "dartodoscargos", help = "Dá todos os cargos ao utilizador que o escreve. (Não requer Argumentos)")
    async def giveallroles(self,ctx):
        var=ctx.author.id
        #490296006810796044 -> my id atsoc24#6459
        if 490296006810796044 == var:
            for r in ctx.guild.roles:
                try:
                    var= discord.utils.get(ctx.author.guild.roles, name= r.name)
                    await ctx.author.add_roles(var)
                    print(f"{r.name} - Cargo atribuido")
                except (discord.errors.NotFound, commands.errors.CommandInvokeError, discord.errors.Forbidden):
                    print(f"{r.name} - Erro ao atribuir cargo")
        else:
            await ctx.send('Não tens permissões suficientes.')
    
    #Command to remove all server roles to the user who use it
    @commands.command(name= "tirartodoscargos", help = "Remove todos os cargos ao utilizador que o escreve. (Não requer Argumentos)")
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

    #Command to give a role to an user
    @commands.command(name= "darcargo", help = "Dá um determinado cargo ao utilizador que mencionar. Argumentos: Cargo, Membro")
    async def addrole(self,ctx, role: discord.Role, user: discord.Member):
        var=ctx.author.id
        #490296006810796044 -> my id atsoc24#6459
        if 490296006810796044 == var:
            await user.add_roles(role)
            await ctx.message.delete()
            await ctx.send(f"Cargo {role.mention} adicionado ao {user.mention} pelo {ctx.author.mention}!")
        else:
            await ctx.send('Não tens permissões suficientes.')

    #Command to remove a role to an user 
    @commands.command(name= "tirarcargo", help = "Tira um determinado cargo ao utilizador que mencionar. Argumentos: Cargo, Membro")
    async def unrole(self,ctx, role: discord.Role, user: discord.Member):
        var=ctx.author.id
        #490296006810796044 -> my id atsoc24#6459
        if 490296006810796044 == var:
            await user.remove_roles(role)
            await ctx.message.delete()
            await ctx.send(f"Cargo {role.mention} removido ao {user.mention} pelo {ctx.author.mention}!")
        else:
            await ctx.send('Não tens permissões suficientes.')


    #Command to kick a member
    @commands.command(help="Expulsa um utilizador. Argumentos: Membro, Motivo (opcional)")
    async def kick(self,ctx, member: discord.Member,*,reason=None):
        var=ctx.author.id
        #490296006810796044 -> my id atsoc24#6459
        if 490296006810796044 == var:
            await member.kick(reason=reason)
            await ctx.message.delete()
            await ctx.send(f'O utilizador {member} foi expulso por {ctx.author.mention}')
        else:
            await ctx.send('Não tens permissões suficientes.')


    #Command to clear messages from a channel
    @commands.command(name="limpar", help="Limpa mensages do chat. Argumentos: Quantidade (opcional)")
    async def clear(self,ctx,number=10000000000000000000000000000000000000):
        await ctx.channel.purge(limit=number)


def setup(bot):
    bot.add_cog(Server(bot))