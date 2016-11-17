#API
####Returns a blob of information about your profile including averages as well as complete combat stats for all heroes.
<pre><b>GET /api/:battlenet</b></pre>

Example:
<pre><i>https://foobar.com/api/alexthecat</i></pre>

Returns:
```javascript
{
    "averages": {
        "Damage Done ": "8,958",
        "Deaths ": "8.82",
        "Eliminations ": "23.68",
        "Final Blows ": "9.19",
        "Healing Done ": "4,472",
        "Objective Kills ": "11.22",
        "Objective Time ": "01:20",
        "Solo Kills ": "1.51"
    },
    "stats": {
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
}
```
####Returns hero level statistics for the given battlenet user.
<pre><b>GET /api/:battlenet/[:hero]</b></pre>

Example:
<pre><i>https://foobar.com/api/alexthecat/HeroData?heroes=zenyatta&heroes=reaper</i></pre>
Returns:
```javascript
{
  "reaper": {
    "Assists": {
      "Healing Done": "8,430",
      "Self Healing": "8,430",
      "Teleporter Pad Destroyed": "1",
      "Turret Destroyed": "1"
    },
    "Best": {
      "Average": "Melee Final Blows - Average",
      "Critical Hits - Most in Game": "117",
      "Critical Hits - Most in Life": "49",
      "Damage Done - Average": "10,234.65",
      "Damage Done - Most in Game": "12,052",
      "Damage Done - Most in Life": "4,442",
      "Deaths - Average": "9.83",
      "Eliminations - Average": "29.69",
      "Eliminations - Most in Game": "42",
      "Eliminations - Most in Life": "13",
      "Final Blows - Average": "17.11",
      "Final Blows - Most in Game": "25",
      "Healing Done - Average": "797.19",
      "Healing Done - Most in Game": "912",
      "Healing Done - Most in Life": "383",
      "Kill Streak - Best": "13",
      "Melee Final Blows - Average": "0.09",
      "Objective Kills - Average": "12.19",
      "Objective Kills - Most in Game": "23",
      "Objective Time - Average": "01:02",
      "Objective Time - Most in Game": "01:26",
      "Self Healing - Average": "0.95",
      "Self Healing - Most in Game": "912",
      "Solo Kills - Average": "4.44",
      "Solo Kills - Most in Game": "6",
      "Weapon Accuracy - Best in Game": "43%"
    },
    "Combat": {
      "Critical Hit Accuracy": "7%",
      "Critical Hits": "1,123",
      "Critical Hits per Minute": "0.12",
      "Damage Done": "108,227",
      "Eliminations": "314",
      "Eliminations per Life": "3.01",
      "Final Blows": "181",
      "Melee Final Blow": "1",
      "Multikills": "7",
      "Objective Kills": "129",
      "Shots Fired": "52,040",
      "Shots Hit": "14,858",
      "Solo Kills": "47",
      "Weapon Accuracy": "28%"
    },
    ...
  },
  "zenyatta": {
    "Assists": {
      "Healing Done": "350,832",
      "Offensive Assists": "1,289",
      "Self Healing": "12,361",
      "Turrets Destroyed": "6"
    },
    "Best": {
      "Average": "Self Healing - Average",
      "Critical Hits - Most in Game": "21",
      "Critical Hits - Most in Life": "11",
      "Damage Done - Average": "8,559.44",
      "Damage Done - Most in Game": "13,798",
      "Damage Done - Most in Life": "6,651",
      "Deaths - Average": "6.92",
      "Eliminations - Average": "21.33",
      "Eliminations - Most in Game": "41",
      "Eliminations - Most in Life": "14",
      "Final Blows - Average": "8.56",
      "Final Blows - Most in Game": "16",
      "Healing Done - Average": "6,166.96",
      "Healing Done - Most in Game": "10,852",
      "Healing Done - Most in Life": "4,657",
      "Kill Streak - Best": "14",
      "Objective Kills - Average": "9.75",
      "Objective Kills - Most in Game": "24",
      "Objective Time - Average": "00:40",
      "Objective Time - Most in Game": "01:48",
      "Offensive Assists - Average": "23",
      "Offensive Assists - Most in Game": "49",
      "Self Healing - Average": "0.31",
      "Self Healing - Most in Game": "798",
      "Solo Kills - Average": "1.1",
      "Solo Kills - Most in Game": "3",
      "Weapon Accuracy - Best in Game": "44%"
    },
    "Combat": {
      "Critical Hit Accuracy": "6%",
      "Critical Hits": "653",
      "Critical Hits per Minute": "0.01",
      "Damage Done": "486,938",
      "Eliminations": "1,214",
      "Eliminations per Life": "3.08",
      "Final Blows": "487",
      "Multikills": "4",
      "Objective Kills": "555",
      "Shots Fired": "33,573",
      "Shots Hit": "9,554",
      "Solo Kills": "63",
      "Weapon Accuracy": "28%"
    },
    ...
  }
}
```

####Returns Top Heroes statistics based on Time Played, Games Won, Win%, etc.
<pre><b>GET /api/:battlenet/topheroes</b></pre>

Example:
<pre><i>https://foobar.com/api/alexthecat/topheroes</i></pre>
Returns:

```javascript
{
    "Eliminations Per Life": {
        "Ana": "1.42",
        "Bastion": "0",
        "D.Va": "6.26",
        "Genji": "0",
        "Hanzo": "2.5",
        "Junkrat": "1.61",
        "L\u00facio": "2.52",
        "McCree": "1.72",
        "Mei": "1.92",
        "Mercy": "0",
        "Pharah": "1.82",
        "Reaper": "2.73",
        "Reinhardt": "1.32",
        "Roadhog": "2.5",
        "Soldier: 76": "0",
        "Symmetra": "0",
        "Torbj\u00f6rn": "0",
        "Tracer": "1",
        "Widowmaker": "0",
        "Winston": "2.65",
        "Zarya": "0",
        "Zenyatta": "3.1",
    },
    "Games Won": {
        "Ana": "15",
        "Bastion": "0",
        "D.Va": "15",
        "Genji": "0",
        "Hanzo": "0",
        "Junkrat": "1",
        "L\u00facio": "9",
        "McCree": "1",
        "Mei": "1",
        "Mercy": "0",
        "Pharah": "1",
        "Reaper": "3",
        "Reinhardt": "2",
        "Roadhog": "9",
        "Soldier: 76": "0",
        "Symmetra": "0",
        "Torbj\u00f6rn": "0",
        "Tracer": "0",
        "Widowmaker": "0",
        "Winston": "3",
        "Zarya": "0",
        "Zenyatta": "32",
    },
    "Objective Kills - Average": {
        "Ana": "6.49",
        "Bastion": "0",
        "D.Va": "18.6",
        "Genji": "0",
        "Hanzo": "13.42",
        "Junkrat": "9.62",
        "L\u00facio": "15.16",
        "McCree": "3.77",
        "Mei": "11.01",
        "Mercy": "0",
        "Pharah": "10.92",
        "Reaper": "11.21",
        "Reinhardt": "6.16",
        "Roadhog": "10.49",
        "Soldier: 76": "0",
        "Symmetra": "0",
        "Torbj\u00f6rn": "0",
        "Tracer": "0",
        "Widowmaker": "16.86",
        "Winston": "15.06",
        "Zarya": "0",
        "Zenyatta": "9.69",
    },
    "Time Played": {
        "Ana": "6 hours",
        "Bastion": "--",
        "D.Va": "6 hours",
        "Genji": "2 seconds",
        "Hanzo": "4 minutes",
        "Junkrat": "42 minutes",
        "L\u00facio": "3 hours",
        "McCree": "29 minutes",
        "Mei": "1 hour",
        "Mercy": "2 minutes",
        "Pharah": "20 minutes",
        "Reaper": "2 hours",
        "Reinhardt": "55 minutes",
        "Roadhog": "4 hours",
        "Soldier: 76": "10 seconds",
        "Symmetra": "--",
        "Torbj\u00f6rn": "--",
        "Tracer": "48 seconds",
        "Widowmaker": "58 seconds",
        "Winston": "1 hour",
        "Zarya": "--",
        "Zenyatta": "10 hours",
    },
    ...
}
```

####Returns achievements such as Defense, Maps, Offense for the given battlenet user in Overwatch.
<pre><b>GET /api/:battlenet/achievements</b></pre>

Example:
<pre><i>https://foobar.com/api/alexthecat/achievements</i></pre>
Returns:

```javascript
{
    "Defense": {
        "Armor Up!": false,
        "Charge!": false,
        "Cold Snap": true,
        "Did That Sting?": false,
        "Ice Blocked": true,
        "Mine Like a Steel Trap": true,
        "Raid Wipe": true,
        "Roadkill": true,
        "Simple Geometry": false,
        "Smooth as Silk": false,
        "The Dragon Is Sated": false,
        "Triple Threat": false
    },
    "General": {
        "Blackjack": true,
        "Centenary": true,
        "Decked Out": false,
        "Decorated": true,
        "Level 10": true,
        "Level 25": true,
        "Level 50": true,
        "Survival Expert": false,
        "The Friend Zone": true,
        "The Path Is Closed": false,
        "Undying": true
    },
    "Maps": {
        "Can't Touch This": true,
        "Double Cap": true,
        "Escort Duty": true,
        "Lockdown": true,
        "Shutout": true,
        "World Traveler": true
    },
    "Offense": {
        "Clearing the Area": false,
        "Death From Above": false,
        "Die Die Die... Die": true,
        "It's High Noon": false,
        "Rocket Man": false,
        "Slice and Dice": false,
        "Special Delivery": false,
        "Target Rich Environment": false,
        "Their Own Worst Enemy": false,
        "Total Recall": false,
        "Waste Not, Want Not": true,
        "Whoa There!": true
    },
    "Support": {
        "Enabler": true,
        "Group Health Plan": false,
        "Huge Rez": false,
        "Huge Success": false,
        "Naptime": true,
        "Rapid Discord": false,
        "Supersonic": true,
        "The Car Wash": false,
        "The Floor Is Lava": false,
        "The Iris Embraces You": true
    },
    "Tank": {
        "Anger Management": true,
        "Game Over": true,
        "Giving You the Hook": true,
        "Hog Wild": false,
        "I Am Your Shield": false,
        "Mine Sweeper": true,
        "Power Overwhelming": true,
        "Shot Down": true,
        "Storm, Earth and Fire": true,
        "The Power of Attraction": false
    }
}
```
####TODO
* ~~/heroes endpoint accept array of heroes~~
* ~~/achievements~~
* ~~Top hero stats~~
* ~~playtimes for heroes~~
* support countries, platforms
* ~~extract duplicate logic into outside func~~
