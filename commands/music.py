import asyncio
import os
from discord import client
from discord.ext.commands.core import command
import pafy
import discord
from youtube_dl import YoutubeDL
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
import ffmpeg


class Music(commands.Cog):
    """Works with Music"""
    
    def __init__(self,bot):
        self.bot = bot
    
    
    #Command to join a room
    @commands.command(help="Entra num canal de voz. (Não requer Argumentos)")
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("Não está em nenhum canal de voz!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    #Command to disconnect from a room
    @commands.command(help="Sai de um canal de voz. (Não requer Argumentos)")
    async def leave(self,ctx):
        await ctx.voice_client.disconnect()

    #Nao esta a funcionar
    @commands.command(help="Começa a tocar uma musica. Argumentos: link")
    async def play(self,ctx, url):
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
            URL = info['url']
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            await ctx.send('Bot is playing')
        else:
            await ctx.send("Bot is already playing")
            return

    #Nao esta a funcionar
    @commands.command(help="Pausa a música. (Não requer Argumentos)")
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send('Em pausa ⏸')

    #Nao esta a funcionar
    @commands.command(help="Volta a reproduzir a música. (Não requer Argumentos)")
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send('A reproduzir ⏯')

def setup(bot):
    bot.add_cog(Music(bot))
