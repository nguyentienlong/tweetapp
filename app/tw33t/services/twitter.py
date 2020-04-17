from twitter import TwitterError

from app.tw33t import app

import twitter
api = twitter.Api(
    consumer_key=app.config['TWITTER_API_KEY'],
    consumer_secret=app.config['TWITTER_SECRET_KEY'],
    access_token_key=app.config['TWITTER_ACCESS_TOKEN'],
    access_token_secret=app.config['TWITTER_ACCESS_TOKEN_SECRET']
)


def get_tweets(twitter_handle):
    try:
        statuses = api.GetUserTimeline(
            screen_name=twitter_handle,
            exclude_replies=True
        )
    except TwitterError as e:
        app.logger.exception(e)
        raise e

    tweets = [s.text for s in statuses]
    limit = app.config['TWITTER_TWEETS_LIMIT']

    return tweets[:limit] if len(tweets) > limit else tweets
