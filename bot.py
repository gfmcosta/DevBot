from discord.ext import commands
from decouple import config
import os
import discord

intents= discord.Intents.default()
intents.members = True

#Bot command prefix 
bot = commands.Bot("!", intents=intents)

#Function with all the commands and tasks
def load_cogs(bot):
    bot.load_extension("manager")
    bot.load_extension("tasks.dates")
    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog= file[:-3]
            bot.load_extension(f"commands.{cog}")

#Load commands and tasks
load_cogs(bot)

#Token .env
TOKEN = config("TOKEN_SECRETO")
#Need to be the last code line to run the bot
bot.run(TOKEN)