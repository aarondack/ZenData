from flask import Flask, render_template, jsonify, abort
from competitive import build_competitive_average, build_combat_total, hero_list, api_fetch, build_top_heroes, user_achievements

app = Flask(__name__, template_folder="../client")

headers = ['Combat', 'Assists', 'Best', 'Deaths', 'Match Awards', 'Game', 'Miscellaneous']
hero_headers = ['Hero Specific','Combat', 'Assists', 'Best', 'Deaths', 'Match Awards', 'Game', 'Miscellaneous']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/<string:owUser>', methods=['GET'])
def get_combat_averages(owUser):
    statBase = {}
    tree = api_fetch(owUser)
    stats = tree.xpath('//div[@id="competitive"]//div[@data-group-id="stats" and @data-category-id="0x02E00000FFFFFFFF"]//text()')

    total = build_combat_total(stats, headers)
    averages = build_competitive_average(tree.xpath('//div[@id="competitive"]//ul//text()'))

    statBase['averages'] = averages
    statBase['stats'] = total
    return jsonify(statBase)

@app.route('/api/<string:owUser>/<string:hero>', methods=['GET'])
def get_hero_data(owUser, hero):
    tree = api_fetch(owUser)
    abort_if_no_hero_hash(hero)

    hash_hero = hero_list[hero]
    hero_stat = tree.xpath('//div[@id="competitive"]//div[@data-group-id="stats" and @data-category-id="{}"]//text()'.format(hash_hero))

    format_stats = build_combat_total(hero_stat, hero_headers)
    return jsonify(format_stats)

@app.route('/api/<string:owUser>/achievements', methods=['GET'])
def get_user_achievements(owUser):
    tree = api_fetch(owUser)
    achievements = user_achievements(tree)
    return jsonify(achievements)

@app.route('/api/<string:owUser>/topheroes', methods=['GET'])
def get_top_heroes(owUser):
    tree = api_fetch(owUser)
    top_heroes = build_top_heroes(tree)
    return jsonify(top_heroes)

def abort_if_no_hero_hash(hero):
    if hero not in hero_list:
        abort(404)
