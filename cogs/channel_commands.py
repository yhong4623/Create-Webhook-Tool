import discord
from discord import app_commands
from discord.ext import commands
from utils.config import get_category_id, set_category_id

class ChannelCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="set_category", description="設置用於創建頻道的類別 ID")
    @app_commands.describe(category_id="目標類別的 ID")
    async def set_category(self, interaction: discord.Interaction, category_id: str):
        """設置全局類別 ID"""
        try:
            category_id = int(category_id)
            category = interaction.guild.get_channel(category_id)

            if category is None or not isinstance(category, discord.CategoryChannel):
                embed = discord.Embed(
                    title="錯誤",
                    description=f"找不到 ID 為 {category_id} 的類別或該 ID 不是類別。",
                    color=discord.Color.red(),
                    timestamp=discord.utils.utcnow()
                )
                embed.set_footer(text=f"由 {interaction.user.name} 觸發")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                return

            set_category_id(category_id)
            embed = discord.Embed(
                title="成功",
                description=f"已設置類別 ID 為 {category_id}。",
                color=discord.Color.green(),
                timestamp=discord.utils.utcnow()
            )
            embed.set_footer(text=f"由 {interaction.user.name} 觸發")
            await interaction.response.send_message(embed=embed, ephemeral=True)

        except ValueError:
            embed = discord.Embed(
                title="錯誤",
                description="請輸入有效的數字 ID。",
                color=discord.Color.red(),
                timestamp=discord.utils.utcnow()
            )
            embed.set_footer(text=f"由 {interaction.user.name} 觸發")
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="create_channel", description="在特定類別中創建一個新的文字頻道和 Webhook")
    @app_commands.describe(channel_name="新頻道的名稱")
    async def create_channel(self, interaction: discord.Interaction, channel_name: str):
        """創建一個新的文字頻道，放在指定類別中，並創建一個 Webhook"""
        category_id = get_category_id()

        if category_id is None:
            embed = discord.Embed(
                title="錯誤",
                description="未設置類別 ID，請先使用 `/set_category` 指令設置類別 ID。",
                color=discord.Color.red(),
                timestamp=discord.utils.utcnow()
            )
            embed.set_footer(text=f"由 {interaction.user.name} 觸發")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        guild = interaction.guild
        category = guild.get_channel(category_id)

        if category is None or not isinstance(category, discord.CategoryChannel):
            embed = discord.Embed(
                title="錯誤",
                description=f"找不到 ID 為 {category_id} 的類別或該 ID 不是類別。",
                color=discord.Color.red(),
                timestamp=discord.utils.utcnow()
            )
            embed.set_footer(text=f"由 {interaction.user.name} 觸發")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        try:
            channel = await guild.create_text_channel(channel_name, category=category)
            webhook = await channel.create_webhook(name="AutoCreatedWebhook")

            embed = discord.Embed(
                title="頻道與 Webhook 創建成功！",
                color=discord.Color.green(),
                timestamp=discord.utils.utcnow()
            )
            embed.add_field(name="新頻道", value=channel.mention, inline=False)
            embed.add_field(name="Webhook URL", value=f"```{webhook.url}```", inline=False)
            embed.set_footer(text=f"由 {interaction.user.name} 創建")
            await interaction.response.send_message(embed=embed, ephemeral=True)

        except discord.Forbidden:
            embed = discord.Embed(
                title="錯誤",
                description="我沒有權限創建頻道或 Webhook。",
                color=discord.Color.red(),
                timestamp=discord.utils.utcnow()
            )
            embed.set_footer(text=f"由 {interaction.user.name} 觸發")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except discord.HTTPException as e:
            embed = discord.Embed(
                title="錯誤",
                description=f"創建失敗：{e}",
                color=discord.Color.red(),
                timestamp=discord.utils.utcnow()
            )
            embed.set_footer(text=f"由 {interaction.user.name} 觸發")
            await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(ChannelCommands(bot))