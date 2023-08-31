import discord
import os
from run_server import serve
from versions.v1 import find_movie, movie_details

from versions.v2.utils import get_query_list, get_movie_detail_query

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as user {0.user}'.format(client))

@client.event
async def on_message(message):

  if message.author == client.user:
    return

  if message.content.startswith('!search'):

    content = message.content
    param = content.split(' ',1)[1]
    print("search log: ", param)
    try:
      await message.channel.send(get_query_list(param))
    except Exception as e:
      await message.channel.send(f"Oops! Can't find any search results for {param}")

  if message.content.startswith('!details'):

    content = message.content
    param = content.split(' ',1)[1]
    print("details log: ",param)

    try:
      await message.channel.send(get_movie_detail_query(param))
    except Exception as e:
      await message.channel.send("No thoughts in my head at the moment")
      print(str(e))

serve()
client.run(os.environ['TOKEN'])
