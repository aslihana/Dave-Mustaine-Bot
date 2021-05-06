import discord
import os
import random

client = discord.Client()

words_to_dave = ["dave", "peace sells","megadeth", "song"]

words_from_dave = ["Peace sells, but who's buying?", "In my hour of need ha, no, you're not there", "What do you mean, 'I don't believe in God'? I talk to him everyday", "I go to court when I have to", "Brother will kill brother spilling blood across the land", "The end is near, it's crystal clear part of the master plan", "You take a mortal man and put him in control", "Just like the Pied Piper led rats through the streets", "Swaying to the Symphony swaying to the Symphony of Destruction", "If there's a new way, I'll be the first in line"]

@client.event
async def on_ready():
  print('We logged in discord as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
 
  msg = message.content

  if message.content.startswith('$dave'):
    await message.channel.send('Hello me, its me again')
  
  if any(word in msg for word in words_to_dave):
    await message.channel.send(random.choice(words_from_dave))
client.run(os.getenv('TOKEN'))

