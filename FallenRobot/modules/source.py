from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from FallenRobot import OWNER_USERNAME, dispatcher
from FallenRobot import pbot as client

ANON = "https://telegra.ph/file/b2b4fee33e6c7d2a5651a.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [𝐕𝐈𝐏 𝐁𝐎𝐘](tg://user?id=1808943146)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ꜰᴀʟʟᴇɴ ✘ ʀᴏʙᴏᴛ sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
⏤͟͟͞͞•𓊈𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 ≛⃝🕊[@THE_VIP_BOY](https://t.me/the_vip_boy)⛦⃕͜🇮🇳𓊉
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴏᴡɴᴇʀ •", url=f"https://t.me/{OWNER_USERNAME}"
                    ),
                    InlineKeyboardButton(
                        "• sᴏᴜʀᴄᴇ •",
                        url="https://wa.me/+13212756881",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "🌱𝐑𝐄𝐏𝐎🌿"
