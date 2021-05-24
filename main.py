import os
from slack_bolt import App

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.command("/hi")
def repeat_text(ack, say, command):
    ack()
    say(f"Hey!")


@app.message("Hello")
def say_hello(message, say):
    user = message['user']
    say(f"Hi there, <@{user}>")


if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
