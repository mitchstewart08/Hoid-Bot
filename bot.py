import discord
import os
import aiohttp
import asyncio
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client()


@client.event
async def on_ready():

    print(
        f'{client.user} is connected to the following guild:\n'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!covid"):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://jsonplaceholder.typicode.com/posts') as r:
                if r.status == 200:
                    js = await r.json()
                    print(f'{js}')
                else:
                    await message.channel.send("Error")

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)
