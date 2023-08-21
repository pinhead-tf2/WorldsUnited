import aiosqlite
import discord.ext.commands
from discord import option
from discord.ext import commands
from discord.commands import SlashCommandGroup


class Queue(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    queue = SlashCommandGroup("Queue", "Commands related to the ban queue")


def setup(bot):
    bot.add_cog(Queue(bot))
