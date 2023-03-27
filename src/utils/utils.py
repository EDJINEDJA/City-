import os
from dataclasses import dataclass

import requests
from dotenv import load_dotenv
from newsapi import NewsApiClient

""" Load env variables """
load_dotenv("./secret/.env")
API_KEY_NEWS = os.getenv("API_KEY_NEWS")


@dataclass
class outputnews:
    Title: str
    Author: str
    Url: str
    Source: str


class utils:
    def __init__(self) -> None:
        pass

    def news(self):

        url = (
            "https://newsapi.org/v2/top-headlines?"
            "country=fr&"
            f"apiKey={API_KEY_NEWS}"
        )
        response = requests.get(url)
        news = response.json()
        articles = []

        for article in news["articles"]:
            articles.append(article)

        articles_tries = sorted(articles, key=lambda k: k["publishedAt"], reverse=True)
        latest_news = articles_tries[0]

        return outputnews(
            Title=latest_news["title"],
            Author=latest_news["author"],
            Url=latest_news["url"],
            Source=latest_news["source"]["name"],
        )
