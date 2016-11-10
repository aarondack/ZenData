import re
import requests
from lxml import html

hero_list = {
    'reaper': '0x02E0000000000002',
    'tracer': '0x02E0000000000003',
    'mercy': '0x02E0000000000004',
    'hanzo': '0x02E0000000000005',
    'reinhardt': '0x02E0000000000007',
    'pharah': '0x02E0000000000008',
    'winston': '0x02E0000000000009',
    'widowmaker': '0x02E000000000000A',
    'zenyatta': '0x02E0000000000020',
    'genji': '0x02E0000000000029',
    'roadhog': '0x02E0000000000040',
    'mccree': '0x02E0000000000042',
    'junkrat': '0x02E0000000000065',
    'soldier-76': '0x02E000000000006E',
    'lucio': '0x02E0000000000079',
    'dva': '0x02E000000000007A',
    'mei': '0x02E00000000000DD',
    'ana': '0x02E000000000013B'
}

URL = 'https://playoverwatch.com/en-us/career/psn/'

def api_fetch(owUser):
    page = requests.get(URL + owUser)
    tree = html.fromstring(page.content)
    return tree

def build_competitive_average(tree):
    competitive_averages = {}
    for value in range(len(tree)):
        regexr = re.match(r'^.*?(?=-)', tree[value])
        if regexr:
            competitive_averages[regexr.group(0)] = tree[value-1]
    return competitive_averages

def build_combat_total(tree, headers):
    root_header = ''
    competitive_stats = {}
    for value in range(len(tree) - 1):
        if any(x == tree[value] for x in headers):
            competitive_stats[tree[value]] = {}
            root_header = tree[value]
        else:
            if re.match(r'[a-zA-Z]+', tree[value]):
                competitive_stats[root_header][tree[value]] = tree[value+1]
    return competitive_stats
