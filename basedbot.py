# basedbot.py
import os
import discord
import yaml
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

# @client.event
# async def on_ready():
#     guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )


def addreq(req):
    with open('./requests.yaml', 'r') as file:
        requests = yaml.load(file, Loader=yaml.FullLoader)
        requests.append(req)
    with open('./requests.yaml', 'w') as f:
        yaml.dump(requests, f)
        resp = f"Added {req}!"
    return resp

def getreq():
    with open('./requests.yaml') as file:
        requests = yaml.load(file, Loader=yaml.FullLoader)
        retstr = f'Active Requests: {len(requests)} \n---\n'
        for req in requests:
            retstr += req + '\n'
    return retstr


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!reqs':
        await message.channel.send(getreq())
        return

    if message.content.startswith('!request'):
        await message.channel.send(addreq(message.content[9:]))
        return

    if message.content.startswith('!req'):
        await message.channel.send(addreq(message.content[5:]))
        return


client.run(TOKEN)
