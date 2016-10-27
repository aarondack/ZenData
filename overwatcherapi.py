from flask import Flask
from flask_restful import Resource, Api
from lxml import html
import requests


app = Flask(__name__)
api = Api(app)

class OverWatcher(Resource):
    def get(self):
        page = requests.get('https://playoverwatch.com/en-us/career/psn/lSN00KI')
        tree = html.fromstring(page.content)
        stat = tree.xpath('//div[@class="card-content"]//text()')
        return(stat)

api.add_resource(OverWatcher, '/')

if __name__ == '__main__':
    app.run(debug=True)
