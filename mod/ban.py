import discord
import os
from discord.ext import commands
import datetime

class ban(commands.Cog):
    def __init__(self, client):
        self.client = client

        @commands.command()
        @commands.has_permissions(ban_members=True)
        @commands.bot_has_permissions(ban_members=True)
        async def ban(self, ctx, member: discord.Member, *, reason: str):
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="Banned", description=f"You have been banned from **{ctx.guild.name} by **{ctx.author}** for reason **{reason}**", colour=ctx.author.colour, timestamp = datetime.datetime.now())
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await member.send(embed=embed)
            await ctx.send(f"Successfully banned {member}!")


        @ban.error 
        async def ban_error(self, ctx, error):
            if isinstance(error, commands.MissingPermissions):
                await ctx.send(f"You need the `ban_members` permissions required to run this command {ctx.author.mention}!")
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Please provide all of the vaild parameters. They are `member` and `reason`")
            if isinstance(error, commands.BotMissingPermissions):
                await ctx.send("I do not have the needed permissions! They are `Ban members`")
            if isinstance(error, commands.MemberNotFound):
                await ctx.send("They're a :ghost: How do I interact with them?")

def setup(bot):
    bot.add_cog(ban(bot))
