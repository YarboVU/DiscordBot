import discord
from asyncio import sleep
import datetime
import embeds as embed
from discord.ui import Button, View, Select


async def clear_messages(ctx, amount):

    await ctx.message.delete()

    count = amount

    clear_embed = discord.Embed(
        title = "ᴍᴀᴅᴇ ʙʏ ᴀʀᴅᴀᴠᴀɴ",
        url = "https://github.com/ardavan8102",
        description = f"𝗗𝗲𝗹𝗲𝘁𝗶𝗻𝗴 **({count})** 𝗠𝗲𝘀𝘀𝗮𝗴𝗲𝘀\n𝗖𝗼𝗻𝘁𝗶𝗻𝘂𝗲?",
        colour = 0x663399
    )
    clear_embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/657987829921611855/1005006606678888488/check.png")
    clear_embed.timestamp = datetime.datetime.utcnow()

    # Callbacks
    # If "Continue" Button Pressed :
    async def continue_button_callback(interaction):
        await ctx.channel.purge(limit = count + 1)
        msg = await ctx.send(embed = embed.cleared_embed)
        await sleep(5)
        await msg.delete()

    # If "Cancel" Button Pressed :
    async def cancel_button_callback(interaction):
        await ctx.channel.purge(limit = 1)
        msg = await ctx.send(embed = embed.cancel_clear_embed)
        await sleep(5)
        await msg.delete()
        

    continue_button = Button(
        label = "Continue",
        style = discord.ButtonStyle.green,
        emoji = "✔️"
    )
    cancel_button = Button(
        label = "Cancel",
        style = discord.ButtonStyle.blurple,
        emoji = "❌"
    )

    # Assign Callbacks
    continue_button.callback = continue_button_callback
    cancel_button.callback = cancel_button_callback

    # View
    view = View()
    view.add_item(cancel_button)
    view.add_item(continue_button)

    await ctx.send(embed = clear_embed, view = view)

async def kick_member(ctx, member):

    await ctx.message.delete()

    kick_embed = discord.Embed(
        title = "ᴍᴀᴅᴇ ʙʏ ᴀʀᴅᴀᴠᴀɴ",
        url = "https://github.com/ardavan8102",
        description = f"𝗞𝗶𝗰𝗸 {member.mention} 𝗙𝗿𝗼𝗺 𝗦𝗲𝗿𝘃𝗲𝗿 ?",
        colour = 0x32CD32
    )
    kick_embed.timestamp = datetime.datetime.utcnow()

    # Callbacks
    # If "Yes" Button Pressed :
    async def yes_button_callback(interaction):

        await ctx.channel.purge(limit = 1) # Delete 'kick_embed' Message
        await member.kick()
        msg = await ctx.send(embed = embed.kicked_embed)
        await sleep(6)
        await msg.delete()

    # If "Cancel" Button Pressed :
    async def no_button_callback(interaction):

        await ctx.channel.purge(limit = 1) # Delete 'kick_embed' Message
        msg = await ctx.send(embed = embed.kick_cancel_embed)
        await sleep(5)
        await msg.delete()
        

    yes_button = Button(
        label = "Yes, Do it",
        style = discord.ButtonStyle.green,
        emoji = "✔️"
    )
    no_button = Button(
        label = "No, Cancel it",
        style = discord.ButtonStyle.blurple,
        emoji = "❌"
    )

    # Assign Callbacks
    yes_button.callback = yes_button_callback
    no_button.callback = no_button_callback

    view = View()
    view.add_item(yes_button)
    view.add_item(no_button)

    await ctx.send(embed = kick_embed, view = view)

async def role_menu(ctx):
    
    await ctx.message.delete()

    menu = Select(
        min_values = 0,
        max_values = 1,
        placeholder = "Select From Here . . .",
        options = [
            discord.SelectOption(
                label = "Gamer", 
                emoji = "🎮", 
                description = "Get A Gamer Role"
            ),

            discord.SelectOption(
                label = "Manager", 
                emoji = "📋", 
                description = "Get A Manager Role"
            )
        ]
    )

    async def menu_callback(interaction):
        role = discord.utils.get(ctx.guild.roles, name = f"{menu.values[0]}")
        user = interaction.user

        if role in interaction.user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message("Role Removed !", ephemeral = True)
        else:
            await user.add_roles(role)
            await interaction.response.send_message("Role Added !", ephemeral = True)
            

    menu.callback = menu_callback

    view = View()
    view.add_item(menu)

    await ctx.send("Choose A Role :", view = view)
