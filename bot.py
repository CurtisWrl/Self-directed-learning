import discord
import datetime
import json
from discord import option
bot = discord.Bot(intents=discord.Intents.all())

#When bot is online, report it in the terminal
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_message(msg):
    pass

#Week 1: say command
@bot.slash_command(name="say", description="Echoes back your message.")
@option(
    "message",
    str,  
    description="The message to echo back",
    required=True
)
async def say(ctx, message: str):
    await ctx.send(message)

#Week 4: timeout command
@bot.slash_command(name="timeout", description="Timeout a user.")
@option(
    "member",
    discord.Member,
    description="The user to timeout",
    required= False
)

@option(
    "minutes",
    int,
    description="The amount of time to timeout the user for",
    required= False
    )

@option(
    "hours",
    int,
    description="The amount of time to timeout the user for",
    required= False
)

@option(
    "reason",
    str,
    description="The reason for the timeout",
    required= False
)
async def timeout(ctx:discord.ApplicationContext, member: discord.Member, minutes: int, hours: int, reason: str = None):
    duration = datetime.timedelta(minutes=minutes, hours=hours)
    await member.timeout_for(duration, reason=reason)
    await ctx.respond(f"Successfully timed out {member.mention} for {minutes} because of {reason}")

bot.run("sus")
