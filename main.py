import os
import discord
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

meme_words = ["Lol", "Lmao", "Your Mom", "Lok", "Lop", "Lel"]
response_words = [
  "Haha soo funnyyy!",
  "LMAOOOOOOOOOOOOOOOOOOOOO",
  "That is the funniest thing heard",
  "I love milk Hhahha",
]

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return (quote)

@client.event
async def on_ready():
  print('The bot has logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
    
  if msg.startswith(';inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any (word in msg for word in meme_words):
    await message.channel.send(random.choice(response_words))


keep_alive()
client.run(os.getenv('DISCORD_BOT_SECRET'))