import discord
from discord.ext import commands
import os
import random
import numpy as np
from openpyxl import load_workbook
import requests as rs
from openai import OpenAI

mapIdeaURL = "https://docs.google.com/spreadsheets/d/1WCC6GrLwaDmcQtINrCU2SEmjKpBJcWqX5AWDenl4hvY/export?format=xlsx&id=1WCC6GrLwaDmcQtINrCU2SEmjKpBJcWqX5AWDenl4hvY"

def load_sheet(url):
    url=mapIdeaURL

    res = rs.get(url=url)
    open('maps_and_descriptors.xlsx', 'wb+').write(res.content)

    wb = load_workbook(filename="maps_and_descriptors.xlsx")
    sheet = wb.active
    return sheet
def random_map():
    sheet = load_sheet(mapIdeaURL)
    maps = sheet['A']
    map = None # Pick a random map, if it's "None", Try again
    while map == None:
        map = maps[np.random.randint(0,len(maps))].value
        if map != None:
            break
    return map
def random_descriptor():
    sheet = load_sheet(mapIdeaURL)
    descriptors = sheet['B']
    descriptor = None # Pick a random map, if it's "None", Try again
    while descriptor == None:
        descriptor = descriptors[np.random.randint(0,len(descriptors))].value
        if descriptor != None:
            break
    return descriptor

load_sheet(mapIdeaURL)

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
    
    load_sheet(mapIdeaURL)

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

@bot.slash_command(name="buffy", description = "buffy")
async def buffy(ctx):
    pic = random.choice(os.listdir("/home/mediafool.py/mediafool.py/buffy-pics/"))

    await ctx.respond("heres a buffy!!")
    await ctx.send(file=discord.File("/home/mediafool.py/mediafool.py/buffy-pics/"+ pic))

@bot.slash_command(name="niña", description = "niña")
async def niña(ctx):
    pic = random.choice(os.listdir("/home/mediafool.py/mediafool.py/nina-pics/"))

    await ctx.respond("heres a niña!!")
    await ctx.send(file=discord.File("/home/mediafool.py/mediafool.py/nina-pics/"+ pic))

@bot.slash_command(name="snoopy", description = "snoopy")
async def niña(ctx):
    pic = random.choice(os.listdir("/home/mediafool.py/mediafool.py/snoopy-pics/"))

    await ctx.respond("heres a snoopy!!")
    await ctx.send(file=discord.File("/home/mediafool.py/mediafool.py/snoopy-pics/"+ pic))

@bot.slash_command(name="meow", description = "meow")
async def meow(ctx):
    meow = "m"
    meow_letters = ['m','m','r','r','e','e','e','e','o','o','o','o','i','i','w','i','u']
    meow_lengths = [2,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,6,6,7,13]
    meow_length = random.choice(meow_lengths)

    for x in range(0,meow_length):
        meow += random.choice(meow_letters)

    await ctx.respond(meow)


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
    try: 
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
    except:
        await ctx.respond("This command failed 😔", ephemeral=True)

@bot.slash_command(name="resource", description = "gives a link to the requested Celeste resource. ex: hist, fwg spreadsheet, etc")
@discord.option(name="resource", description="the thing that you want a link to. (ex: hist, fwg spreadsheet, fwg collectors, modded golden list)")
async def resource(ctx, resource: str):
    match resource:
        case 'hist' | 'hard list' | 'hardlist': await ctx.respond("https://docs.google.com/spreadsheets/d/1A88F3X2lOQJry-Da2NpnAr-w5WDrkjDtg7Wt0kLCiz8")
        case 'leaderboard': await ctx.respond("https://www.speedrun.com/celeste")
        case 'gist' | 'garden list': await ctx.respond("https://docs.google.com/spreadsheets/d/1VVIcfkpQsRYQsNmUeM1Uti2G0En6ba6o2cXrGoE-bKM")
        case 'fwg spreadsheet' | 'spreadsheet' | 'strats' | 'stratsheet': await ctx.respond("https://docs.google.com/spreadsheets/d/1HrSBQKw-L1onD2uz5lSlt6NADftpys2au5V7lf79OrM/edit?usp=sharing")
        case 'fwg collectors' | 'graduate list': await ctx.respond("https://docs.google.com/spreadsheets/d/1FesTb6qkgMz-dCn7YdioRydToWSQNTg1axFEIHU4FF8")
        case 'modded golden list' | 'tierlist' | 'mod list': await ctx.respond("https://docs.google.com/spreadsheets/d/1v0yhceinMGr5alNekOxEkYCxXcYUsbtzMRVMezxbcVY/edit")
        case _: await ctx.respond("Please provide a valid resource. ex: hist, fwg spreadsheet, fwg collectors, modded golden list, stratsheet")

    

bot.run(token)
