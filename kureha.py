import discord
import logging
import nest_asyncio

logging.basicConfig(level=logging.INFO)
nest_asyncio.apply()
kver = '0.1'
kverdt = '\n9/15/21'

TOKEN='Token'

client = discord.Client()

@client.event
async def on_ready():
    print('Bot user {0.user} is online'.format(client))
    
@client.event
async def on_message(message):
    if str(message.author) == 'nkdv#4125':
            
        if message.content.startswith('ut04'):
            await message.channel.send('Red power node Isolated!')
            
        elif message.content.startswith('e1m1'):
            await message.channel.send('Until it is done.')
            
    if message.content == 'kd':
        await message.channel.send('Hey! Thats my command prefix!')
            
    elif message.content.startswith('kdversion'):
        await message.channel.send('Version ' + kver + kverdt)
    
    elif message.content.startswith('kdhelp'):
        await message.channel.send('https://puu.sh/IaRyY/46a81cad2f.png')
         
client.run(TOKEN)