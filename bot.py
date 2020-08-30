import discord
import random
from discord.ext import commands

#prefix to invoke bot is franz
client = commands.Bot(
    command_prefix = 'franz '
)

#when the bot is ready
@client.event
async def on_ready():
    print('Bot is ready.')

#member joins the server
@client.event
async def on_member_join(member):
    print(f'(member) has joined the server.')

#member leaves or somehow else exits server
@client.event
async def on_member_remove(member):
    print(f'(member) has removed the server.')

#ping command responds with latency of Bot
@client.command()
async def ping(ctx):
    await ctx.send(f'Franz\'s latency: {round(client.latency * 1000)}ms')

#8ball game to ask a question and get a random response
@client.command(aliases=['8ball', 'eightball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes – definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don\'t count on it.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.',
                 'Probably not',
                 'For sure',
                 'Sorry, but no',
                 'Never',
                 'How am I supposed to know? I\'m just a robot.',
                 'Clearly not',
                 'I\'m not sure',
                 'Why are you asking me such things?']


    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
client.run()
