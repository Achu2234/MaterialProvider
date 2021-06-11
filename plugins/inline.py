import logging
from urllib.parse import quote

from pyrogram import Client, emoji, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultCachedDocument

from utils import get_search_results
from info import CACHE_TIME, SHARE_BUTTON_TEXT, AUTH_USERS, AUTH_CHANNEL

logger = logging.getLogger(__name__)
cache_time = 0 if AUTH_USERS or AUTH_CHANNEL else CACHE_TIME


@AnimeshVerma.on_inline_query(filters.user(AUTH_USERS) if AUTH_USERS else None)
async def answer(bot, query):
    """🤖 Developer Animesh Verma """

    if AUTH_CHANNEL and not await is_subscribed(bot, query):
        await query.answer(results=[],
                           cache_time=0,
                           switch_pm_text="""
                           **😶 You need to subscribe my channel @Librarian_Official, to use me.....!**
                           **ThankYou, Contact [Owner](https://telegram.me/AniMesH941) 🙏🏻**""",
                           switch_pm_parameter="subscribe")
        return

    results = []
    if '|' in query.query:
        string, file_type = query.query.split('|', maxsplit=1)
        string = string.strip()
        file_type = file_type.strip().lower()
    else:
        string = query.query.strip()
        file_type = None

    offset = int(query.offset or 0)
    reply_markup = get_reply_markup(bot.username, query=string)
    files, next_offset = await get_search_results(string,
                                                  file_type=file_type,
                                                  max_results=10,
                                                  offset=offset)

    for file in files:
        results.append(
            InlineQueryResultCachedDocument(
                title=file.file_name,
                file_id=file.file_id,
                caption=file.caption or "",
                description=f'Size: {get_size(file.file_size)}\nType: {file.file_type}',
                reply_markup=reply_markup))

    if results:
        switch_pm_text = f"🔎 Type To Search Your Book"
        if string:
            switch_pm_text += f" for {string}"

        await query.answer(results=results,
                           cache_time=cache_time,
                           switch_pm_text=switch_pm_text,
                           switch_pm_parameter="start",
                           next_offset=str(next_offset))
    else:

        switch_pm_text = f'❌ No Results, Contact Animesh'
        if string:
            switch_pm_text += f' for "{string}"'

        await query.answer(results=[],
                           cache_time=cache_time,
                           switch_pm_text=switch_pm_text,
                           switch_pm_parameter="okay")


def get_reply_markup(username, query):
    FILES_BUTTONS = [
                 [
                  InlineKeyboardButton('● Search Again', switch_inline_query_current_chat=query),
                  InlineKeyboardButton('● Join Channel', url='https://t.me/Librarian_Official'),
                  ],
                   [
                   InlineKeyboardButton('☎️ Contact Owner ', url='https://t.me/AniMesH941'),  
                   ]
              ]
    return InlineKeyboardMarkup(buttons)


def get_size(size):
    """Get size in readable format"""

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])


async def is_subscribed(bot, query):
    try:
        user = await bot.get_chat_member(AUTH_CHANNEL, query.from_user.id)
    except UserNotParticipant:
        pass
    except Exception as e:
        logger.exception(e)
    else:
        if not user.status == 'kicked':
            return True

    return False