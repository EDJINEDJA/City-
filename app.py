import asyncio
import datetime
import os

import discord
from dotenv import load_dotenv

from src.utils.utils import utils

""" Load env variables """
load_dotenv("./secret/.env")
# se connecter au serve
API_KEY = os.getenv("API_KEY")

""" intent for initialize the client """
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

""" For check if the bot is ready """


@client.event
async def on_ready():
    print("ready")


"""On_message"""


@client.event
async def on_message(message):
    # Check if the message is provided by human
    if message.author.bot:
        return
    # Check if the message begin by the prefixe of the prompt /news
    if message.content == "/news":
        parser = utils()
        user = message.author
        # Feedback for the user
        Author = parser.news().Author
        Source = parser.news().Source
        Title = parser.news().Title
        Url = parser.news().Url

        embed = discord.Embed(
            title="News en france",
            description=f"Titre : {Title}\n ",
            color=discord.Color.blue(),
        )
        embed.set_image(
            url="https://play.google.com/store/apps/details?id=com.zumobi.msnbc&hl=fr"
        )
        embed.set_footer(text=f"Source : {Source} \n Author : {Author} \n Url : {Url}")
        await user.send(embed=embed)

        await message.channel.send(embed=embed)
    else:
        await message.channel.send("Please, The prompt is /news")


if __name__ == "__main__":
    client.run(API_KEY)
