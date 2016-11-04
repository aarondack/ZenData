from flask import Flask
from flask_restful import Resource, Api
from lxml import html
import requests


app = Flask(__name__)
api = Api(app)

class OverWatcher(Resource):
    def get(self, owUser):
        statBase = []
        page = requests.get('https://playoverwatch.com/en-us/career/psn/' + owUser)
        tree = html.fromstring(page.content)
        stat = tree.xpath('//div[@class="card-content"]//text()')
        stat1= tree.xpath('//div[@data-group-id="stats"]//text()')
        statBase.append(stat)
        statBase.append(stat1)
        return(statBase)

api.add_resource(OverWatcher, '/<string:owUser>')

if __name__ == '__main__':
    app.run(debug=True)
