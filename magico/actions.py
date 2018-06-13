import os
from slackclient import SlackClient


AVATAR = 'https://www.bandadicefali.it/wp-content/uploads/2016/09/Magico-Gonzalez-figurina-Cadiz.png'


def get_client():
    if get_client.instance is None:
        if 'SLACK_BOT_TOKEN' not in os.environ:
            raise ValueError("Missing required 'SLACK_BOT_TOKEN'!")
        get_client.instance = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
    return get_client.instance
get_client.instance = None


def get_realname(userid):
  result = get_client().api_call(
      "users.info",
      user=userid
  )
  if result['ok']:
      return result['user']['real_name']

  return 'Unknown'


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
