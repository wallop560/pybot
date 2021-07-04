import discord
from discord.ext import commands
token = "ODYxMjAwMDgzOTg3MjAyMDQ4.YOGVFA.57mdWbbE3OAo1iJub4bI2vCkSCs"

Client = commands.Bot(command_prefix=';', case_insensitive=True)
client = discord.Client()
@Client.event
async def on_ready():
  print('Ready')

@Client.command()
async def move(ctx,member = None,channel = None):
  print(member)
  print(channel)
  member = await ctx.guild.fetch_member(int(member))    
  channel = ctx.guild.get_channel(int(channel)) 
  print(channel)
  print(member)
  await member.move_to(channel)

@Client.event
async def on_message(message):
  ctx = await Client.get_context(message)
  if ctx.valid:
    await Client.invoke(ctx)

Client.run(token)