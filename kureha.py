#Kureha Discord Bot
import discord #pip install -U discord.py
import logging
import nest_asyncio #https://github.com/erdewit/nest_asyncio

logging.basicConfig(level=logging.INFO)
nest_asyncio.apply()
kver = 'v0.2.0a'
kverdt = '10/2/21'

TOKEN='' #REMEMBER TO REMOVE THIS BEFORE MAKING A COMMIT
client = discord.Client()

@client.event
async def on_ready():
    print('{} is online'.format(client.user))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for kd prefix"))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'kd':
        await message.channel.send('Hey! Thats my command prefix! For help, try kdhelp or kdcommands!')
            
    elif message.content == 'kdver' or message.content == 'kdversion':
        await message.channel.send('Kureha is running.\nVersion ' + kver + '\nVersion date ' + kverdt)
    
    elif message.content == 'kdhelp':
        await message.channel.send('Check out the commands list or other information on github: https://github.com/nkdv0/KurehaBot')
         
    elif message.content == 'kdcommands' or message.content == 'kdc':
        await message.channel.send('https://github.com/nkdv0/KurehaBot/blob/main/Commands')
    
    elif message.content.startswith('kd'):
        await message.channel.send('Unknown command! Try kdhelp or kdcommands!')
        
    elif message.contet == 'kdgit':
        await message.channel.send('https://github.com/nkdv0/KurehaBot')
        
    
        
    else:
        return
    
client.run(TOKEN)