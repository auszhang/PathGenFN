import networkx as nx

G = nx.graph()

# Named locations only, for now
POI_list = ["Lonely Lodge", "Retail Row", "Flush Factory", "Anarchy Acres", "Shifty Shafts", "Greasy Grove",
            "Risky Reels", "Fatal Fields", "Lucky Landing", "Junk Junction", "Snobby Shores", "Pleasant Park",
            "Salty Springs", "Moisty Mire", "Loot Lake", "Dusty Divot", "Tilted Towers", "Haunted Hills",
            "Tomato Town"]

G.add_nodes_from(POI_list)


# Number of chests pulled from fortnitechests.info, with some personal digression
# For Risky Reels, I excluded the side houses
# For Moisty Mire, I counted filmset only
# Tomato Town includes the overpass
POI_dict = {"Lonely Lodge": 12, "Retail Row": 18, "Flush Factory": 12, "Anarchy Acres": 13,
            "Shifty Shafts": 12, "Greasy Grove": 15, "Risky Reels": 16, "Fatal Fields": 18,
            "Lucky Landing": 14, "Junk Junction": 10, "Snobby Shores": 11, "Pleasant Park": 17,
            "Salty Springs": 13, "Moisty Mire": 11, "Loot Lake": 17, "Dusty Divot": 17,
            "Tilted Towers": 34, "Haunted Hills": 11, "Tomato Town": 5}
# How about ditching scores for POI?
#   Or maybe we can keep it, but simplify scores instead:
#       So, something like Tilted: 3, Lonely: 2, Crates: 1
# If we get rid of scores for POI, then we don't need to worry about whether a team looted a place
#   and that affecting the POI's actual value.

# Function that generates edges based on user inputs
# Call this function in main.py (but where?)
# INPUTS: either string (POI) or tuple of string (coordinates)

















