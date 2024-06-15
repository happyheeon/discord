import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.tree.sync()

@bot.tree.command(name="공지")
async def notification(interaction: discord.Interaction, content: str):
    channel = interaction.guild.get_channel(int(1250388932689002538))
    if channel is None:
        await interaction.response.send_message("채널을 찾을 수 없습니다. 채널 ID를 확인하세요.")
        return
    await channel.send(f"@everyone\n```{content}```")
    await interaction.response.send_message("공지가 전송되었습니다.")

bot.run('os.environ['token']')
