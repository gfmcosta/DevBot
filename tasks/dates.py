from discord.ext import commands, tasks
import datetime

class Dates(commands.Cog):
    """Works with Dates"""
    
    def __init__(self,bot):
        self.bot = bot
    
    #Start counting datetime. Command -> !datahoje
    @commands.command(name="datahoje", help="Mostra a data e hora de 2 em 2 segundos (Não requer Argumentos)")
    async def start_stop_datenow(self, ctx):
        #True
        if self.current_time.is_running():
            self.current_time.stop()
            name =  ctx.author.name
            response= "Data e Hora parado por: " + name
            await ctx.send(response)
        #False
        else:
            self.current_time.start()
            name =  ctx.author.name
            response= "Data e Hora começado por: " + name
            await ctx.send(response)

    #Task Example. Return the dateTime in (2 seconds)
    @tasks.loop(seconds=2)
    async def current_time(self):
        now = datetime.datetime.now()

        now= now.strftime("%d/%m/%Y às %H:%M:%S")

        channel = self.bot.get_channel(889931036950151188)

        await channel.send("Data atual: " + now)

def setup(bot):
    bot.add_cog(Dates(bot))
