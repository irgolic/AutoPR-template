import discord
from discord.ext import commands
from poll import Poll
from utils import parse_poll_args

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def create_poll(ctx, *args):
    poll_args = parse_poll_args(args)

    if poll_args is None:
        await ctx.send('Invalid poll arguments. Please use the correct format: `!create_poll "Question" "Option 1" "Option 2" ...`')
        return

    question, options = poll_args
    poll = Poll(question, options)

    embed = discord.Embed(title=question, description='\n'.join([f'{i+1}. {opt}' for i, opt in enumerate(options)]))

    message = await ctx.send(embed=embed)

    for i in range(len(options)):
        await message.add_reaction(str(i + 1) + '\N{COMBINING ENCLOSING KEYCAP}')

    poll.set_message_id(message.id)
    poll.set_author_id(ctx.author.id)

@bot.command()
async def close_poll(ctx, message_id: int):
    # Retrieve the poll associated with the message ID and close it

    try:
        poll = Poll.get_poll_by_message_id(message_id)
    except ValueError:
        await ctx.send('Invalid message ID.')
        return

    if poll is None:
        await ctx.send('No poll found with that message ID.')
        return

    if poll.author_id != ctx.author.id:
        await ctx.send('You do not have permission to close this poll.')
        return

    poll.close()

    embed = discord.Embed(title=poll.question, description='\n'.join([f'{i+1}. {opt}' for i, opt in enumerate(poll.options)]))
    embed.add_field(name='Results', value=poll.get_results())

    await ctx.send(embed=embed)

bot.run('your-bot-token')