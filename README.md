#ZenData
This is an API currently in building phases for getting read-only information about players and their heroes from overwatch.

#API
####Returns a blob of information about your profile including averages as well as complete combat stats for all heroes.
<pre><b>GET /api/{battlenet}</b></pre>

Example:
<pre><i>https://foobar.com/api/alexthecat</i></pre>

Returns:
```javascript
[
    {
        "Damage Done ": "8,958",
        "Deaths ": "8.82",
        "Eliminations ": "23.68",
        "Final Blows ": "9.19",
        "Healing Done ": "4,472",
        "Objective Kills ": "11.22",
        "Objective Time ": "01:20",
        "Solo Kills ": "1.51"
    },
    {
        "Assists": {
            "Healing Done": "778,122",
            "Recon Assist": "1",
            "Teleporter Pads Destroyed": "3"
        },
        "Best": {
            "Average": "Melee Final Blows - Average",
            "Damage Done - Average": "8,958",
            "Damage Done - Most in Game": "35,731",
            "Deaths - Average": "8.82",
            "Defensive Assists - Most in Game": "41",
            "Eliminations - Average": "23.68",
            "Eliminations - Most in Game": "71",
            "Final Blows - Average": "9.19",
            "Final Blows - Most in Game": "31",
            "Healing Done - Average": "4,472",
            "Healing Done - Most in Game": "16,955",
            "Melee Final Blows - Average": "0.04",
            "Multikill - Best": "5",
            "Objective Kills - Average": "11.22",
            "Objective Kills - Most in Game": "45",
            "Objective Time - Average": "01:20",
            "Objective Time - Most in Game": "05:33",
            "Offensive Assists - Most in Game": "49",
            "Solo Kills - Average": "1.51",
            "Solo Kills - Most in Game": "31",
            "Time Spent on Fire - Average": "01:51",
            "Time Spent on Fire - Most in Game": "08:26"
        },
        "Combat": {
            "Damage Done": "1,558,626",
            "Eliminations": "4,121",
            "Environmental Kills": "26",
            "Final Blows": "1,600",
            "Melee Final Blows": "7",
            "Multikills": "35",
            "Objective Kills": "1,954",
            "Solo Kills": "263"
        },
        "Deaths": {
            "Environmental Deaths": "44"
        },
        "Game": {
            "Games Played": "174",
            "Games Won": "89",
            "Objective Time": "03:53:34",
            "Time Played": "37 hours",
            "Time Spent on Fire": "05:21:54"
        },
        "Match Awards": {
            "Cards": "64",
            "Medals": "437",
            "Medals - Bronze": "148",
            "Medals - Gold": "126",
            "Medals - Silver": "163"
        },
        "Miscellaneous": {
            "Defensive Assists": "1,695",
            "Defensive Assists - Average": "10",
            "Games Lost": "77",
            "Games Tied": "8",
            "Melee Final Blow - Most in Game": "1",
            "Offensive Assists": "1,453",
            "Offensive Assists - Average": "8"
        }
    }
]
```
####Returns hero level statistics for the given battlenet user. Currently only accepts one, but want to expand to take multiple.
<pre><b>GET /api/{battlenet}/{hero}</b></pre>

Example:
<pre><i>https://foobar.com/api/alexthecat/zenyatta</i></pre>
Returns:
```javascript
{
    "Assists": {
        "Healing Done": "298,207",
        "Offensive Assists": "1,120",
        "Self Healing": "9,813",
        "Turrets Destroyed": "6"
    },
    "Best": {
        "Critical Hits - Most in Game": "21",
        "Critical Hits - Most in Life": "10",
        "Damage Done - Average": "8,321.06",
        "Damage Done - Most in Game": "10,921",
        "Damage Done - Most in Life": "4,733",
        "Deaths - Average": "6.95",
        "Eliminations - Average": "21.32",
        "Eliminations - Most in Game": "41",
        "Eliminations - Most in Life": "14",
        "Final Blows - Average": "8.4",
        "Final Blows - Most in Game": "16",
        "Healing Done - Average": "6,027.65",
        "Healing Done - Most in Game": "8,426",
        "Healing Done - Most in Life": "4,466",
        "Kill Streak - Best": "14",
        "Objective Kills - Average": "9.82",
        "Objective Kills - Most in Game": "24",
        "Objective Time - Average": "00:39",
        "Objective Time - Most in Game": "01:41",
        "Offensive Assists - Average": "23",
        "Offensive Assists - Most in Game": "49",
        "Self Healing - Average": "0.29",
        "Self Healing - Most in Game": "467",
        "Solo Kills - Average": "1.03",
        "Solo Kills - Most in Game": "3",
        "Weapon Accuracy - Best in Game": "44%"
    },
    "Combat": {
        "Critical Hit Accuracy": "6%",
        "Critical Hits": "556",
        "Critical Hits per Minute": "0.01",
        "Damage Done": "411,669",
        "Eliminations": "1,055",
        "Eliminations per Life": "3.06",
        "Final Blows": "416",
        "Multikills": "4",
        "Objective Kills": "486",
        "Shots Fired": "28,434",
        "Shots Hit": "8,056",
        "Solo Kills": "51",
        "Weapon Accuracy": "28%"
    },
    "Deaths": {
        "Environmental Deaths": "3"
    },
    "Game": {
        "Games Played": "49",
        "Games Won": "29",
        "Objective Time": "32:34",
        "Time Played": "9 hours",
        "Time Spent on Fire": "02:58:03",
        "Win Percentage": "58%"
    },
    "Hero Specific": {
        "Transcendence Healing - Best": "1,491"
    },
    "Match Awards": {
        "Cards": "33",
        "Medals": "124",
        "Medals - Bronze": "41",
        "Medals - Gold": "32",
        "Medals - Silver": "50"
    },
    "Miscellaneous": {
        "Defensive Assists": "1,004",
        "Defensive Assists - Average": "20",
        "Defensive Assists - Most in Game": "41",
        "Games Lost": "19",
        "Games Tied": "2",
        "Healing Done": "298,207",
        "Healing Done - Average": "6,028",
        "Multikill - Best": "3",
        "Transcendence Healing": "83,748"
    }
}
```

####TODO
* /heroes endpoint accept array of heroes
* /achievements
* quickplay
* playtimes for heroes
