# Poll and Survey Bot for Discord

This Discord bot allows users to create and participate in polls and surveys with various question types, such as multiple-choice, rating scales, and open-ended questions. The results are collected and displayed in an easy-to-understand format.

## Features

- Create polls and surveys with various question types.
- Participate in polls and surveys by reacting to messages or submitting responses through text.
- View poll and survey results in an organized and easy-to-understand format.
- Customize the appearance of poll and survey messages.

## Setup

1. Clone this repository or download the `poll_and_survey_bot` folder.
2. Install the required packages by running `pip install -r requirements.txt`.
3. Create a new Discord bot and obtain its token. To do this, follow the instructions in the [Discord Developer Portal](https://discord.com/developers/applications).
4. Rename `config_example.json` to `config.json` and insert your bot token and desired prefix.
5. Run the bot by executing `python bot.py`.

## Usage Instructions

- To create a poll, use the command `!poll <title> <option1> <option2> ... <optionN>`. For example, `!poll "Favorite Fruit" Apple Banana Orange`.
- To create a survey, use the command `!survey <title>`. The bot will DM you with instructions on how to add questions and publish the survey.
- To view the results of a poll or survey, use the command `!results <poll/survey ID>`.

For more detailed instructions and additional commands, type `!help` in a channel where the bot is present.