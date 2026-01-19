import time
import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"


def dict_json(url: str):
    r = requests.get(url)
    return r.json()


def main():
    ids = dict_json(f"{BASE_URL}/topstories.json")

    for story_id in ids[:30]:
        time.sleep(1)

        item = dict_json(f"{BASE_URL}/item/{story_id}.json")

        title = item.get("title")
        link = item.get("url")

        print({"title": title, "link": link})


if __name__ == "__main__":
    main()
