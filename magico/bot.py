import re
import time
from magico import get_client, react
from magico.commands import mapping as command_mapping, default as default_command
from slackclient import SlackClient


RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
COMMAND_PATTERN = r"(^M[áa]gico(\sGonz[áa]lez)?,?|M[áa]gico(\sGonz[áa]lez)?$)"


def parse_bot_commands(slack_events):
    """
    Parses a list of events coming from the Slack RTM API to find bot commands.
    If a bot command is found, this function returns a tuple of command and channel.
    If its not found, then this function returns None, None.
    """
    for event in slack_events:
        print(event)
        if event["type"] == "message" and not "subtype" in event:
            if re.search(COMMAND_PATTERN, event["text"], re.I | re.U):
                message = re.sub(COMMAND_PATTERN, '', event["text"], flags=re.I | re.U).strip()
                return message, event
            elif event["user"] == "U321V1TCH":
                react(event['channel'], 'pepe', event['ts'])
    return None, None


def handle_command(command, event):
    """
    Executes bot command if the command is known
    """
    # Finds and executes the given command, filling in response
    for cmd, callback in command_mapping.items():
        if command.lower().startswith(cmd):
            # command cleanup
            command = command.replace(cmd, "").strip()
            if command.endswith("?"):
                command = command.replace("?", "")
            return callback(command, event)

    default_command(command, event)


def listen():
    """
    """
    if get_client().rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        while True:
            command, channel = parse_bot_commands(get_client().rtm_read())
            if command:
                print("Received command: %s" % command)
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")


if __name__ == '__init__':
  listen()
