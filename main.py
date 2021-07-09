import discord
import os
from discord.ext import commands
import datetime
from tools.alive import keep_alive
from mod.Ban import *

bot = commands.Bot(command_prefix='b!')
bot.remove_command('help')

color = 0x45608f

@bot.event
async def on_ready():
    print("Started")

bot.run('ODYyOTMyOTE5MDM4NzcxMjAx.YOfi6A.OYGjuaT2QKEujO2PFm_vPRYI8G4')
