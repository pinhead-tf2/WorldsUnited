import aiosqlite
import discord.ext.commands
from discord import option
from discord.ext import commands
from discord.commands import SlashCommandGroup


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ban = SlashCommandGroup("ban", "Commands related to globally banning and unbanning users")

    @ban.command(name="ban",
                 description="Manually register a ban in the database. ")
    @option("reason", description="Reason the user is being banned")
    @option("evidence", description="Optional evidence (as urls please ty im lazy fuck you colon three kiss men)",
            required=False,
            default=None)
    @commands.is_owner()
    async def register(self, ctx,
                       reason: str,
                       evidence: str
                       ):
        return await ctx.respond("honestly, what the fuck is a kilometer", ephemeral=True)

#     its 4am and im going to bed bcx im going crazy
#     you get THIS much
#     crazy
#     i was crazy once
#     they put me in a room
#     a rubber room a rubber room with rats
#     they put me in a rubber room with rubber rats
#     rubber rats
#     i hate rubber rats
#     they make me crazy


def setup(bot):
    bot.add_cog(Ban(bot))
