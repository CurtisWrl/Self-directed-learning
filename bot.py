#week 1: create a bot
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

#Week 2: say command
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
    required= True
)

@option(
    "minutes",
    int,
    description="The amount of time to timeout the user for",
    required= True
    )

@option(
    "hours",
    int,
    description="The amount of time to timeout the user for",
    required= True
)

@option(
    "reason",
    str,
    description="The reason for the timeout",
    required= True
)
async def timeout(ctx:discord.ApplicationContext, member: discord.Member, minutes: int, hours: int, reason: str):
    duration = datetime.timedelta(minutes=minutes, hours=hours)
    await member.timeout_for(duration, reason=reason)
    await ctx.respond(f"Successfully timed out {member.mention} because of {reason}")
#ban
@bot.slash_command(name='ban', description='Ban a user')
@option(
    'member',
    discord.Member,
    description='The user to ban',
    required=True
)
@option(
    'reason',
    str,
    description='The reason for the ban',
    required=True
)
async def ban(ctx: discord.ApplicationContext, member: discord.Member, reason: str):
    await member.ban(reason=reason)
    await ctx.respond(f"Successfully banned {member.mention} for {reason}")
#Week 5 kick command
@bot.slash_command(name='kick', description='Kick a user')
@option(
    'member',
    discord.Member,
    description='The user to kick',
    required=True
)
@option(
    'reason',
    str,
    description='The reason for the kick',
    required=True
)
async def kick(ctx: discord.ApplicationContext, member: discord.Member, reason: str):
    await member.kick(reason=reason)
    await ctx.respond(f"Successfully kicked {member.mention} for {reason}")

#Giving a role
@bot.slash_command(name='give_role', description='Give a role to a user')
@option(
    'member',
    discord.Member,
    description='The user to give the role to',
    required=True
)
@option(
    'role',
    discord.Role,
    description='The role to give to the user',
    required=True
)
async def role(ctx: discord.ApplicationContext, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.respond(f"Successfully given {role.mention} to {member.mention}")

#Get a user's display avatar
@bot.slash_command(name='avatar', description='Get a user\'s display avatar')
@option(
    'member',
    discord.Member,
    description='The user to get the avatar of',
    required=True
)
async def avatar(ctx: discord.ApplicationContext, member: discord.Member):
    await ctx.respond(member.display_avatar.url)

#help slash command
@bot.slash_command(name='help', description='Get help')
async def help(ctx: discord.ApplicationContext):
    with open('help.json', 'r') as f:
        help_data = json.load(f)
    embed = discord.Embed(title='Help', description='Here are the available commands:', color=0xffca00)
    for command in help_data:
        embed.add_field(name=command, value=help_data[command], inline=False)
    await ctx.respond(embed=embed)
    
bot.run(‘your bot's token')
