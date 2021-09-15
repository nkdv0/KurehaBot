#Kureha Discord Bot
import discord #pip install -U discord.py
import logging
import nest_asyncio #https://github.com/erdewit/nest_asyncio

logging.basicConfig(level=logging.INFO)
nest_asyncio.apply()
kver = '0.1'
kverdt = '\n9/15/21'

TOKEN=''
client = discord.Client()

@client.event
async def on_ready():
    print('Bot user {} is online'.format(client.user))
    
@client.event
async def on_message(message):
    # if str(message.author) == 'nkdv#4125':
            
    #     if message.content == 'ut04':
    #         await message.channel.send('Red power node Isolated!')
            
    #     elif message.content == 'e1m1':
    #         await message.channel.send('Until it is done.')
            
    if message.content == 'kd':
        await message.channel.send('Hey! Thats my command prefix!')
            
    elif message.content == 'kdver' or 'kdversion':
        await message.channel.send('Kureha is running version ' + kver + kverdt)
    
    elif message.content == 'kdhelp':
        await message.channel.send('Check out the commands page on github: https://github.com/nkdv0/KurehaBot/blob/main/Commands')
         
    elif message.content == 'kd':
        ()
    
client.run(TOKEN)