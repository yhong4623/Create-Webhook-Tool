import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.webhooks = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'已登入為 {bot.user.name}')
    try:
        await bot.load_extension('cogs.channel_commands')
        await bot.tree.sync()
        print("斜線指令已同步")
    except Exception as e:
        print(f'啟動時出錯：{e}')

bot.run('YOUR_BOT_TOKEN')