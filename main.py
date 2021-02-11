import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()


def get_quote():
    response = requests.get("https://www.breakingbadapi.com/api/quote/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['quote'] + "\n— " + json_data[0]['author']
    return (quote)


def get_death():
    response = requests.get("https://breakingbadapi.com/api/random-death")
    json_data = json.loads(response.text)
    print(json_data)
    name = json_data['death'].upper()
    cause = json_data['cause']
    resp = json_data['responsible']
    lastwords = json_data['last_words']
    img = json_data['img']
    death = '⠀\n' + name + '\nCause of death — ' + cause + '\nKilled by — ' + resp + '\nLast words — ' + lastwords + '\n⠀' + '\n' + img
    print(death)
    return (death)


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('-h'):
            await message.channel.send('> commands are: ' + '\n-q > quote\n-d > death info')

        if message.content.startswith('-q'):
            quote = get_quote()
            await message.channel.send(quote)

        if message.content.startswith('-d'):
            death = get_death()
            await message.channel.send(death)

keep_alive()

client.run(os.getenv('SECRET'))
