import json

import falcon


class QuoteResource:
    @staticmethod
    def on_get(req, resp):
        quote = {
            'quote': 'Crush your enemies. See them driven before you. Hear the lamentations of their women.',
            'author': 'conan'
        }
        resp.body = json.dump(quote)


if __name__ == "__main__":
    api = falcon.API()
    api.add_route('/quote', QuoteResource())
