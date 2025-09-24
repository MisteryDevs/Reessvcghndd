from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from nexichat import nexichat

SUPPORT_CHANNEL = "Ur_Rishu_143"  # Updates/Support channel (constant)

@Client.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    bot = await client.get_me()

    text = f"""**❖ нᴇʏ  {message.from_user.first_name} !, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !
━━━━━━━━━━━━━━━━━━━━━━━━━━━

● ɪ ᴀᴍ  {bot.mention} !

⦿━━━━━━━━━━━━━━━━━━━━━⦿
❍ •  ɪ'ʟʟ ʀᴇᴀᴄᴛ ᴛᴏ ᴇᴠᴇʀʏ ᴍᴇssᴀɢᴇ  •
│❍ • ʙᴇsᴛ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇ •
│❍ • ɴᴏ ʟᴀɢs + ɴᴏ ᴀᴅs •
│❍ • 24x7 ᴏɴʟɪɴᴇ sᴜᴘᴘᴏʀᴛ •
│❍ • ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ •
❍ • ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs •
⦿━━━━━━━━━━━━━━━━━━━━━⦿

❖ ᴛʜɪs ɪs ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ, ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ •\n\n❍ • ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ʙᴏᴛ ʙʏ @ReactionByBot  •\n\n❍ • ᴜᴘᴅᴀᴛᴇ - @Ur_rishu_143**"""

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙", url=f"https://t.me/{bot.username}?startgroup=true")
            ],
            [
                InlineKeyboardButton("⌯  sᴜᴘᴘᴏʀᴛ ⌯", url=f"https://t.me/{SUPPORT_CHANNEL}"),
                InlineKeyboardButton("⌯  ᴏᴡɴᴇʀ ⌯", url=f"https://t.me/{message.from_user.username}" if message.from_user.username else f"tg://user?id={message.from_user.id}")
            ]
        ]
    )

    await message.reply_text(text, reply_markup=buttons)
