from Music import *

bot = discord.Bot()

with open("config.json") as f:
    config = json.load(f)


@bot.event
async def on_ready():
    print(bot.user, flush=True)


bot.add_cog(Music(bot, config))
bot.run(config["discord_bot_token"])
