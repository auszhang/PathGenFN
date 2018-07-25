import math
import networkx as nx

G = nx.Graph()

# Named locations only, for now
POI_list = ["Lonely Lodge", "Retail Row", "Flush Factory", "Anarchy Acres", "Shifty Shafts", "Greasy Grove",
            "Risky Reels", "Fatal Fields", "Lucky Landing", "Junk Junction", "Snobby Shores", "Pleasant Park",
            "Salty Springs", "Loot Lake", "Dusty Divot", "Tilted Towers", "Haunted Hills",
            "Tomato Town", "Lazy Links", "Paradise Palms"]

G.add_nodes_from(POI_list)


# POI_dict is OBSOLETE because of Season 5 update
# Number of chests pulled from fortnitechests.info, with some personal digression
# For Risky Reels, I excluded the side houses
# For Moisty Mire, I counted filmset only
# For Tomato Town, I included the overpass
POI_dict = {"Lonely Lodge": [12, (91, 41)], "Retail Row": [18, (75, 53)], "Flush Factory": [12, (34, 88)],
            "Anarchy Acres": [13, (52, 22)], "Shifty Shafts": [12, (36, 64)], "Greasy Grove": [15, (22, 62)],
            "Risky Reels": [16, (75, 19)], "Fatal Fields": [18, (61, 76)], "Lucky Landing": [14, (57, 92)],
            "Junk Junction": [10, (18, 11)], "Snobby Shores": [11, (4, 44)], "Pleasant Park": [17, (27, 28)],
            "Salty Springs": [13, (57, 61)], "Loot Lake": [17, (40, 36)], "Dusty Divot": [17, (60, 50)],
            "Tilted Towers": [34, (37, 48)], "Haunted Hills": [11, (13, 19)], "Tomato Town": [5, (67, 30)]}


# INPUTS: either string (POI) or tuple of int (coordinates)
def distance(c1, c2):
    """Takes set of either POI name/coordinates and returns the distance between them"""
    # Changes from str -> tuple(int)

    if type(c1) == str:
        c1 = POI_dict[c1][1]
    if type(c2) == str:
        c2 = POI_dict[c2][1]

    result_int = round(math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2), 2)  # Distance formula, rounded to 2 decimals
    return result_int


# 10 units is ~ 74 seconds
def time(c1, c2):
    """Uses results from distance() function and converts to time"""
    return round((74/10) * distance(c1, c2), 2)


def gen_edges():
    for k, v in POI_dict.items():
        for k2, v2 in POI_dict.items():
            if k is not k2:
                G.add_edge(k, k2, weight=time(k, k2))


# Prints edges
# for i, j, d in G.edges(data="weight"):
#     print(i, j, d)


# String processing
# Expected input: "Lonely Lodge", (C-3,6-2)
# Or something like: E-6,3-9 | C-3,6-2 -> (46, 29), . . .

start_node = ""  # str or tuple


def process_text(text1, text2):
    letter_dict = {'A': 0, 'B': 10, 'C': 20, 'D': 30, 'E': 40, 'F': 50, 'G': 60, 'H': 70, 'I': 80, 'J': 90}
    result_text1 = None
    result_text2 = None

    if ',' in text1:  # if tuple
        list_text1 = text1.split()
        first_coord = letter_dict[list_text1[0][0]] + int(list_text1[0][2])
        sec_coord = (10 * (int(list_text1[1][0]) - 1)) + int(list_text1[1][2])
        result_text1 = (first_coord, sec_coord)
    else:  # if str
        result_text1 = text1

    list_text2 = text2.split()
    first_coord = letter_dict[list_text2[0][0]] + int(list_text2[0][2])
    sec_coord = (10 * (int(list_text2[1][0]) - 1)) + int(list_text2[1][2])
    result_text2 = (first_coord, sec_coord)

    return result_text1, result_text2


# Call this as add_user_input(process_text[0], process_text[1])
def add_user_input(coords):
    """Adds user inputs as nodes to the graph"""
    start = coords[0]
    circle = coords[1]
    POI_dict["Circle"] = [0, circle]
    global start_node
    for k, v in POI_dict.items():
        if (type(start) == str and start == k) or (type(start) == tuple and start == v[1]):
            start_node = k
            return

    POI_dict["Unnamed Start Location"] = [0, start]
    start_node = "Unnamed Start Location"


# print(nx.dijkstra_path(G, "Lucky Landing", "Risky Reels"))
def gen_path() -> [str]:
    """Generates path of POIs"""
    path = []
    time_left = 380
    if start_node != "Unnamed Start Location":
        time_left -= 90
    path.append(start_node)
    return path


def format_path(path_list):
    """Formats results of gen_path() as str"""
    str_result = "Path: " + str(path_list)
    return str_result


# PSEUDO
# Such that total time for first circle is 6:20 and time remaining at end is >= 0
#   Visit most POIs possible
# Assume time spent at each POI is 90 seconds
# first POI is 90 seconds, every POI after is 60 seconds
# START: user input coords
# END: center of circle // edge of circle
# distance to END has to shrink for any node we go to

# 380 seconds
# START: Lonely Lodge 90 secs
# END: (F-2, 7-7) -> (52,67)

# 290 seconds


# . . .
# 6:20 -> 380 seconds

# for n in G:












