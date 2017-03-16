import re
from flask import Flask, render_template, jsonify, abort, request
from competitive import build_competitive_average, build_combat_total, hero_list, api_fetch, build_top_heroes, user_achievements, build_about_user, build_winloss, check_error

app = Flask(__name__, template_folder="../client")

headers = ['Combat', 'Assists', 'Best', 'Deaths', 'Match Awards', 'Game', 'Miscellaneous']
hero_headers = ['Hero Specific','Combat', 'Assists', 'Best', 'Deaths', 'Match Awards', 'Game', 'Miscellaneous']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/<string:owUser>/', methods=['GET'])
def get_combat_averages(owUser):
    statBase = {}
    tree = api_fetch(owUser)
    stats = tree.xpath('//div[@id="competitive"]//div[@data-group-id="stats" and @data-category-id="0x02E00000FFFFFFFF"]//text()')

    games_data = build_winloss(stats)
    total = build_combat_total(stats, headers)
    averages = build_competitive_average(tree.xpath('//div[@id="competitive"]//ul//text()'))
    about = build_about_user(tree.xpath('//img[@class="player-portrait"]/@src'))

    statBase['about'] = about
    statBase['averages'] = averages
    statBase['stats'] = total
    statBase['winData'] = games_data
    errorVal = check_error(statBase['averages'])
    if errorVal:
        return errorVal
    else:
        return jsonify(statBase)

@app.route('/api/<string:owUser>/HeroData', methods=['GET'])
def get_hero_data(owUser):
    tree = api_fetch(owUser)
    heroes = request.args.getlist('heroes')
    hero_data = {}
    # test url : http://127.0.0.1:5000/api/lSN00KI/HeroData?heroes=zenyatta&heroes=reaper&heroes=roadhog&platform=psn&country=en-us
    for hero in heroes:
        abort_if_no_hero_hash(hero)
        hash_hero = hero_list[hero]
        hero_data[hero] = build_combat_total(tree.xpath('//div[@id="competitive"]//div[@data-group-id="stats" and @data-category-id="{}"]//text()'.format(hash_hero)), hero_headers)
        errorVal = check_error(hero_data[hero])
    if errorVal:
        return errorVal
    else:
        return jsonify(hero_data)

@app.route('/api/<string:owUser>/achievements', methods=['GET'])
def get_user_achievements(owUser):
    tree = api_fetch(owUser)
    achievements = user_achievements(tree)
    errorVal = check_error(achievements['General'])
    if errorVal:
        return errorVal
    else:
        return jsonify(achievements)

@app.route('/api/<string:owUser>/topheroes', methods=['GET'])
def get_top_heroes(owUser):
    tree = api_fetch(owUser)
    top_heroes = build_top_heroes(tree)
    errorVal = check_error(top_heroes['Games Won'])
    if errorVal:
        return errorVal
    else:
        return jsonify(top_heroes)

def abort_if_no_hero_hash(hero):
    if hero not in hero_list:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
