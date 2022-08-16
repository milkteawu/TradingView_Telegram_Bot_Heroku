# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : fabston                 #
# File Name             : handler.py              #
# ----------------------------------------------- #

# TradingView Example Alert Message:
# {
# "key":"9T2q394M92", "telegram":"-1001298977502", "discord":"789842349670960670/BFeBBrCt-w2Z9RJ2wlH6TWUjM5bJuC29aJaJ5OQv9sE6zCKY_AlOxxFwRURkgEl852s3", "msg":"Long #{{ticker}} at `{{close}}`"
# }

from telegram import Bot
import os
from datetime import datetime, timezone, timedelta, strptime

def get_timestamp():
    # timestamp = time.strftime("%Y-%m-%d %X")
    tz = timezone(timedelta(hours=+8))
    timestamp = strptime(datetime.now(tz), "%Y-%m-%dT%H:%M:%S")
    return timestamp

def send_alert(data):
    msg = data["msg"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    if os.environ.get("send_telegram_alerts"):
        tg_bot = Bot(token=os.environ.get("tg_token"))
        try:
            tg_bot.sendMessage(
                data["telegram"],
                msg,
                get_timestamp(),
                parse_mode="MARKDOWN",
            )
        except KeyError:
            tg_bot.sendMessage(
                os.environ.get("channel"),
                msg,
                get_timestamp(),
                parse_mode="MARKDOWN",
            )
        except Exception as e:
            print("[X] Telegram Error:\n>", e)