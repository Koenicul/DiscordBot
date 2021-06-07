from discord import channel
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from pafy import new

urls = []
servers = []
currentSong = []
queue = []
ffmpeg_opts = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
isPaused = False

@tasks.loop(seconds = 1)
async def myLoop(ctx):
    if not servers[0].is_playing() and len(queue) > 0  and not isPaused:
        servers[0].play(FFmpegPCMAudio(queue[0], **ffmpeg_opts))
        currentSong.append(queue[0])
        queue.remove(queue[0])
        await ctx.send("Now playing: " + currentSong[0])

@tasks.loop(seconds = 1)
async def popSong():
    if not servers[0].is_playing() and not isPaused:
        urls.remove(urls[0])
        currentSong.clear()

@commands.command(pass_context=True,name="Play", help="Plays audio.")
async def Play(ctx, url):
    if not ctx.message.guild.voice_client:
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        servers.append(voice)
        popSong.start()
        myLoop.start(ctx)
    video = new(url)
    audio = video.getbestaudio().url
    urls.append(audio)
    if not servers[0].is_playing() and not len(currentSong) > 0:
        currentSong.append(url)
        await Songs(ctx, audio)
    else:
        queue.append(audio)
        await ctx.send("Added to queue.")

async def Songs(ctx, audio):
    servers[0].play(FFmpegPCMAudio(audio, **ffmpeg_opts))
    servers[0].is_playing() 
    await ctx.send("Now playing: " + currentSong[0])

@commands.command(name="Die", help="Disconnects the bot.")
async def Die(ctx):
    try:
        server = ctx.message.guild.voice_client
        await server.disconnect()
        await ctx.send("k")
    except:
        await ctx.send("Currently not in a VC")

@commands.command(name="Pause", help="Pauses music.")
async def Pause(ctx):
    if ctx.message.guild.voice_client:
        if servers[0].is_playing():
            servers[0].pause()
            global isPaused
            isPaused = True
            await ctx.send("Paused music.")
        else:
            await ctx.send("There is no music playing.")
    else:
        await ctx.send("Bot is not connected.")

@commands.command(name="Resume", help="Resumes music.")
async def Resume(ctx):
    if ctx.message.guild.voice_client:
        if len(currentSong) > 0:
            if not servers[0].is_playing():
                servers[0].resume()
                global isPaused
                isPaused = False
                await ctx.send("Resumed music.")
            else:
                await ctx.send("There is no music playing.")
        else:
            ctx.send("Music is already playing.")
    else:
        await ctx.send("Bot is not connected.")

def setup(bot):
    bot.add_command(Play)
    bot.add_command(Die)
    bot.add_command(Pause)
    bot.add_command(Resume)