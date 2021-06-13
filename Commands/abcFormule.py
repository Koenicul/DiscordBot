from discord.ext import commands
import math

def floatToString(flt):
  return ('%.15f' % flt).rstrip('0').rstrip('.')

@commands.command(name="ABC", help="Calculates abc-Formula")
async def ABC(ctx, a="", b="", c=""): 
  try:
    A = float(a)
    B = float(b)
    C = float(c)
  except ValueError:
    return await ctx.send("Invalid!")
  
  if A == 0:
      await ctx.send("That is not a quadratic equation")
  else:
    D = B**2 - 4*A*C
    if D < 0:
        await ctx.send("Graph doesn't intersect")
    elif D == 0:
        X = (-B + math.sqrt(D))/(2*A)
        await ctx.send("Graph intersects at x = {}".format(floatToString(X)))
    elif D > 0:
        X = (-B + math.sqrt(D))/(2*A)
        X2 = (-B - math.sqrt(D))/(2*A)
        await ctx.send("Graph intersects at x = {} and x = {}".format(floatToString(X), floatToString(X2)))

def setup(bot):
  bot.add_command(ABC)