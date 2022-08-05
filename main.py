# Standard Imports
import discord

# File Imports
import get_configs as cfg
import user_cmd as user
import admin_cmd as admin
import embeds as embed

# Specefic Imports
from discord.ext import commands, tasks
from discord import Intents
from discord.ui import Button, View, Select
from asyncio import sleep


bot = commands.Bot(
    command_prefix = cfg.prefix,
    help_command = None,
    intents = Intents.all()
)

# Member Count On Channel Name
@tasks.loop(minutes = 30)
async def member_checker():
    guild = bot.get_guild(cfg.guild)
    show_channel = guild.get_channel(cfg.member_count_channel)
    await show_channel.edit(name = f"Members : {guild.member_count}")

@member_checker.before_loop
async def before_looping_occur():
    await bot.wait_until_ready()

member_checker.start()


# Bot Startup
@bot.event
async def on_ready():
    await bot.change_presence(
        status = discord.Status.dnd,
        activity = discord.Game(" Freelancing")
    )
    print(" BOT IS ONLINE ")

# Help Command
@bot.command()
async def help(ctx):
    await user.help_command(ctx)

# Clear Messages In Specefic Channel
@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 1):
    await admin.clear_messages(ctx, amount)

# Kick's A Member
@bot.command()
@commands.has_permissions(administrator = True)
async def kick(ctx, member : discord.Member):
    await admin.kick_member(ctx, member)


# Create Ticket Form
@bot.command()
@commands.has_permissions(manage_channels = True)
async def tick(ctx, id : int):

    channel = bot.get_channel(id)
    guild = ctx.guild

    async def create_button_callback(interaction):

        category = discord.utils.get(guild.categories, name = cfg.ticket_category)
        channel = await guild.create_text_channel(f'{interaction.user.name}', category = category)

        await channel.set_permissions(guild.default_role, view_channel = False)
        await channel.set_permissions(interaction.user, view_channel = True)

        await channel.send(interaction.user.mention)
        await channel.send(embed = embed.ticket_welcome_embed)

    create_ticket_button = Button(
        label = "Create Ticket",
        style = discord.ButtonStyle.green,
        emoji = "✍️"
    )
    visit_site_button = Button(
        label = "Go To The Site",
        url = "https://yarbo.ir/team/eskandari/",
        emoji = "🌎"
    )

    create_ticket_button.callback = create_button_callback

    view = View()
    view.add_item(create_ticket_button)
    view.add_item(visit_site_button)

    await channel.send(embed = embed.ticket_main_embed, view = view)

# Close Ticket
@bot.command()
@commands.has_permissions(administrator = True)
async def close(ctx):

    await ctx.message.delete()

    if ctx.channel.category.name == cfg.ticket_category:
        msg = await ctx.channel.send("Ticket Closing In 5 Sec")
        await sleep(1)
        await msg.edit("Ticket Closing In 4 Sec")
        await sleep(1)
        await msg.edit("Ticket Closing In 3 Sec")
        await sleep(1)
        await msg.edit("Ticket Closing In 2 Sec")
        await sleep(1)
        await msg.edit("Ticket Closing In 1 Sec")
        await sleep(1)
        await msg.edit("Ticket Closing In 0 Sec")
        await ctx.channel.delete()
    else:
        await ctx.send("This Works Only For Ticket Channels")

# Select Roles
@bot.command()
@commands.has_permissions(administrator = True)
async def rolem(ctx):
    await admin.role_menu(ctx)


# Unknown Command
@bot.event
async def on_command_error(ctx, err):
    if isinstance(err, commands.CommandNotFound):
        wrong_cmd_embed = discord.Embed(
            title = "ᴍᴀᴅᴇ ʙʏ ᴀʀᴅᴀᴠᴀɴ",
            url = "https://github.com/ardavan8102",
            description = f"**{ctx.message.content}** 𝗜𝘀 𝗡𝗼𝘁 𝗩𝗮𝗹𝗶𝗱 𝗖𝗼𝗺𝗺𝗮𝗻𝗱 !\n𝗨𝘀𝗲 => (!𝗵𝗲𝗹𝗽)",
            colour = 0xFF0000
        )

        await ctx.message.delete()
        await ctx.send(ctx.author.mention)
        await ctx.send(embed = wrong_cmd_embed)

bot.run(cfg.token)