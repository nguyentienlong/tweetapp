import time

from flask_restplus import Namespace, Resource, fields, abort

from app.tw33t import app
from app.tw33t.services import twitter

tweet_ns = Namespace('tweet', description='Tweet Endpoint')

tweets_model = tweet_ns.model('Tweets', {
    'tweets': fields.List(fields.String(required=True, description='A tweet'))
})

success_model = tweet_ns.model('Success Response', {
    'message': fields.String,
    'data': fields.Nested(tweets_model)
})

notfound_model = tweet_ns.model('Error Response', {
    'message': fields.String
})


@tweet_ns.route('/<string:twitter_handle>', endpoint='index')
@tweet_ns.doc(params={'twitter_handle': 'A twitter handle'})
class IndexPage(Resource):

    @tweet_ns.response(model=success_model, code=200, description='Get tweets successfully')
    @tweet_ns.response(model=notfound_model, code=400, description='No tweet found')
    def get(self, twitter_handle):
        try:
            tweets = twitter.get_tweets(twitter_handle)
            app.logger.info('Tweets for {} : {}'.format(twitter_handle, tweets))
        except Exception as e:
            abort(400, 'No tweet found')

        if len(tweets) == 0:
            abort(400, 'No tweet found')

        return {
            'message': 'ok',
            'data': {'tweets': tweets}
        }
