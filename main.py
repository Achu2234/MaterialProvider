# Made with python3
# @Animesh_941
# Copyright permission under GNU License

import os
import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.ERROR
                             
from pyrogram import filters 
from pyrogram.raw.all import layer
from utils import Media
from info import SESSION, API_ID, API_HASH, BOT_TOKEN
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

AnimeshVerma = Client(
    "Material Bot",
    session_name= os.environ["SESSION"],
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
    workers=50,
    plugins={"root": "plugins"},
    sleep_threshold=5,
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

✨ 𝗠𝗮𝗱𝗲 𝘄𝗶𝘁𝗵 ❤️ 𝗕𝘆 [𝗔𝗻𝗶𝗺𝗲𝘀𝗵 𝗩𝗲𝗿𝗺𝗮](https://telegram.me/AniMesH941)
 **――――――――――――――――――――――**
✨ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 [𝗧𝗲𝗮𝗺 𝗟𝗶𝗯𝗿𝗮𝗿𝗶𝗮𝗻™️](https://telegram.me/Team_Librarian)
"""
FILES_TEXT = """
**★ Hello {}, You Can Search Your Desired Materials anytime via Inline Mode.**
**❍ With this mode, You can get your desired Books, Handwritten Notes, Short Notes in PDF Format directly which are available in Team Librarian Database.**
**❍ You Can Also Request Your Book To Be Added In Our Database, Request Your Book via @LibrarianHelpBot.**

**➧ To use this bot, Type Our Bot's Username and Start Searching,**
    **@EntranceMaterialsBot {Your Filename}**

**➧ Check This Demo {Example}:** 
    `@EntranceMaterialsBot Ncert`

**★ You can also use the Buttons Below For Searching Your Files, Click**
**[● Search Here] :** To Search Files in this Chat.
**[● Go Inline] :** To Search Your Files in another Chat.

**★ For Reporting any Issues, Or If you need any help, You can report them at the Support Group @Librarian_Institute**

✨ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 [𝗧𝗲𝗮𝗺 𝗟𝗶𝗯𝗿𝗮𝗿𝗶𝗮𝗻™️](https://telegram.me/Team_Librarian)
"""
                             
ABOUT_TEXT = """
**● Name : Material Provider Bot**
**● Creator : [Animesh](https://telegram.me/AniMesH941)**
**● Language : [Python3](https://python.org)**
**● Server : [Heroku](https://heroku.com)**
**● Source Code : [Click Here](https://t.me/Want_SourceCode)**

**● Powered By : [Team Librarian™️](https://telegram.me/Team_Librarian)**
"""

START_BUTTONS = InlineKeyboardMarkup(
            [
              [
              InlineKeyboardButton('📒 Find Entrance Examination Materials 📝', callback_data='files')
             ],
              [
               InlineKeyboardButton('ℹ️ Help', callback_data='help'),
               InlineKeyboardButton('🤖 About', callback_data='about')
               InlineKeyboardButton('⛔️ Close', callback_data='close')
              ]
        ]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [
          [
           InlineKeyboardButton('🏠 Home', callback_data='home'),
           InlineKeyboardButton('🤖 About', callback_data='about')
          ],
           [
           InlineKeyboardButton('📒 Find Entrance Examination Materials 📝', callback_data='files') 
           ]
        ]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📮 Feedback', url='https://telegram.me/AniMesH941')
        ],[
        InlineKeyboardButton('🏠 Home', callback_data='home'),
        InlineKeyboardButton('⛔️ Close', callback_data='close')
        ]]
    )
CLOSE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⛔️ Close', callback_data='close')
        ]]
    )

@AnimeshVerma.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
    

@AnimeshVerma.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
@AnimeshVerma.on_message(filters.command(["files"]))
async def help(bot, update):
            text=FILES_TEXT.format(update.from_user.mention),
            reply_markup = FILES_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
                             
@AnimeshVerma.on_message(filters.command(["help"]))
async def help(bot, update):
    text = HELP_TEXT.format(update.from_user.mention)
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
            
AnimeshVerma.run()
