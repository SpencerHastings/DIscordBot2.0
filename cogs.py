from modules.essential.Core import Core
from modules.palindrome.Palindrome import Palindrome
from modules.ping.Ping import Ping
from modules.roles.DefaultRole import DefaultRole


def add_cogs(bot):
    bot.add_cog(Core(bot))
    bot.add_cog(Ping(bot))
    bot.add_cog(DefaultRole(bot))
    bot.add_cog(Palindrome(bot))
