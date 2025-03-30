from os import environ

import dotenv
import discord

dotenv.load_dotenv()

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print("Ready!")

@bot.slash_command()
async def hello(ctx):
    await ctx.respond("Hey!")

bot.run(environ["BINGO_TOKEN"])
