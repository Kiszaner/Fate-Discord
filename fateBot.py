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
	    await client.say(f"{emojis}")
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
    authorComplete = str(ctx.message.author)
    authorSimple = authorComplete.partition("#")[0]
    pic_dir = f"./characters/{authorSimple}.png"
    #pic_dir = f"./characters/{str(ctx.message.author)}.png"
    if path.isfile(pic_dir):
        await client.send_file(ctx.message.channel, pic_dir)
    else:
        await client.say("Character not found.")

@client.command(pass_context=True)
async def character(ctx, user):
	"""Sends the character picture of the user specified."""
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
	""" Mutes every player but the GM. """
	if not has_role(ctx.message.author, "GM"):
		await client.say("You need to be GM to run this command.")
	else:
		chan_mem = ctx.message.author.voice.voice_channel.voice_members
		for mem in chan_mem:
			if not has_role(mem, "GM"):
				await client.say("People muted:")
				await client.say(mem)
				await client.server_voice_state(mem, mute=True)

@client.command(pass_context=True)
async def unmuteall(ctx):
	""" Umutes every player in the channel. """
	if not has_role(ctx.message.author, "GM"):
		await client.say("You need to be GM to run this command.")
	else:
		chan_mem = ctx.message.author.voice.voice_channel.voice_members
		for mem in chan_mem:
			await client.say("People unmuted:")
			await client.say(mem)
			await client.server_voice_state(mem, mute=False)

@client.command(pass_context=True)
async def setpic(ctx):
    """ Sets this player's picture """

    #ToDo: save url in the json
    if len(ctx.message.attachments) > 1:
        await client.say("Please, send just one single file.")
    else:
    	for attachment in ctx.message.attachments:
            pic_url = attachment["url"]
            await client.say(pic_url)

def has_role(member, ref_role):
	for role in member.roles:
		if role.name == ref_role:
			return True
	return False

#def set_picture(url):

client.run(cfg.TOKEN)
