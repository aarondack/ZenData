import re
from flask import Flask, render_template, jsonify, abort, request
from competitive import build_competitive_average, build_combat_total, hero_list, api_fetch, build_top_heroes, user_achievements, build_about_user, build_winloss

app = Flask(__name__, template_folder="../client")

headers = ['Combat', 'Assists', 'Best', 'Deaths', 'Match Awards', 'Game', 'Miscellaneous']
hero_headers = ['Hero Specific','Combat', 'Assists', 'Best', 'Deaths', 'Match Awards', 'Game', 'Miscellaneous']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/<string:owUser>/<string:owCtry>', methods=['GET'])
def get_combat_averages(owUser, owCtry):
    statBase = {}
    tree = api_fetch(owUser,owCtry)
    stats = tree.xpath('//div[@id="competitive"]//div[@data-group-id="stats" and @data-category-id="0x02E00000FFFFFFFF"]//text()')

    games_data = build_winloss(stats)
    total = build_combat_total(stats, headers)
    averages = build_competitive_average(tree.xpath('//div[@id="competitive"]//ul//text()'))
    about = build_about_user(tree.xpath('//img[@class="player-portrait"]/@src'))

    statBase['about'] = about
    statBase['averages'] = averages
    statBase['stats'] = total
    statBase['winData'] = games_data
    return jsonify(statBase)

@app.route('/api/<string:owUser>/<string:owCtry>/HeroData', methods=['GET'])
def get_hero_data(owUser, owCtry):
    tree = api_fetch(owUser, owCtry)
    heroes = request.args.getlist('heroes')
    hero_data = {}
    for hero in heroes:
        abort_if_no_hero_hash(hero)
        hash_hero = hero_list[hero]
        hero_data[hero] = build_combat_total(tree.xpath('//div[@id="competitive"]//div[@data-group-id="stats" and @data-category-id="{}"]//text()'.format(hash_hero)), hero_headers)
    return jsonify(hero_data)

@app.route('/api/<string:owUser>/<string:owCtry>/achievements', methods=['GET'])
def get_user_achievements(owUser, owCtry):
    tree = api_fetch(owUser, owCtry)
    achievements = user_achievements(tree)
    return jsonify(achievements)

@app.route('/api/<string:owUser>/<string:owCtry>/topheroes', methods=['GET'])
def get_top_heroes(owUser, owCtry):
    tree = api_fetch(owUser, owCtry)
    top_heroes = build_top_heroes(tree)
    return jsonify(top_heroes)

def abort_if_no_hero_hash(hero):
    if hero not in hero_list:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
