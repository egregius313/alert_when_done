#!/usr/bin/env python3
"""
alert_when_done

Usage:
    awd-server [OPTIONS] -- <cmd>...

Options:
    --config <cfg>  configuration file
    -p <pid>        watch pid
"""
import json
import os
import subprocess
import sys

import docopt
from telegram.ext import CommandHandler, Updater


try:
    with open('config.json', 'r') as f:
        config = json.load(f)

    token = config['token']
    updater = Updater(token=token)
except FileNotFoundError:
    print(
        'Could not find configuration file config.json',
        file=sys.stderr
    )
    exit(1)
except json.JSONDecodeError:
    print(
        'Could not parse config.json',
        file=sys.stderr
    )
    exit(1)
except KeyError:
    print(
        'config.json requires "token" and "receiver" fields',
        file=sys.stderr
    )
    exit(1)


def start(bot, update):
    """
    Begin first connection with the server.
    """
    bot.send_message(chat_id=update.message.chat_id,
                     text="im_too_lazy_to_generate_oauth_tokens")


start_handler = CommandHandler('start', start)


def progress(bot, update):
    """
    Show the progress 
    """


if __name__ == '__main__ ':
    docopt.docopt(__doc__)
