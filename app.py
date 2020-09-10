import praw, os, requests, json

def discordPush(submission):
    data = {
        "username": os.getenv("DISCORD_WEBHOOK_NAME"), # edit this yourself
        "avatar_url": os.getenv("DISCORD_WEBHOOK_AVATAR"), # edit this yourself
        "content": "",
        "embeds": [
            {
                "author": {
                    "name": str(submission.author),
                    "url": "https://www.reddit.com/u/" + str(submission.author)
                },
                "title": str(submission.title),
                "url": "https://www.reddit.com" + str(submission.permalink),
                "image": {
                    "url": submission.url
                }
            }
        ]
    }

    push = requests.post(url=os.getenv("DISCORD_WEBHOOK_URL"),
                         headers={"Content-Type": "application/json"},
                         data=json.dumps(data))

    return "[" + str(push.status_code) + "] Passing data " + str(submission.permalink) + " to Discord Webhook"

app = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                  client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                  user_agent="ChangeMeClient/0.1 by YourUsername",
                  username=os.getenv("REDDIT_USERNAME"),
                  password=os.getenv("REDDIT_PASSWORD"))

last="" ## quite surprising, low effort logic has been created

subreddit = app.subreddit("Hololive")
while 1:
    for submission in subreddit.new(limit=1):
        if last != submission:
            print(discordPush(submission))
        last=submission