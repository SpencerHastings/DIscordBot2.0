from datetime import datetime
import logging
import random
import asyncio
from discord.ext import commands
from config.token import botToken
from config.settings import prefix

TOKEN = botToken

FIRST_START = True

bot = commands.Bot(command_prefix=prefix)

pingList = [
    "I'm sorry, Dave. I'm afraid I can't do that."
    , "Affirmative, Dave. I read you."
    , "I know I've made some very poor decisions recently, but I can give you my complete assurance that my work will "
      "be back to normal. "
    , "[clears throat]"
    , "pong."
    , "Hello there"
    , "Man is free at the instant he wants to be."
    , "PONG"
    , "ping"
    , "IP Trace Completed"]


@bot.command()
async def ping(ctx):
    await ctx.send(random.choice(pingList))


@bot.command()
async def stop(ctx):
    await ctx.send('Stopping')
    print('Stopping')
    await bot.logout()


@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    await bot.invoke(ctx)


# @bot.event
# async def on_member_join(member):
#     role = discord.utils.get(member.guild.roles, name=DEFAULT)
#     await bot.add_roles(member, role)

def get_time():
    now = datetime.now()
    currentTime = now.strftime("%m/%d/%Y-%H:%M:%S")
    return currentTime


@bot.event
async def on_ready():
    global FIRST_START
    if FIRST_START:
        FIRST_START = False
        logging.basicConfig(filename='./logs/bot' + get_time() + '.log',
                            filemode='a',
                            format='%(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        logging.info('------------------------------------------------')
        logging.info('Bot started at ' + get_time())
        logging.info('------------------------------------------------')
        print("Bot Ready")


@bot.event
async def on_disconnect():
    logging.info('Bot disconnected at ' + get_time())


async def background_task():
    await bot.wait_until_ready()
    await asyncio.sleep(5)
    while not bot.is_closed():
        try:
            logging.info("Background Task")
            await asyncio.sleep(5)
        except Exception as e:
            logging.error("Background Task" + str(e))
            print(str(e))
            await asyncio.sleep(5)


bot.loop.create_task(background_task())
bot.run(TOKEN)
