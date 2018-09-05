#!/usr/bin/env python
# encoding: utf-8
#
# Description: Plugin for 'remedar': what kids do repeating
#              with accent what an adult said to mock
# Author: Pablo Iranzo Gomez (Pablo.Iranzo@gmail.com)

import logging

import stampy.stampy
import stampy.plugin.config
from stampy.i18n import _
from stampy.i18n import _L
import re


def init():
    """
    Initializes module
    :return: List of triggers for plugin
    """

    triggers = ["*"]

    return triggers


def cron():
    """
    Function to be executed periodically
    :return:
    """


def run(message):  # do not edit this line
    """
    Executes plugin
    :param message: message to run against
    :return:
    """
    text = stampy.stampy.getmsgdetail(message)["text"]
    if text:
        replacevowels(message)
    return


def help(message):  # do not edit this line
    """
    Returns help for plugin
    :param message: message to process
    :return: help text
    """
    commandtext = ""
    return commandtext


def replacevowels(message):
    """
    Finds vowels in messages and replaces by 'i'
    :param message: message to process
    :return:
    """

    logger = logging.getLogger(__name__)

    msgdetail = stampy.stampy.getmsgdetail(message)

    texto = msgdetail["text"]
    chat_id = msgdetail["chat_id"]
    message_id = msgdetail["message_id"]
    who_id = msgdetail["who_id"]

    remedar = stampy.plugin.config.config(key='remedar', gid=chat_id)

    if texto != '' and remedar and who_id in remedar.split(" "):
        text = re.sub("[aeouAEOUáéóúàèòùäëöü]", "i", texto)
        if texto != text:
            logger.info("Remedar for %s in chat %s" % (who_id, chat_id))
            stampy.stampy.sendmessage(chat_id=chat_id, text=text,
                                      reply_to_message_id=message_id,
                                      disable_web_page_preview=True,
                                      parse_mode="Markdown")

    return
