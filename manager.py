import asyncio
import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument

class Manager(commands.Cog):
    """Management commands"""
    
    def __init__(self,bot):
        self.bot = bot


    #Console event to know if the bot is online
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"I'm online! Logged as: {self.bot.user}")


    #Event when someone write a message
    @commands.Cog.listener()
    async def on_message(self, message):
        #Ignore the bot messages
        if message.author == self.bot.user:
            return    
        #Catch an censured word, advertise and delete
        if "puta" in message.content:
            await message.channel.send(f"Não utilize palavrões, {message.author.name} ")
            
            await message.delete()

    #Event when an error ocure.
    @commands.Cog.listener()
    async def on_command_error(self, ctx,error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send("Por favor envia todos os Argumentos. Escreva !help para ver quais os argumentos necessários.")
        elif isinstance(error,CommandNotFound):
            await ctx.send("O comando não existe. Escreva !help para ver todos os comandos.")
        else:
            raise error

    #Event when someone join the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcomechannel = self.bot.get_channel(889280444397408276)
        url_image = "https://cdn.discordapp.com/attachments/815283670616113162/891041303008247808/BareEarlyCanadagoose-size_restricted.gif"
        embed_image = discord.Embed(
            title = "Welcome",
            description = f"Sê Bem-vindo ao servidor, {member.mention}",
            color= 0x6B66B2,
        )
        embed_image.set_author(name=self.bot.user, icon_url= self.bot.user.avatar_url)
        embed_image.set_thumbnail(url=member.avatar_url)
        embed_image.set_footer(text="Feito por " + self.bot.user.name, icon_url= self.bot.user.avatar_url)
        embed_image.set_image(url=url_image)
        await welcomechannel.send(embed=embed_image)

    #Event when someone leave the server
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        welcomechannel = self.bot.get_channel(889280446444220466)
        url_image = "https://cdn.discordapp.com/attachments/815283670616113162/891041303008247808/BareEarlyCanadagoose-size_restricted.gif"
        embed_image = discord.Embed(
            title = "GoodBye",
            description = f"{member.name} saiu do servidor!",
            color= 0x6B66B2,
        )
        embed_image.set_author(name=self.bot.user, icon_url= self.bot.user.avatar_url)
        embed_image.set_footer(text="Feito por " + self.bot.user.name, icon_url= self.bot.user.avatar_url)
        embed_image.set_image(url=url_image)
        await welcomechannel.send(embed=embed_image)

def setup(bot):
    bot.add_cog(Manager(bot))
