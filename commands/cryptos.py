from discord.ext import commands
import requests

class Cryptos(commands.Cog):
    """Works with Cryptocurrency """
    
    def __init__(self,bot):
        self.bot = bot
    
    #Command return the value of 2 coins. Command -> !binance (Virtual coin) (coin)
    @commands.command(help="Verifica o preço de uma moeda virtual com moeda real. Argumentos: moeda, base")
    async def binance(self, ctx, coin, base):
        try:
            response = requests.get(f"https://www.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
            data = response.json()
            price = data.get("price")
            if price:
                await ctx.send(f"O valor do par {coin}/{base} é {price}")
            else:
                await ctx.send(f"O par {coin}/{base} é inválido")
        except Exception as error:
            await ctx.send("Erro. Tente novamente mais tarde ou comunique a um administrador.")
            print(error)

def setup(bot):
    bot.add_cog(Cryptos(bot))
