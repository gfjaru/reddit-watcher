# reddit-watcher

👀 have an eyes on subreddit, always get latest post.

## Requirements

API Keys of course, get one here -> https://www.reddit.com/prefs/apps
Discord webhook -> https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks

## Installation

(run locally) set environment variable for:

- DISCORD_WEBHOOK_URL
- DISCORD_WEBHOOK_NAME
- DISCORD_WEBHOOK_AVATAR
- REDDIT_CLIENT_ID
- REDDIT_CLIENT_SECRET
- REDDIT_USERNAME
- REDDIT_PASSWORD
- REDDIT_SUBREDDIT

Then install dependencies, just type

```
pip install -r requirements.txt
```

Run the app.


## Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

***idk how to deal with this, run worker manually after deploying, go to heroku app > resource > worker

Watchout for free users, workers never sleep, free user without verified credit card got 400hours per month


---

Originally created for grabbing meme from r/Hololive.
