from discord.ext import commands
import math

def floatToString(flt):
  return ('%.15f' % flt).rstrip('0').rstrip('.')

@commands.command(name="ABC", help="Calculates abc-Formula")
async def abc(ctx, a="", b="", c=""): 
  try:
    A = float(a)
    B = float(b)
    C = float(c)
  except:
    return await ctx.send("Invalid!")
  
  if A == 0:
      print("That is not a quadratic equation")
      input()
  else:
    try:
      X = (-B + math.sqrt(B**2 - 4*A*C))/(2*A)
      X2 = (-B - math.sqrt(B**2 - 4*A*C))/(2*A)
    except:
      return await ctx.send("Invalid!")
    if X != X2:
      await ctx.send("{} or {}".format(floatToString(X), floatToString(X2)))
    else:
      await ctx.send("{}".format(floatToString(X)))

def setup(bot):
  bot.add_command(abc)