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

    if ctx.author not in user_scores:
        user_scores[ctx.author] = 0

    selected_questions = [question for question in questions if question['category'] == categories[category]]
    question = random.choice(selected_questions)
    question_text = question["question"]
    options = [f"{index+1}. {option}" for index, option in enumerate(question["options"])]
    await ctx.send(f"{question_text}\nOptions:\n{' '.join(options)}")
    answer = await client.wait_for("message", check=lambda message: message.author == ctx.author, timeout=30)