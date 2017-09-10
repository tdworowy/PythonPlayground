import json

import falcon


class QuoteResource:
    def on_get(selfs,req,resp):
        quote={
            'quote':'Crush your enemies. See them driven before you. Hear the lamentations of their women.',
            'author' : 'conan'
        }
        resp.body =json.dump(quote)

api = falcon.API()
api.add_route('/quote',QuoteResource())

