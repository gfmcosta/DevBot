from discord.ext import commands

class Smarts(commands.Cog):
    """Smart commands"""
    
    def __init__(self,bot):
        self.bot = bot
    
    #Command to calculate an expression. Command -> !calcular (expression)
    @commands.command(name="calcular", help="Calcula uma expressão. Argumentos: Expressão (Ex: 2+2)")
    async def calculate_expression(self, ctx, *expression):
        expression = "".join(expression)
        response = eval(expression)
        await ctx.send("A resposta é: " + str(response))

def setup(bot):
    bot.add_cog(Smarts(bot))
