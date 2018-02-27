import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import pandas as pd
import random
import numpy as np

client = Bot(description="Fate bot for discord. Made by SowlJBA", command_prefix="!", pm_help = False)

def calc_dices(n):
    results = list(np.random.choice(["+","-"," "],n))
    total = results.count("+")-results.count("-")
    return results, total

def dicesToEmojis(dices):
	rt_emojis = []
	for dice in dices:
		if dice == "+":
			rt_emojis.append("<:pluskey:415985383742898177>")
		elif dice == "-":
			rt_emojis.append("<:minuskey:415985384011464715>")
		elif dice == " ":
			rt_emojis.append("<:voidkey:415985887604899840>")
	return ' '.join(rt_emojis)

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    return await client.change_presence(game=discord.Game(name='Hosting Fate Game'))

@client.command(pass_context=True)
async def dice(ctx, n_dices=4):
	"""Lanza un número de dados definido en el comando."""
	if isinstance(n_dices, int):
	    await client.say(str(ctx.message.author)+" lanza los dados y saca...")
	    result = calc_dices(n_dices)
	    emojis = dicesToEmojis(result[0])
	    await client.say("Dados... "+emojis)
	    await client.say("Resultado total: "+str(result[1]))
	else:
		await client.say("Por favor, no seas malo con el programador, mete un número entero de dados.")

@client.command(pass_context=True)
async def map(ctx):
	""" Envía una imagen del mapa."""
	await client.say("Still working on this command.")

@client.command(pass_context=True)
async def my_character(ctx):
	"""Envía la imagen del personaje del usuario que envía el comando."""
	pic_dir = str(ctx.message.author)+".png"
	await client.send_file(ctx.message.channel, pic_dir)

@client.command(pass_context=True)
async def character(ctx, user):
	"""Envía la imagen del personaje del usuario especificado. (Para obtener el usuario deseado
	utiliza el identificador que aparece cuando lanza un dado)"""
	await client.say("Still working on this command.")

client.run('NDE1OTc4MzMwMzMyODU2MzIw.DW9xmA.DHxYPGsU9FEScFTVkF_zEKLtwPM')