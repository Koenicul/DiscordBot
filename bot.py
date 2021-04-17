import os
from dotenv import load_dotenv
load_dotenv()
import requests
import re
import json
from discord.ext import commands
import math
from discord.ext.commands import CommandNotFound

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

bot = commands.Bot(command_prefix=os.getenv("Prefix"), case_insensitive=True, help_command= help_command)

@bot.event
async def on_ready():
  print("logged in as {}".format(bot.user.name))

async def get_quote():
  response = requests.get("https://zenquotes.io/api/random").json()[0]
  return "{}-{}".format(response['q'], response['a'])

@bot.command(name="Quote", help="Inspire moment")
async def quote(ctx):
  await ctx.send(await get_quote())

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

bot.load_extension("Commands.abcFormule")
bot.load_extension("Commands.Homework")
bot.run(os.getenv("Token"))