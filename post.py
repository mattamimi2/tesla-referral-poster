import os
import praw
import random

reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_SECRET"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"],
    user_agent="tesla-referral-poster by " + os.environ["REDDIT_USERNAME"],
)

link = os.environ["REFERRAL_LINK"]

subreddits = ["TeslaReferralCodeClub", "teslareferralcode", "TeslaReferralsCode"]

titles = [
    "Get a free month of Full Self-Driving (Supervised) when you use my link",
    "Tesla referral link - free month of FSD Supervised",
    "Free FSD trial with my Tesla referral code",
]

for sub in subreddits:
    title = random.choice(titles)
    reddit.subreddit(sub).submit(
        title=title,
        selftext=f"Get a free month of Full Self-Driving (Supervised) when you use my link.\n\n{link}\n\nHappy to answer any questions about ownership!",
    )
    print(f"Posted to r/{sub}")

print("All posts done!")
