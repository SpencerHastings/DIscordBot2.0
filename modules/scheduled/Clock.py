from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext import commands
from datetime import datetime

CLOCK_ID = "clock_task"


class Clock(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.channelID = 0
        self.scheduler = AsyncIOScheduler()
        self.scheduler.start()
        self.started = False

    async def clock(self):
        await self.bot.wait_until_ready()
        c = self.bot.get_channel(self.channelID)
        time = datetime.now().strftime("%I:%M %p")
        await c.send("It is currently " + time + ".")

    @commands.command()
    async def startClock(self, ctx: commands.Context):
        if not self.started:
            self.channelID = ctx.channel.id
            self.scheduler.add_job(self.clock, CronTrigger(second="0"), id=CLOCK_ID)
            self.started = True
            await ctx.send("Clock Started")
        else:
            await ctx.send("Clock Already Started")

    @commands.command()
    async def stopClock(self, ctx: commands.Context):
        if self.started:
            self.scheduler.remove_job(CLOCK_ID)
            self.started = False
            await ctx.send("Clock Stopped")
        else:
            await ctx.send("Clock Already Stopped")
