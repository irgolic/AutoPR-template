# 🤖👨‍💻 AutoPR Github Action Template

<div align="center">

[![Discord](https://badgen.net/badge/icon/discord?icon=discord&label&color=purple)](https://discord.gg/ykk7Znt3K6)

[AutoPR](https://github.com/irgolic/AutoPR) automatically writes pull requests in response to issues using GPT-4.   
Check the issues and pull requests in this repository for examples of what AutoPR can do.

</div>

# 🛠 Usage

Warning: This Github Action is currently **in development**, and in **alpha release**.
If you're interested in using this action, please reach out on [Discord](https://discord.gg/vz7p9TfHsh).

## If you don't yet have access to GPT-4

If you've got a cool idea you'd like to try out AutoPR with, feel free to make an issue in this repository, and I'll run it manually.

## Using your own token

You may press "Use this template" to create a new repository with the AutoPR workflow file, or copy it to your own repository manually.

You will also need to perform the following steps:
- In `Settings -> Secrets and variables -> Actions`, enter your Open AI API key as `OPENAI_API_KEY`
- In `Settings -> Actions -> General`, scroll down to `Workflow permissions` and enable `Allow Github Actions to create and approve pull requests`

Whenever a new issue is opened or edited, the action will push a branch named `autopr/issue-#` and open a pull request to the base branch.
Please note that if the branch already exists (on issue edit), it will be overwritten.
