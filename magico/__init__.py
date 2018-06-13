import os
from slackclient import SlackClient


AVATAR = 'https://www.bandadicefali.it/wp-content/uploads/2016/09/Magico-Gonzalez-figurina-Cadiz.png'
# instantiate Slack client
SLACK_CLIENT = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def get_client():
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
