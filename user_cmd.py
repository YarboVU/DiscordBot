import discord
import datetime
import embeds as embed
from discord.ui import Button, View

class Buttons(Button):
    def __init__(self, label, color, emoji):
        super().__init__(label = label, style = color, emoji = emoji)



async def help_command(ctx):

    guild = ctx.guild

    await ctx.message.delete()

    # Callbacks
    async def mention_callback(interaction):
        await interaction.response.send_message(
            f"Send Request To : {guild.owner.mention}", 
            ephemeral = True
        )

    async def command_list_callback(interaction):
        await interaction.response.send_message(
            embed = embed.command_list_embed,
            ephemeral = True
        )

    # Buttons

    mention_owner_button = Buttons(
        "Contact Owner",
        color = discord.ButtonStyle.green,
        emoji = "📞"
    )

    command_list_button = Buttons(
        "Command List", 
        color = discord.ButtonStyle.blurple, 
        emoji = "📋"
    )

    # Assigning Callbacks
    mention_owner_button.callback = mention_callback
    command_list_button.callback = command_list_callback

    # View
    view = View()
    view.add_item(mention_owner_button)
    view.add_item(command_list_button)

    await ctx.send(embed = embed.help_embed, view = view)
