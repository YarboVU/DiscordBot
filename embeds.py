import discord
import datetime
import get_configs as cfg
from discord.ui import Button, View

command_list_embed = discord.Embed(
    title = "ᴍᴀᴅᴇ ʙʏ ᴀʀᴅᴀᴠᴀɴ",
    url = "https://github.com/ardavan8102",
    description = f"𝗖𝗼𝗺𝗺𝗮𝗻𝗱 𝗟𝗶𝘀𝘁 𝗢𝗳 𝗕𝗼𝘁 **:**\nprefix : {cfg.prefix}",
    colour = 0xFFA500
)
command_list_embed.add_field(
    name = "**⭐ help**",
    value = "Basic Help Command",
    inline = True
)
command_list_embed.add_field(
    name = "**⭐ clear (Admin)**",
    value = "Clear's A Specefic Amount Of Messages",
    inline = True
)
command_list_embed.add_field(
    name = "**⭐ Kick (Admin)**",
    value = "Kick's An User From Server",
    inline = True
)

#########################################################################

help_embed = discord.Embed(
    title = "ᴍᴀᴅᴇ ʙʏ ᴀʀᴅᴀᴠᴀɴ",
    url = "https://github.com/ardavan8102",
    description = "𝗛𝗲𝘆 𝗧𝗵𝗲𝗿𝗲,\n𝗪𝗵𝗮𝘁 𝗖𝗮𝗻 𝗶 𝗗𝗼 𝗙𝗼𝗿 𝗬𝗼𝘂 ?",
    colour = 0x663399
)
help_embed.timestamp = datetime.datetime.utcnow()

#########################################################################

cleared_embed = discord.Embed(
    title = "ᴍᴀᴅᴇ ʙʏ ᴀʀᴅᴀᴠᴀɴ",
    url = "https://github.com/ardavan8102",
    description = "𝗠𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗗𝗲𝗹𝗲𝘁𝗲𝗱 !",
    colour = 0x7CFC00
)
cleared_embed.timestamp = datetime.datetime.utcnow()

cancel_clear_embed = discord.Embed(
    title = "ᴍᴀᴅᴇ ʙʏ ᴀʀᴅᴀᴠᴀɴ",
    url = "https://github.com/ardavan8102",
    description = "𝗢𝗽𝗲𝗿𝗮𝘁𝗶𝗼𝗻 𝗖𝗮𝗻𝗰𝗲𝗹𝗲𝗱 !",
    colour = 0xFF0000
)
cleared_embed.timestamp = datetime.datetime.utcnow()

#########################################################################

kicked_embed = discord.Embed(
    title = "ᴍᴀᴅᴇ ʙʏ ᴀʀᴅᴀᴠᴀɴ",
    url = "https://github.com/ardavan8102",
    description = "𝗞𝗶𝗰𝗸𝗲𝗱 𝗙𝗿𝗼𝗺 𝗦𝗲𝗿𝘃𝗲𝗿 !",
    colour = 0x00FA9A
)
cleared_embed.timestamp = datetime.datetime.utcnow()

kick_cancel_embed = discord.Embed(
    title = "ᴍᴀᴅᴇ ʙʏ ᴀʀᴅᴀᴠᴀɴ",
    url = "https://github.com/ardavan8102",
    description = "𝗢𝗽𝗲𝗿𝗮𝘁𝗶𝗼𝗻 𝗖𝗮𝗻𝗰𝗲𝗹𝗲𝗱 !",
    colour = 0xFF0000
)
cleared_embed.timestamp = datetime.datetime.utcnow()

#########################################################################

ticket_main_embed = discord.Embed(
    title = "ᴍᴀᴅᴇ ʙʏ ᴀʀᴅᴀᴠᴀɴ",
    url = "https://github.com/ardavan8102",
    description = "𝗔𝘀𝗸 𝗬𝗼𝘂𝗿 𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻 𝗢𝗿 𝗙𝗶𝗻𝗱 𝗧𝗵𝗲 𝗔𝗻𝘀𝘄𝗲𝗿 !",
    colour = 0x663399
)
ticket_main_embed.set_image(url = "https://cdn.discordapp.com/attachments/657987829921611855/1005085965645271160/-python.png")
    
ticket_welcome_embed = discord.Embed(
    title = "ᴍᴀᴅᴇ ʙʏ ᴀʀᴅᴀᴠᴀɴ",
    url = "https://github.com/ardavan8102",
    description = "𝗧𝗲𝗹𝗹 𝗨𝘀 𝗬𝗼𝘂𝗿 𝗣𝗿𝗼𝗯𝗹𝗲𝗺 𝗔𝗻𝗱 𝗪𝗲 𝗪𝗶𝗹𝗹 𝗦𝗼𝗹𝘃𝗲 𝗜𝘁 !\n𝗔𝘀𝗸 𝗔𝗱𝗺𝗶𝗻 𝗧𝗼 𝗖𝗹𝗼𝘀𝗲 𝗧𝗶𝗰𝗸𝗲𝘁 !",
    colour = 0xFFFF00
)