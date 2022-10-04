from Music import *
from json import loads

bot = discord.Bot()

with open("config.json", encoding="utf-8") as f:
    config = loads(f.read())


@bot.event
async def on_ready():
    print(bot.user, flush=True)


bot.add_cog(Music(bot, config))
bot.run(config["discord_bot_token"])
