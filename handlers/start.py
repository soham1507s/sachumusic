from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CRVA9-gABByMRYIZjxocQxAh3Z5UrUPwuLKCfIDMAAqgCAAI3yjBU3MpuQNTjE3oeBA")
    await message.reply_text(
                f""" <b>Hey {message.from_user.first_name}!  I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\n🔴 Do you want me to play music in your Telegram groups'voice chats? Please click the \'📜 User Manual 📜\' button below to know how you can use me.\n\n🔴 The [Assistant](https://t.me/Chatuniversemusic1) must be in your group to play music in the voice chat of your group.\n\n🔴 More info & commands mentioned in the [User Manual](https://telegra.ph/Chatuniversemusic1bot-04-14)\n\nA project by @UNIQUEGURI 🇮🇳\n\n✅ Join our bots channel and group\n🔰@Hindi_chattinggg_IND 
 </b>""",
      
       reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 User Manual 📜", url="https://telegra.ph/Chatuniversemusic1bot-04-14")
                  ],[
                    InlineKeyboardButton(
                        "👨‍💻 Owner 👨‍💻", url="https://t.me/UNIQUEGURI"
                    )
                   ],[
                    InlineKeyboardButton(
                        "Support channel🎙️" , url="https://t.me/cuXmusic"
                  )
                ],[ 
                    InlineKeyboardButton(
                        "Support Chat 🎙️", url="https://t.me/Hindi_chattinggg_IND"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )
        

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "🔴cuXmusic player is online ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Support Channel", url="https://t.me/cuXmusic"
                    )
                ],[
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
