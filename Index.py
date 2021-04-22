import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = '(', description = "Pa empezar resumidamente")

@bot.command()

async def verga (ctx):
	await ctx.send('comes')

@bot.command()

async def nhentai (ctx, Codigo: int, Condigo2: int):
	await ctx.send(Codigo + Condigo2)

@bot.command()

async def Hentai (ctx, Codigo: str):
	await ctx.send('https://nhentai.to/g/' + Codigo)

@bot.command()

# Bot evento en esa monda

@bot.event

async def on_ready():
	print('Arranca Hpta')


bot.run('your bot')