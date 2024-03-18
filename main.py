import discord

from discord.ext import commands
import os
import random
import numpy as np
from openpyxl import load_workbook
import requests as rs
from openai import OpenAI

def load_sheet():
    xlsx_url="https://docs.google.com/spreadsheets/d/1WCC6GrLwaDmcQtINrCU2SEmjKpBJcWqX5AWDenl4hvY/export?format=xlsx&id=1WCC6GrLwaDmcQtINrCU2SEmjKpBJcWqX5AWDenl4hvY"

    res = rs.get(url=xlsx_url)
    open('maps_and_descriptors.xlsx', 'wb+').write(res.content)

    wb = load_workbook(filename="maps_and_descriptors.xlsx")
    sheet = wb.active
    return sheet
def random_map():
    sheet = load_sheet()
    maps = sheet['A']
    map = None # Pick a random map, if it's "None", Try again
    while map == None:
        map = maps[np.random.randint(0,len(maps))].value
        if map != None:
            break
    return map
def random_descriptor():
    sheet = load_sheet()
    descriptors = sheet['B']
    descriptor = None # Pick a random map, if it's "None", Try again
    while descriptor == None:
        descriptor = descriptors[np.random.randint(0,len(descriptors))].value
        if descriptor != None:
            break
    return descriptor


load_sheet()

bot = commands.Bot()
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

gpt = OpenAI(api_key="none", base_url="https://forward.free-chat.asia/v1")

token = str(os.getenv("TOKEN"))

@bot.event
async def on_ready():
    print(f"WE'RE LOGGED IN BOYS")


@bot.slash_command(name="mapidea", description = "generate a fun new map idea!!!!!!!!")
async def mapidea(ctx):
    
    if random.randint(0, 200)==1:
        await ctx.respond("map idea: ")
        await ctx.send(file=discord.File('./pumber.png'))

    elif random.randint(0,10) == 1:
        await ctx.respond("map idea: " + random_map() + " but " + random_descriptor() + " and " + random_descriptor())
    else:
        await ctx.respond("map idea: " + random_map() + " but " + random_descriptor())
    
    load_sheet()


@bot.slash_command(name="glueidea", description = "generate a fun new glue idea!!!!!!!!")
async def glueidea(ctx):
    await ctx.respond("glue idea: glue" + " but " + random_descriptor())

#send random glue pic
@bot.slash_command(name="glue", description = "glue")
async def glue(ctx):
    pic = random.choice(os.listdir('/home/mediafool.py/mediafool.py/glue-pics/'))

    await ctx.respond("heres a glue!!!!!!!")
    await ctx.send(file=discord.File('/home/mediafool.py/mediafool.py/glue-pics/'+ pic))
    
@bot.slash_command(name="percy", description = "percy")
async def percy(ctx):
    pic = random.choice(os.listdir("/home/mediafool.py/mediafool.py/percy-pics/"))

    await ctx.respond("heres a percy!!")
    await ctx.send(file=discord.File("/home/mediafool.py/mediafool.py/percy-pics/"+ pic))

@bot.slash_command(name="meow", description = "meow")
async def meow(ctx):
    meow = np.random.randint(1,10)
    match meow:
        case 1: await ctx.respond("meow")
        case 2: await ctx.respond("meow")
        case 3: await ctx.respond("mrrow")
        case 4: await ctx.respond("mow")
        case 5: await ctx.respond("maaaoourr")
        case 6: await ctx.respond("mmm")
        case 7: await ctx.respond("mowwow")
        case 8: await ctx.respond("mrr")
        case 9: await ctx.respond("18567 S Garland St, Boise, Idaho, United States")
        case _: await ctx.respond("mrrp")

@bot.slash_command(description = "nya")
async def nya(ctx):
    await ctx.respond("nya")

@bot.slash_command(name="explain", description = "Explains \"tech\" in \"video games\"")
@discord.option("thing", description="Thing you want explained")
@discord.option("game", description="Game name")
async def explain(ctx, thing: str, game: str):
    if len(thing)>100 or len(game)>100:
        await ctx.respond("Please keep your queries under 100 characters", ephemeral=True)
        return
    completion = gpt.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are an assistant whose primary purppose is to explain mechanics in video games. Try to respond with very varied explanations, even if they are incorrect."},
        {"role": "user", "content": f"Can you explpain what a {thing} is in {game}"}
      ]
    )
    randomname = np.random.randint(0,30)
    citation = ""
    match randomname:
        case 5: citation = "[Source: <:percy:1146429763687288965>]"
        case 10: citation = "[citation needed]"
        case 15: citation = "[Source: _cnn.com_]"
        case 20: citation = "[Source: _mediafool_]"
        case 25: citation = f"[Source: _{game.replace(' ', '')}.com_]"
    await ctx.respond(f"Q: Explain \"{thing}\" from \"{game}\". \nA: {completion.choices[0].message.content} {citation}")

bot.run(token)


