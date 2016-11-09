from flask import Flask
from flask_restful import Resource, Api, abort
from lxml import html
from competitive import build_competitive_average, build_combat_total, hero_list
import requests

app = Flask(__name__)
api = Api(app)

headers = ['Combat', 'Assists', 'Best', 'Deaths', 'Match Awards', 'Game', 'Miscellaneous']
hero_headers = ['Hero Specific','Combat', 'Assists', 'Best', 'Deaths', 'Match Awards', 'Game', 'Miscellaneous']

URL = 'https://playoverwatch.com/en-us/career/psn/'

class OverWatcher(Resource):
    def get(self, owUser):
        statBase = []
        page = requests.get(URL + owUser)
        tree = html.fromstring(page.content)
        stats = tree.xpath('//div[@id="competitive-play"]//div[@data-group-id="stats" and @data-category-id="0x02E00000FFFFFFFF"]//text()')

        total = build_combat_total(stats, headers)
        averages = build_competitive_average(tree.xpath('//div[@id="competitive-play"]//ul//text()'))

        statBase.extend((averages, total))
        return(statBase)

class HeroData(Resource):
    def get(self, owUser, hero):
        page = requests.get(URL + owUser)
        tree = html.fromstring(page.content)
        abort_if_no_hero_hash(hero)

        hash_hero = hero_list[hero]
        hero_stat = tree.xpath('//div[@id="competitive-play"]//div[@data-group-id="stats" and @data-category-id="{}"]//text()'.format(hash_hero))

        format_stats = build_combat_total(hero_stat, hero_headers)
        return format_stats

def abort_if_no_hero_hash(hero):
    if hero not in hero_list:
        abort(404, message="That hero does not exist")

api.add_resource(OverWatcher, '/<string:owUser>')
api.add_resource(HeroData, '/<string:owUser>/<string:hero>')

if __name__ == '__main__':
    app.run(debug=True)
