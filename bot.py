import asyncio
import os

from discord.ext import commands

from cogs import add_cogs
from config.token import botToken
from config.settings import prefix

if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

bot = commands.Bot(command_prefix=prefix)
add_cogs(bot)
bot.run(botToken)

# random stuff below

# async def background_task():
#     await bot.wait_until_ready()
#     await asyncio.sleep(5)
#     while not bot.is_closed():
#         try:
#             logging.info("Background Task")
#             await asyncio.sleep(5)
#         except Exception as e:
#             logging.error("Background Task" + str(e))
#             print(str(e))
#             await asyncio.sleep(5)
#
#
# bot.loop.create_task(background_task())
