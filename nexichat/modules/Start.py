from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from nexichat import nexichat

@nexichat.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    await message.reply_video(
        video="https://envs.sh/RCD.mp4",
        caption=(
            f"""**❖ нᴇʏ  {message.from_user.first_name} !, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !
━━━━━━━━━━━━━━━━━━━━━━━━━━━

● ɪ ᴀᴍ  {(await client.get_me()).mention} !

⦿━━━━━━━━━━━━━━━━━━━━━⦿
❍ •  ɪ'ʟʟ ʀᴇᴀᴄᴛ ᴛᴏ ᴇᴠᴇʀʏ ᴍᴇssᴀɢᴇ  •
│❍ • ʙᴇsᴛ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇ •
│❍ • ɴᴏ ʟᴀɢs + ɴᴏ ᴀᴅs •
│❍ • 24x7 ᴏɴʟɪɴᴇ sᴜᴘᴘᴏʀᴛ •
│❍ • ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ •
❍ • ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs •
⦿━━━━━━━━━━━━━━━━━━━━━⦿

❖ ᴛʜɪs ɪs ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ, ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ  •\n\n❍ • ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ʙᴏᴛ ʙʏ /clone**"""
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton("❖ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ❖", url="https://t.me/REACTION7_ROBOT?startgroup=true")
                ],
                [  # Second row
                    InlineKeyboardButton("• sᴜᴘᴘᴏꝛᴛ •", url="https://t.me/BOTMINE_SUPPORT"),
                    InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇ •", url="https://t.me/BOTMINE_TECH")
                ]
            ]
        )
    )
