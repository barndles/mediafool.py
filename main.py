import discord

from discord.ext import commands
import os
import random
import numpy as np
from openpyxl import load_workbook
import requests as rs

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
bot.run(token)


