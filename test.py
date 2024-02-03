import requests, json
import datetime
import tweepy
import os

def get_pushed_files():
    event_path = os.getenv("GITHUB_EVENT_PATH")

    if event_path and os.path.exists(event_path):
        with open(event_path, "r") as file:
            data = file.read()

        # GitHub Actionsのpushイベントから変更されたファイルを取得
        if data:
            changes = (
                eval(data).get("commits")[0].get("added")
                + eval(data).get("commits")[0].get("modified")
                + eval(data).get("commits")[0].get("removed")
            )

            print("Changed files:")
            for file in changes:
                print(file)


if __name__ == "__main__":
    get_pushed_files()
