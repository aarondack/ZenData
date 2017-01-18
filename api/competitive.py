import re
import requests
from flask import request
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

top_heroes = {
    'Time Played': 'overwatch.guid.0x0860000000000021',
    'Games Won': 'overwatch.guid.0x0860000000000039',
    'Win Percentage': 'overwatch.guid.0x08600000000003D1',
    'Weapon Accuracy': 'overwatch.guid.0x086000000000002F',
    'Eliminations Per Life': 'overwatch.guid.0x08600000000003D2',
    'Multikill - Best': 'overwatch.guid.0x0860000000000346',
    'Objective Kills - Average': 'overwatch.guid.0x086000000000039C'
}

achievements = {
    'General': 'overwatch.achievementCategory.0',
    'Offense': 'overwatch.achievementCategory.1',
    'Defense': 'overwatch.achievementCategory.2',
    'Tank': 'overwatch.achievementCategory.3',
    'Support': 'overwatch.achievementCategory.4',
    'Maps': 'overwatch.achievementCategory.5',
}
# Adding some CTRY_URL into the PSN_URL so we can make this more dynamic later if we'd like
CTRY_URL = '/en-us/'
PSN_URL = 'https://playoverwatch.com/en-us/career/psn/'

def api_fetch(owUser, owCtry):
    platform = request.args.get('platform')
    if platform:
        platform_url = 'https://playoverwatch.com/en-us/career/'+ platform + '/'
        page = requests.get(platform_url + owUser)
        tree = html.fromstring(page.content)
        return tree
    countrl = 'https://playoverwatch.com/{}/career/psn/'.format(owCtry) 
    page = requests.get(countrl + owUser)
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

def build_top_heroes(tree):
    top_heroes_stats = {}
    for key, value in top_heroes.items():
        each_top_hero_stats = top_heroes_processing(tree.xpath('//div[@id="competitive"]//div[@data-group-id="comparisons" and @data-category-id="{}"]//text()'.format(value)))
        top_heroes_stats[key] = each_top_hero_stats
    return top_heroes_stats

def top_heroes_processing(tree):
    top_heroes_processing = {}
    for value in range(len(tree)):
        if re.match(r'[a-zA-Z]+', tree[value]):
            if tree[value] == 'overwatch.guid.undefined':
                continue
            top_heroes_processing[tree[value]] = tree[value+1]
    return top_heroes_processing

def user_achievements(tree):
    user_achievements = {}
    for key, value in achievements.items():
        each_achievement = achievement_processing(tree.xpath('//div[@data-category-id="{}"]//div[@class="tooltip media-card achievement-card"]//text()'.format(value)),
        tree.xpath('//div[@data-category-id="{}"]//div[@class="tooltip media-card achievement-card m-disabled"]//text()'.format(value)))
        user_achievements[key] = each_achievement
    return user_achievements

def achievement_processing(achieved, pending):
    processed_achievements = {}
    for value in achieved:
        if value == '?':
            continue
        processed_achievements[value] = True
    for value in pending:
        if value == '?':
            continue
        processed_achievements[value] = False
    return processed_achievements

def build_about_user(tree):
    user_info = {}
    platform = request.args.get('platform')
    if platform:
        user_info['platform'] = platform
        user_info['avatar'] = ''.join(tree)
    else:
        user_info['platform'] = 'psn'
        user_info['avatar'] = ''.join(tree)
    return user_info
