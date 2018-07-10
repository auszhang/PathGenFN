import math
import networkx as nx

G = nx.Graph()

# Named locations only, for now
POI_list = ["Lonely Lodge", "Retail Row", "Flush Factory", "Anarchy Acres", "Shifty Shafts", "Greasy Grove",
            "Risky Reels", "Fatal Fields", "Lucky Landing", "Junk Junction", "Snobby Shores", "Pleasant Park",
            "Salty Springs", "Moisty Mire", "Loot Lake", "Dusty Divot", "Tilted Towers", "Haunted Hills",
            "Tomato Town"]

G.add_nodes_from(POI_list)


# Number of chests pulled from fortnitechests.info, with some personal digression
# For Risky Reels, I excluded the side houses
# For Moisty Mire, I counted filmset only
# For Tomato Town, I included the overpass
POI_dict = {"Lonely Lodge": [12, (91, 41)], "Retail Row": [18, (75, 53)], "Flush Factory": [12, (34, 88)],
            "Anarchy Acres": [13, (52, 22)], "Shifty Shafts": [12, (36, 64)], "Greasy Grove": [15, (22, 62)],
            "Risky Reels": [16, (75, 19)], "Fatal Fields": [18, (61, 76)], "Lucky Landing": [14, (57, 92)],
            "Junk Junction": [10, (18, 11)], "Snobby Shores": [11, (4, 44)], "Pleasant Park": [17, (27, 28)],
            "Salty Springs": [13, (57, 61)], "Moisty Mire": [11, (83, 80)], "Loot Lake": [17, (40, 36)],
            "Dusty Divot": [17, (60, 50)], "Tilted Towers": [34, (37, 48)], "Haunted Hills": [11, (13, 19)],
            "Tomato Town": [5, (67, 30)]}


# INPUTS: either string (POI) or tuple of int (coordinates)
def distance(c1, c2):
    """Takes set of either POI name/coordinates and returns the distance between them"""
    # Changes from str -> tuple(int)
    if type(c1) == str:
        c1 = POI_dict[c1][1]
    if type(c2) == str:
        c2 = POI_dict[c2][1]

    result_int = round(math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2))  # Distance formula
    return result_int


# Rememeber to convert distance->time
def heuristic():
    pass

