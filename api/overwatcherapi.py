from flask import Flask
from flask_restful import Resource, Api, abort
from competitive import build_competitive_average, build_combat_total, hero_list, api_fetch, build_top_heroes

app = Flask(__name__)
api = Api(app)

headers = ['Combat', 'Assists', 'Best', 'Deaths', 'Match Awards', 'Game', 'Miscellaneous']
hero_headers = ['Hero Specific','Combat', 'Assists', 'Best', 'Deaths', 'Match Awards', 'Game', 'Miscellaneous']


class OverWatcher(Resource):
    def get(self, owUser):
        statBase = {}
        tree = api_fetch(owUser)
        stats = tree.xpath('//div[@id="competitive"]//div[@data-group-id="stats" and @data-category-id="0x02E00000FFFFFFFF"]//text()')

        total = build_combat_total(stats, headers)
        averages = build_competitive_average(tree.xpath('//div[@id="competitive"]//ul//text()'))

        statBase['averages'] = averages
        statBase['stats'] = total
        return(statBase)

class HeroData(Resource):
    def get(self, owUser, hero):
        tree = api_fetch(owUser)
        abort_if_no_hero_hash(hero)

        hash_hero = hero_list[hero]
        hero_stat = tree.xpath('//div[@id="competitive"]//div[@data-group-id="stats" and @data-category-id="{}"]//text()'.format(hash_hero))

        format_stats = build_combat_total(hero_stat, hero_headers)
        return format_stats

class UserAchievements(Resource):
    def get(self, owUser):
        tree = api_fetch(owUser)
        achievements = tree.xpath('//div[@data-category-id="overwatch.achievementCategory.0"]//text()')
        return achievements

class TopHeroes(Resource):
    def get(self, owUser):
        tree = api_fetch(owUser)
        top_heroes = build_top_heroes(tree)
        return top_heroes


def abort_if_no_hero_hash(hero):
    if hero not in hero_list:
        abort(404, message="That hero does not exist")

api.add_resource(OverWatcher, '/api/<string:owUser>')
api.add_resource(HeroData, '/api/<string:owUser>/<string:hero>')
api.add_resource(UserAchievements, '/api/<string:owUser>/achievements')
api.add_resource(TopHeroes, '/api/<string:owUser>/topheroes')

if __name__ == '__main__':
    app.run(debug=True)
