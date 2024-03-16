import discord

from discord.ext import commands
import json
import os
import random


bot = commands.Bot()
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

barndles = 266000735454363649
slime = 496765197575520270

#token = str(os.getenv("TOKEN"))

maps = ["1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "farewell", "cosmic column", "sentient forest", "pumber", "java's crypt", "the tower (XVI)", "starlight station", "mango mesa", "flying battery", "the core problem", "hydroshock", "subway neon", "meaningless contraptions", "golden alleyway", "system.invalidmapexception", "skyline usurper", "clockwork", "plasma reactor", "floating point", "psychokinetic", "ivory", "sex", "solar express", "nelumbo", "heart of the storm", "ultra difficult", "glyph", "flavors of pi", "cryoshock", "chromatic complex", "fractured iridescence", "ngmhs", "7d1d", "mauve", "solaris", "madeline votes in the US presidential election", "ufo nest", "waterbear mountain", "run for freedom", "d1d7", "cpvl", "lxvi", "sapphire dash", "vivid abyss", "avian ascension", "magnetic dawn", "Mature Grape+", "5b garbage version", "cycle madness garbage version", "Darkmoon Ruins", "summit down-side"] 

descriptors = ["good", "made by slime", "made by leviathan", "a collab", "with theo", "with two theos", "with reverse theo", "morbius", "the D side", "etselec", "it requires not being single", "hist", "slinky tries to golden it until they die", "you are limited to one dash direction", "its gay", "literally impossible", "oshiro", "I forgot", "I forgor 💀", "techspam", "not techspam", "one random room is gm", "its 10x as long", "inputs are reversed", "its in neko atsume", "dropzle", "with retention", "dultra spam", "bad", "rcb spam", "with gravityhelper", "beginner", "dashless", "with 6 dashes", "no refills", "golden is required", "with crouch climbs", "with uncrouched climbs", "gm", "gm-4", "gm+2", "one room", "zero rooms", "without any of the features that make it unique", "in minecraft", "from the hit video game celeste", "it’s the urban dictionary definition of pumber", "it’s a screenshot of the end of pumber 04 (phase) taken by cookie", "mixed with " + random.choice(maps), "lots of 1fs (makes it hard)", "lots of 1fs (makes it easy)", "unfun", "fun", "with a golden room", "intro car", "garbage version", "not rta viable", "harder than acheron", "banned in 12 countries", "harder than 7c", "blindfolded", "it's a first-person shooter", "it's 2k3", "with screenshake", "without Madeline", "summit down-side", "if you die in the game you die in real life", "if you die in real life you die in the game", "but made by glue", "but do 5 push-ups every time you die"]

@bot.event
async def on_ready():
    print(f"WE'RE LOGGED IN BOYS")
    #os.chdir(r'/home/barndles/Documents/discord-bots/mediafool')


@bot.slash_command(name="mapidea", description = "generate a fun new map idea!!!!!!!!")
async def mapidea(ctx):
    if random.randint(0, 200)==1:
        await ctx.respond("map idea: ")
        await ctx.send(file=discord.File('./pumber.png'))
    elif random.randint(0,10)==1:
        await ctx.respond("map idea: " + random.choice(maps) + " but " + random.choice(descriptors) + " and " + random.choice(descriptors))
    else:
        await ctx.respond("map idea: " + random.choice(maps) + " but " + random.choice(descriptors))

@bot.slash_command(name="glueidea", description = "generate a fun new glue idea!!!!!!!!")
async def glueidea(ctx):
    await ctx.respond("glue idea: glue" + " but " + random.choice(descriptors))

#send random glue pic
@bot.slash_command(name="glue", description = "glue")
async def glue(ctx):
    #pic = random.choice(os.listdir("/home/barndles/Documents/discord-bots/mediafool/glue-pics"))
    pic = random.choice(os.listdir('C:\\Users\\brand\\Documents\\code\\mediafool\\glue-pics\\'))

    await ctx.respond("heres a glue!!")
    #await ctx.send(file=discord.File("/home/barndles/Documents/discord-bots/mediafool/glue-pics/"+ pic))
    await ctx.send(file=discord.File('C:\\Users\\brand\\Documents\\code\\mediafool\\glue-pics\\'+ pic))
    
@bot.slash_command(name="percy", description = "percy")
async def percy(ctx):
    pic = random.choice(os.listdir("C:\\Users\\brand\\Documents\\code\\mediafool\\percy-pics\\"))

    await ctx.respond("heres a percy!!")
    await ctx.send(file=discord.File("C:\\Users\\brand\\Documents\\code\\mediafool\\percy-pics\\"+ pic))
bot.run(token)
