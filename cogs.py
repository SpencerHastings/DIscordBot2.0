from modules.essential.Core import Core
from modules.palindrome.Palindrome import Palindrome
from modules.ping.Ping import Ping
from modules.roles.DefaultRole import DefaultRole
from config.settings import features
from modules.scheduled.Clock import Clock


def add_cogs(bot):
    bot.add_cog(Core(bot))
    if features.get('ping'):
        bot.add_cog(Ping(bot))
    if features.get('default_role'):
        bot.add_cog(DefaultRole(bot))
    if features.get('palindrome'):
        bot.add_cog(Palindrome(bot))
    if features.get('clock'):
        bot.add_cog(Clock(bot))
