from discord.ext import commands
import json
import os

huiswerk = {}

with open('huiswerk.json', 'r') as file:
    huiswerk = json.load(file)

def save():
    with open('huiswerk.json', 'w') as file:
        file.write(json.dumps(huiswerk))

@commands.command(name="HwReset", help="Reset homework file")
async def HwReset(ctx):
    if ctx.message.author.name == os.getenv("OwnerID"):
        huiswerk.clear()
        save()
        return await ctx.send("Homework has been reset")
    else:
        return await ctx.send("You don't have permission")

@commands.command(name="HwAdd", help="Add homework")
async def HwAdd(ctx, Subject="", Exercise=""):
    if Exercise != "":
        if not Subject.lower() in huiswerk:
            huiswerk[Subject.lower()] = []
        if Exercise in huiswerk[Subject.lower()]:
            return await ctx.send("Subject already exist")

        huiswerk[Subject.lower()].append(Exercise)
        await ctx.send('"{}" was added to {}'.format(Exercise, Subject))
        save()
    else:
        return await ctx.send("Invalid!") 

@commands.command(name="HwShow", help="Show homework")
async def HwShow(ctx, Subject=""):
    if Subject.lower() in huiswerk:
        await ctx.send("Showing homework from {}".format(Subject))
        for x in huiswerk[Subject.lower()]:
            await ctx.send(x)
    else:
        await ctx.send("This subject doesn't exist")

@commands.command(name="HwRemove", help="Remove homework")
async def HwRemove(ctx, Subject="", Exercise=""):
    if not Subject.lower() in huiswerk:
        return await ctx.send("This subject doesn't exist")
    try:
        huiswerk[Subject.lower()].remove(Exercise)
        if len((huiswerk[Subject.lower()])) <= 0:
            huiswerk.pop(Subject.lower())
        save()
        return await ctx.send('"{}" has been removed from {}'.format(Exercise, Subject))
    except ValueError:
        return await ctx.send("This exercise doesn't exist")

@commands.command(name="HwShowAll", help="Shows all subjects with homework")
async def HwShowAll(ctx):
    if len(huiswerk) != 0:
        for x in huiswerk:
            await ctx.send(x)

def setup(bot):
    bot.add_command(HwAdd)
    bot.add_command(HwShow)
    bot.add_command(HwRemove)
    bot.add_command(HwReset)
    bot.add_command(HwShowAll)