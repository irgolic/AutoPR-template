import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix="!", intents=intents)

categories = {
    "1": "History",
    "2": "Geography",
    "3": "Science",
    "4": "Entertainment"
}

questions = {}
with open("questions.json", "r") as file:
    questions = json.load(file)

@client.event
async def on_ready():
    print(f"{client.user.name} is now online")

user_scores = {}

@client.command()
async def start(ctx, category: str):
    if category not in categories:
        await ctx.send(f"Invalid category. Please choose from the following categories:\n{', '.join([f'{key}: {categories[key]}' for key in categories])}")
        return

    selected_questions = [question for question in questions if question['category'] == categories[category]]
    await display_leaderboard(ctx)