from flask import Flask
from flask_restful import Resource, Api
from lxml import html
from competitive import build_competitive_average, build_combat_total
import requests

app = Flask(__name__)
api = Api(app)

headers = ['Combat', 'Assists', 'Best', 'Deaths', 'Match Awards', 'Game', 'Miscellaneous']


class OverWatcher(Resource):
    def get(self, owUser):
        statBase = []
        page = requests.get('https://playoverwatch.com/en-us/career/psn/' + owUser)
        tree = html.fromstring(page.content)
        stat1 = tree.xpath('//div[@id="competitive-play"]//div[@data-group-id="stats" and @data-category-id="0x02E00000FFFFFFFF"]//text()')
        foo = build_combat_total(stat1, headers)
        averages = build_competitive_average(tree.xpath('//div[@id="competitive-play"]//ul//text()'))
        statBase.append(averages)
        statBase.append(foo)
        return(statBase)

api.add_resource(OverWatcher, '/<string:owUser>')

if __name__ == '__main__':
    app.run(debug=True)
