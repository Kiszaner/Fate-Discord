import discord
import asyncio
import platform
import pandas as pd
import random
import numpy as np
import config.config as cfg
from os import path
from discord.ext.commands import Bot
from discord.ext import commands

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
async def me(ctx):
    """Sends the character picture of the user that has sent the command."""
    pic_dir = f"./characters/{str(ctx.message.author)}.png"
    if path.isfile(pic_dir):
        await client.send_file(ctx.message.channel, pic_dir)
    else:
        await client.say("Character not found.")

@client.command(pass_context=True)
async def character(ctx, user):
	"""Sends the character picture of the user specified. To obtain the user identifier
	look at the message sent when he uses the dice command. Or you can just right-click on his
	icon and click on profile (it should look like: Paco#1917"""
	pic_dir = f"./characters/{user}.png"
	if path.isfile(pic_dir):
		await client.send_file(ctx.message.channel, pic_dir)
	else:
		await client.say("Character not found.")

@client.command(pass_context=True)
async def clear(ctx):
	""" Clears every bot message from the channel. """
	await client.purge_from(ctx.message.channel, limit=200, check=lambda m: (m.author == client.user) or m.content.startswith(prefix))

@client.command(pass_context=True)
async def muteall(ctx):
	""" Mutes every player but the DJ. """
	if not has_role(ctx.message.author, "DJ"):
		await client.say("You need to be DJ to run this command.")
	else:
		for member in ctx.message.author.voice.voice_channel.voice_members:
			if not has_role(ctx.message.author, "DJ"):
				await client.server_voice_state(member, mute=True)

@client.command(pass_context=True)
async def unmuteall(ctx):
	""" Umutes every player in the channel. """
	if not has_role(ctx.message.author, "DJ"):
		await client.say("You need to be DJ to run this command.")
	else:
		for member in ctx.message.author.voice.voice_channel.voice_members:
			await client.server_voice_state(member, mute=False)

def has_role(member, ref_role):
	for role in member.roles:
		if role.name == ref_role:
			return True
	return False

client.run(cfg.TOKEN)
