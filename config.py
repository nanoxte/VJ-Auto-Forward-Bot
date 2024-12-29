from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "d538c2e1a687d414f5c3dce7bf4a743c")
      API_ID = int(getenv("API_ID", "23054736"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7214222575:AAHSuRNS05nBKMB2ZSAugp8jFJXxxkA7QCU")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002146782406:-1002252063312").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
