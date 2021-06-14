from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CVUFv6wABBQXdYMc3pDJxmweJ_HpT-u8tj-2TQncAAi4CAAIeQzhWEKTMFGmT2u4fBA")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nThis is a VC Music Bot which can play music in your group's Voice Chat.
Powered By @Bakchodi_Squad
\nTo get started simply add me to your group and make me admin with full rights
\nHit /help list of available commands.
<\b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴀssɪsᴛᴀɴᴛ", url="https://t.me/Raksha_op",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url="https://t.me/Bakchodi_Squad"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀᴛᴛɪɴɢ", url="https://t.me/god_of_loll"
                    ),
                    InlineKeyboardButton(
                        "Sᴏᴜʀᴄᴇ", url="https://telegra.ph/file/6d661cc458396796f4692.jpg"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ", url="https://t.me/QueenMusic_Robot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ", url="https://t.me/Lover_xd"
                    ),
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url="https://t.me/Bakchodi_Squad"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Cʜᴀɴɴᴇʟ", url="https://t.me/tc_bots"
                    ),
                    InlineKeyboardButton(
                        "Gʀᴏᴜᴘ", url="https://t.me/tcbotsbugs"
                    )
                ]
            ]
        )
    )    
