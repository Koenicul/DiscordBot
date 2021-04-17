from discord.ext import commands
import json

huiswerk = {}

with open('huiswerk.json', 'r') as file:
    huiswerk = json.load(file)

def save():
    with open('huiswerk.json', 'w') as file:
        file.write(json.dumps(huiswerk))

@commands.command(name="HwReset", help="Reset homework file")
async def HwReset(ctx):
    if ctx.message.author.id == 431360318942216192:
        huiswerk.clear()
        save()
        return await ctx.send("Homework has been reset")

@commands.command(name="HwAdd", help="Add homework")
async def HwAdd(ctx, Subject="", Exercise=""):
    if not Subject.lower() in huiswerk:
        huiswerk[Subject.lower()] = []
    if Exercise in huiswerk[Subject.lower()]:
        return await ctx.send("Subject already exist")

    huiswerk[Subject.lower()].append(Exercise)
    await ctx.send('"{}" was added to {}'.format(Exercise, Subject))
    save()

@commands.command(name="HwShow", help="Show homework")
async def HwShow(ctx, Subject=""):
    if Subject.lower() in huiswerk:
        await ctx.send(huiswerk[Subject.lower()])
    else:
        await ctx.send("This subject doesn't exist")

@commands.command(name="HwRemove", help="Remove homework")
async def HwRemove(ctx, Subject="", Exercise=""):
    if not Subject.lower() in huiswerk:
        return await ctx.send("This subject doesn't exist")
    try:
        huiswerk[Subject.lower()].remove(Exercise)
        save()
        return await ctx.send('"{}" has been removed from {}'.format(Exercise, Subject))
    except ValueError:
        return await ctx.send("This exercise doesn't exist")

def setup(bot):
  bot.add_command(HwAdd)
  bot.add_command(HwShow)
  bot.add_command(HwRemove)
  bot.add_command(HwReset)