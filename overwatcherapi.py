from flask import Flask
from flask_restful import Resource, Api
from lxml import html
from competitive import build_competitive_average
import requests

app = Flask(__name__)
api = Api(app)

class OverWatcher(Resource):
    def get(self, owUser):
        statBase = []
        page = requests.get('https://playoverwatch.com/en-us/career/psn/' + owUser)
        tree = html.fromstring(page.content)
        stat1 = tree.xpath('//div[@id="competitive-play"]//div[@data-group-id="stats"]//text()')
        averages = build_competitive_average(tree.xpath('//div[@id="competitive-play"]//ul//text()'))
        statBase.append(averages)
        statBase.append(stat1)
        return(statBase)

api.add_resource(OverWatcher, '/<string:owUser>')

if __name__ == '__main__':
    app.run(debug=True)
