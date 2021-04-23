from discord.ext import commands
import math

@commands.command(name="MathRules", help="Cos & Sin rule")
async def MathRules(ctx, Type="", Type2="", Measure1="", Measure2="", Measure3=""):
  try:
    mes1 = float(Measure1)
    mes2 = float(Measure2)
    mes3 = float(Measure3)
  except ValueError:
    return await ctx.send("Invalid!")

  if Type.lower() == "sin":
    if Type2.lower() == "corner":
      try:
        answer = round(math.degrees(math.asin((mes1*(math.sin(math.radians(mes2))))/mes3)), 2)
      except ValueError:
        return await ctx.send("Invalid!")
    if Type2.lower() == "side":
      try:
        answer = round((mes2*math.sin(math.radians(mes1)))/(math.sin(math.radians(mes3))), 2)
      except ValueError:
        return await ctx.send("Invalid!")
    
  elif Type.lower() == "cos":
    if Type2.lower() == "corner":
      try:
        answer = round(math.degrees(math.acos((mes2**2 + mes3**2 - mes1**2)/(2*mes2*mes3))), 2)
      except ValueError:
        return await ctx.send("Invalid!")
    elif Type2.lower() == "side":
      try:
        answer = round(math.sqrt(mes2**2 + mes3**2 - 2*mes2*mes3*math.cos(math.radians(mes1))), 2)
      except ValueError:
        return await ctx.send("Invalid!")

  await ctx.send(answer)

def setup(bot):
  bot.add_command(MathRules)