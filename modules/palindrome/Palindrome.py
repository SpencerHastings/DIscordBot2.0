from discord.ext import commands


def check_palindrome(msg: str):
    msg1: str = ''.join(e for e in msg if e.isalnum())
    msg2: str = msg1.lower()
    return msg2 == msg2[::-1]


class Palindrome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.name == "palindromes":
            if not check_palindrome(message.content):
                await message.delete()
