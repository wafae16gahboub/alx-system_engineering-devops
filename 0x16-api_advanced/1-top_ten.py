#!/usr/bin/python3
""" task 1"""
import requests


def top_ten(subreddit):
    base_url = 'https://www.reddit.com'
    headers = {'user-agent': 'fake_user_agent'}

    dict_response = requests.get(
      base_url + "/r/" + subreddit + "/hot.json",
      headers=headers,
      allow_redirects=False).json()

    list_posts = dict_response.get('data', {}).get("children", [])
    if not list_posts:
        print("None")
    for title in list_posts[:10]:
        print(title.get('data').get('title'))
