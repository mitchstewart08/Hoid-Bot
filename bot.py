import discord
from discord.ext import commands
import os
import aiohttp
import asyncio
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def test(ctx, *args):
    print(len(args))


@bot.command()
async def covid(ctx, *args):
    if args:
        async with aiohttp.ClientSession() as session:
            state = args[0]
            async with session.get(f'https://api.covidtracking.com/v1/states/{state}/current.json') as r:
                if r.status == 200:
                    results = await r.json()
                    desc = "**Positive Cases**:" + str(results["positive"]) + '\n' + "**Negative Cases**:" + str(results["negative"]) + '\n' + "**Pending Cases**:" + str(results["pending"]) + '\n\n' + "**Hospitalized Currently Cases**:" + str(
                        results["hospitalizedCurrently"]) + '\n' + "**Hospitalized Cases Cumlative**:" + str(results["hospitalizedCumulative"]) + '\n' + "**ICU Currently **:" + str(results["inIcuCurrently"]) + '\n' + "**ICU Cumulative Total**:" + str(results["inIcuCumulative"]) + '\n'
                    embed = discord.Embed(
                        title=f"Covid stats for {state}" or None, description=desc or None)
                    await ctx.send(embed=embed)
                else:
                    await message.channel.send("Error")
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.covidtracking.com/v1/us/current.json') as r:
                if r.status == 200:
                    results = await r.json()
                    desc = "**Positive Cases**:" + str(results[0]["positive"]) + '\n' + "**Negative Cases**:" + str(results[0]["negative"]) + '\n' + "**Pending Cases**:" + str(results[0]["pending"]) + '\n\n' + "**Hospitalized Currently Cases**:" + str(
                        results[0]["hospitalizedCurrently"]) + '\n' + "**Hospitalized Cases Cumlative**:" + str(results[0]["hospitalizedCumulative"]) + '\n' + "**ICU Currently **:" + str(results[0]["inIcuCurrently"]) + '\n' + "**ICU Cumulative Total**:" + str(results[0]["inIcuCumulative"]) + '\n'
                    embed = discord.Embed(title="Covid stats for America" or None,
                                          description=desc or None)
                    await ctx.send(embed=embed)
                else:
                    await message.channel.send("Error")


@ bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@ bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@ bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@ bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


@ bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))


@ cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

bot.run(TOKEN)
