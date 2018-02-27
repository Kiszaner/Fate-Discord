import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import pandas as pd
import random
import numpy as np
from os import path

prefix="!"
client = Bot(description="Fate bot for discord.", command_prefix=prefix, pm_help = False)

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
    print(f'Logged in as {client.user.name} (ID:{client.user.id}) | Connected to {str(len(client.servers))} servers | Connected to {str(len(set(client.get_all_members())))} users')
    return await client.change_presence(game=discord.Game(name='Hosting Fate Game'))

@client.command(pass_context=True)
async def dice(ctx, n_dices=4):
	"""Sends a predefined number of dices."""
	if isinstance(n_dices, int):
	    await client.say(f"{str(ctx.message.author)} throws the dices and gets...")
	    result = calc_dices(n_dices)
	    emojis = dicesToEmojis(result[0])
	    await client.say(f"Dices... {emojis}")
	    await client.say(f"Total result: {str(result[1])}")
	else:
		await client.say("Please enter an integer number of dices.")

@client.command(pass_context=True)
async def map(ctx):
	""" Sends the map image."""
	await client.say("Still working on this command.")

@client.command(pass_context=True)
async def my_character(ctx):
    """Sends the character picture of the user that has sent the command."""
    pic_dir = f"./characters/{str(ctx.message.author)}.png"
    if path.isfile(pic_dir):
        await client.send_file(ctx.message.channel, pic_dir)
    else:
        await client.say("character not found.")

@client.command(pass_context=True)
async def character(ctx, user):
	"""Sends the character picture of the user specified. (To obtain the user identifier
	look at the message sent when he uses the dice command)"""
	await client.say("Still working on this command.")

@client.command(pass_context=True)
async def clear(ctx):
	""" Clears every bot message from the channel. """
	await client.purge_from(ctx.message.channel, limit=200, check=lambda m: (m.author == client.user) or m.content.startswith(prefix))

client.run('NDE1OTc4MzMwMzMyODU2MzIw.DW9xmA.DHxYPGsU9FEScFTVkF_zEKLtwPM')
