import json

import requests
from bs4 import BeautifulSoup


def top_songs(date=20150301):
    response = requests.get(
        f"https://www.officialcharts.com/charts/singles-chart/{date}/7501/"
    )
    # with open("test2.html", "w", encoding="utf-8") as file:
    #     file.write(str(response.content))
    soup = BeautifulSoup(
        response.content,
        "html.parser",
    )
    with open("test.html", "w", encoding="utf-8") as file:
        file.write(str(soup))

    songs = soup.find_all("div", "track", limit=10)

    top100 = {
        index
        + 1: {
            item.find("div", "artist")
            .text.strip(): item.find("div", "title")
            .text.strip()
        }
        for index, item in enumerate(songs)
    }

    with open("songs.json", "w") as file:
        json.dump(top100, file)
    return top100
