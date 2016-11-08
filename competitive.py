import re

def build_competitive_average(tree):
    competitive_averages = {}
    for value in range(len(tree)):
        regexr = re.match(r'^.*?(?=-)', tree[value])
        if regexr:
            competitive_averages[regexr.group(0)] = tree[value-1]
    return competitive_averages
