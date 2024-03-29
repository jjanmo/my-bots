import os
from slack_sdk.rtm_v2 import RTMClient
from dotenv import load_dotenv
from time import sleep

load_dotenv()

rtm = RTMClient(token=os.getenv("SLACK_BOT_TOKEN"))


@rtm.on("message")
def handle(client: RTMClient, event: dict):
    if "안녕" in event["text"]:
        channel_id = event["channel"]
        thread_ts = event["ts"]
        user = event[
            "user"
        ]  # This is not username but user ID (the format is either U*** or W***)

        client.web_client.chat_postMessage(
            channel=channel_id, text=f"반가워 <@{user}>!", thread_ts=thread_ts
        )


if __name__ == "__main__":
    rtm.connect()
    while True:  # @rtm.on 상태를 유지
        sleep(1)
