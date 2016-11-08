import re

def build_competitive_average(tree, averages):
    competitive_averages = { averages: {} }
    for value in range(len(tree)):
        print(tree[value])
        regexr = re.match(r'[a-zA-Z]+', tree[value])
        if regexr:
            competitive_averages[averages][regexr.group(0)] = tree[value-1]
        else:
            continue
    return competitive_averages
