import discord
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_message(message):
  html = urlopen("http://www.ece.uci.edu/")  
  bsObject = BeautifulSoup(html, "html.parser") 
  table = bsObject.find('table')
  
    # we do not want the bot to reply to itself
  if message.author == client.user:
        return

  if message.content.startswith('!hello'):
        await message.channel.send('hello')

  if message.content.startswith('!server'): 
    trs = table.find_all('tr')
    await message.channel.send('Server                             Load Average')
  for idx, tr in enumerate(trs):
    if idx > 0:
      tds = tr.find_all('td')
      sequence = tds[0].text.strip() 
      description = tds[1].text.strip()
      result = sequence, description
      await message.channel.send(result)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.getenv('TOKEN'))
