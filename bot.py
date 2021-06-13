import os
from dotenv import load_dotenv
load_dotenv()
from discord.ext import commands
from discord.ext.commands import CommandNotFound

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

bot = commands.Bot(command_prefix=os.getenv("Prefix"), case_insensitive=True, help_command= help_command)

@bot.event
async def on_ready():
    print("logged in as {}".format(bot.user.name))

@bot.event
async def on_command_error(error):
    if isinstance(error, CommandNotFound):
      return
    raise error

bot.load_extension("Commands.abcFormule")
bot.load_extension("Commands.Homework")
bot.load_extension("Commands.Song")
bot.run(os.getenv("Token"))