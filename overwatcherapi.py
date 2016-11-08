from flask import Flask
from flask_restful import Resource, Api
from lxml import html
from dictionary import build_competitive_average
import requests

app = Flask(__name__)
api = Api(app)

class OverWatcher(Resource):
    def get(self, owUser):
        statBase = []
        page = requests.get('https://playoverwatch.com/en-us/career/psn/' + owUser)
        tree = html.fromstring(page.content)
        stat = tree.xpath('//div[@id="competitive-play"]//ul//text()')
        stat1 = tree.xpath('//div[@id="competitive-play"]//div[@data-group-id="stats"]//text()')
        stat2 = build_competitive_average(stat, 'averages')
        statBase.append(stat)
        statBase.append(stat1)
        return(statBase)

api.add_resource(OverWatcher, '/<string:owUser>')

if __name__ == '__main__':
    app.run(debug=True)
