from flask_restplus import Api
from .tweet import tweet_ns

api = Api(prefix='/api', doc='/doc')
api.add_namespace(tweet_ns)
