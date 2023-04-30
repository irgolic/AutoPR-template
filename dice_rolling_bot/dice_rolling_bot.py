import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.command(name="roll", help="Rolls a die. Format: !roll <num_of_dice>d<sides_of_die>")
async def roll_dice(ctx, dice: str):
    num_of_dice, sides_of_die = map(int, dice.split("d"))
    rolls = [random.randint(1, sides_of_die) for _ in range(num_of_dice)]
    await ctx.send(', '.join(map(str, rolls)))

bot.run("your_bot_token_here")