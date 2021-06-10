# Made with python3
# @Animesh_941
# Copyright permission under GNU License

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AnimeshVerma = Client(
    "Material Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """
**Hello {}, I am a Simple Material Provider Bot.**
**I Can Provide You all Materials Related to Entrance Examinations**

**Check Below Buttons To know more:**
**Developed By [𝗔𝗡𝗜𝗠𝗘𝗦𝗛](https://t.me/AniMesH941)**
"""

HELP_TEXT = """
**☛ Hii {}, I Can Provide You Any Book In PDF Format**
**Although I'm The First Bot On Whole Telegram, Developed Using python**

**🤖 Features of this Bot-
 ┣ Get Books on Demand
 ┣ All variety of books 
 ┣ All competitive exams books
 ┣ All novels/ magazines/ newspaper.
 ┣ Contact admin feature
 ┗ Paid promotion available.**

**✨ 𝗦𝗵𝗮𝗿𝗲 𝗠𝗲, 𝗠𝗮𝗱𝗲 𝘄𝗶𝘁𝗵 ❤️ 𝗕𝘆 [𝗔𝗻𝗶𝗺𝗲𝘀𝗵 𝗩𝗲𝗿𝗺𝗮](https://telegram.me/AniMesH941)**
  **―――――――――――――――――――――――――――――**
**✨ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 [𝗧𝗲𝗮𝗺 𝗟𝗶𝗯𝗿𝗮𝗿𝗶𝗮𝗻™️](https://telegram.me/Team_Librarian)**
"""

ABOUT_TEXT = """
**● Name : Material Provider Bot**
**● Creator : [Animesh](https://telegram.me/AniMesH941)**
**● Language : [Python3](https://python.org)**
**● Server : [Heroku](https://heroku.com)**

**● Powered By : [Team Librarian™️](https://telegram.me/Team_Librarian)**
"""

DISCLAIMER_TEXT = """
 **• We are strictly against piracy.**
 **• You will be sent your desired books via bot within 6 hours to 6 days.**
 **• You can join our daily E-Newspaper service by contacting admin. All English, Hindi, Marathi & Other Regional News Updates For Examinations available.**
 **• Spamming inside the bot may lead you ban forever.**
 **• We may promote some Ads here to overcome server and maintainence expenses. Contact Admin for more info.**
 
**‼️ Check This Telegraph Link Before You Ask For Any Book - [Click Here ⚠️](https://telegra.ph/DISCLAIMER-04-28-5)**
"""

START_BUTTONS = InlineKeyboardMarkup(
        [
            [
             InlineKeyboardButton('⚠️ Disclaimer', callback_data='terms'),
             InlineKeyboardButton('🤖 About', callback_data='about')
            ],
             [
              InlineKeyboardButton('ℹ️ Help', callback_data='help'),
              InlineKeyboardButton('⛔️ Close', callback_data='close')
             ]
        ]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠 Home', callback_data='home'),
        InlineKeyboardButton('🤖 About', callback_data='about'),
        InlineKeyboardButton('⛔️ Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠 Home', callback_data='home'),
        InlineKeyboardButton('ℹ️ Help', callback_data='help'),
        InlineKeyboardButton('⛔️ Close', callback_data='close')
        ]]
    )
DISCLAIMER_BUTTONS = InlineKeyboardMarkup(
        [
          [
        InlineKeyboardButton('⚜️ Share Our Bot With Your Friends 🤖', url="""https://t.me/share/text?text=**Hey, Check What I Found... The Best Telegram Bot To Provide You Study Materials, Developed In Pyrogram & Python 3. Check Now @EntranceMaterialsBot Don't Miss It 👋🏻"""),
          ],
           [
            InlineKeyboardButton('ℹ️ Help', callback_data='help'),
            InlineKeyboardButton('🏠 Home', callback_data='home')
           ]
        ]
     ) 
CLOSE_BUTTONS = InlineKeyboardMarkup(
        [
            [
        InlineKeyboardButton('⛔️ Close', callback_data='close')
            ]
         ]
     )

@AnimeshVerma.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=HELP_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    elif update.data == "terms":
        await update.message.edit_text(
            text=DISCLAIMER_TEXT,
            disable_web_page_preview=True,
            reply_markup=DISCLAIMER_BUTTONS
    else:
        await update.message.delete()
    

@AnimeshVerma.on_message(filters.command(["start"]))
async def help(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@AnimeshVerma.on_message(filters.command(["help"]))
async def start(bot, update):
    text = HELP_TEXT.format(update.from_user.mention)
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
          
AnimeshVerma.run()
