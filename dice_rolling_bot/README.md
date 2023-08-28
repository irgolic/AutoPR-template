# Dice Rolling Bot

This is a Discord bot that allows users to roll virtual dice by typing a command, such as "!roll 1d6". The bot supports various dice types (d4, d6, d8, d10, d12, d20) and multiple dice rolls at once.

## Setup Instructions

1. Install the required libraries:

```bash
pip install discord.py
```

2. Create a `.env` file in the `dice_rolling_bot` folder with your Discord bot token:

```
DISCORD_TOKEN=your_bot_token_here
```

3. Run the bot:

```bash
python dice_rolling_bot.py
```

## Usage Guidelines

To use the dice rolling bot, type a command following this format:

```
!roll NdX
```

Where `N` is the number of dice to roll and `X` is the type of dice (e.g., d4, d6, d8, d10, d12, d20).

### Examples

- Roll a single 6-sided dice:

```
!roll 1d6
```

- Roll two 20-sided dice:

```
!roll 2d20
```

- Roll three 10-sided dice:

```
!roll 3d10
```

When the command is entered, the bot will reply with the results of the individual dice rolls and the total sum.