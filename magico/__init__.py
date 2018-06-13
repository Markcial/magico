# -*- coding: utf-8 -*-
import os
from slackclient import SlackClient


__VERSION__ = '0.0.1'

AVATAR = 'https://www.bandadicefali.it/wp-content/uploads/2016/09/Magico-Gonzalez-figurina-Cadiz.png'
# instantiate Slack client
SLACK_CLIENT = None


def get_client():
    if SLACK_CLIENT is None:
        if 'SLACK_BOT_TOKEN' not in os.environ:
            raise ValueError("Missing required 'SLACK_BOT_TOKEN'!")
        SLACK_CLIENT = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
    return SLACK_CLIENT


def say(channel, message):
    # Sends the response back to the channel
    get_client().api_call(
        "chat.postMessage",
        channel=channel,
        icon_url=AVATAR,
        username="Mágico González",
        text=message
    )


def react(channel, emoji, ts=None):
  get_client().api_call(
      'reactions.add',
      channel=channel,
      name=emoji,
      timestamp=ts
  )
