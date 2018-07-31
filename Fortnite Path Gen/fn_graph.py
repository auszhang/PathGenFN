import math
#import networkx as nx

#G = nx.Graph()

# Named locations only, for now
POI_list = ["Lonely Lodge", "Retail Row", "Flush Factory", "Shifty Shafts", "Greasy Grove",
            "Risky Reels", "Fatal Fields", "Lucky Landing", "Junk Junction", "Snobby Shores", "Pleasant Park",
            "Salty Springs", "Loot Lake", "Dusty Divot", "Tilted Towers", "Haunted Hills",
            "Tomato Town", "Lazy Links", "Paradise Palms"]

#G.add_nodes_from(POI_list)

Unnamed_POIs = ["RV Park", "Superhero Mansion", "Crate Yard", "Villain Lair", "Viking Village", "Racetrack",
                "Motel", "Disco Factory", "Desert Village"]

# Number of chests pulled from fortnitechests.info, with some personal digression
# Number of chests included for possible weights to POIs in the future
# For Risky Reels, I excluded the side houses
# For Tomato Town, I included the overpass
POI_dict = {"Lonely Lodge": (91, 41), "Retail Row": (75, 53), "Flush Factory": (34, 88),
            "Shifty Shafts": (36, 64), "Greasy Grove": (22, 62),
            "Risky Reels": (75, 19), "Fatal Fields": (61, 76), "Lucky Landing": (57, 92),
            "Salty Springs": (57, 61), "Loot Lake": (40, 36), "Dusty Divot": (60, 50),
            "Tilted Towers": (37, 48), "Haunted Hills": (13, 19), "Tomato Town": (67, 30),
            "Lazy Links": (53, 19), "Paradise Palms": (83, 74)}

# G.add_nodes_from(POI_dict.keys)


# INPUTS: either string (POI) or tuple of int (coordinates)
def distance(c1, c2):
    """Takes set of either POI name/coordinates and returns the distance between them"""
    # Changes from str -> tuple(int)

    if type(c1) == str:
        c1 = POI_dict[c1]
    if type(c2) == str:
        c2 = POI_dict[c2]

    result_int = round(math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2), 2)  # Distance formula, rounded to 2 decimals
    return result_int


# 10 units is ~ 74 seconds
def time(c1, c2):
    """Uses results from distance() function and converts to time"""
    return round((74/10) * distance(c1, c2), 2)


# def gen_edges():
#     for k, v in POI_dict.items():
#         for k2, v2 in POI_dict.items():
#             if k is not k2:
#                 G.add_edge(k, k2, weight=time(k, k2))


# Prints edges
# for i, j, d in G.edges(data="weight"):
#     print(i, j, d)


# String processing
# Expected input: "Lonely Lodge", (C-3,6-2)
# Or something like: E-6,3-9 | C-3,6-2 -> (46, 29), . . .


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


class Node():
    def __init__(self, name):
        self.name = name
        self.num_before = 0
        self.prev = None
        self.neighbors = []
        self.time_left = 380
        self.location = tuple()

    def __repr__(self):
        return "name: " + self.name + "," + "location: " + str(self.location)


start_node = Node("Temp Name")  # Changed to type Node
circle_center = tuple()


# Call this as add_user_input(process_text[0], process_text[1])
def add_user_input(coords):
    """Adds user inputs as nodes to the graph"""
    start = coords[0]
    # circle = coords[1]
    global circle_center
    circle_center = coords[1]
    global start_node

    for k, v in POI_dict.items():
        if (type(start) == str and start == k) or (type(start) == tuple and start == v):
            if start == k:
                start_node.name = k
                return

    POI_dict["Unnamed Start Location"] = [start]
    start_node.name = "Unnamed Start Location"


# def gen_path() -> [str]:
#     """Generates path of POIs"""
#     path = []
#     time_left = 380
#     if start_node != "Unnamed Start Location":
#         time_left -= 90
#     path.append(start_node)
#     return path


# time_left = 380  # New global variable
# path = []
# copy_G = G.copy()


# Changed from gen_path()
# def add_start_node() -> [str]:
#     """Adds first node to empty list"""
#     if start_node.name != "Unnamed Start Location":
#         start_node.time_left -= 90
#     global path
#     path.append(start_node)


# Assumes that:
#	Time has already been deducted when necessary
#	start_node has been added to graph


# def gen_copy_G():
#     """Creates and returns copy of graph that removes nodes inaccessible by initial remaining time"""
#     radius = time_left
#     copy_G = G.copy()
#     for e in copy_G.edges_iter():
#         if start_node in e and weight < time_left:
#             for n in e:
#                 if n != start_node:
#                     copy_G.remove_node(n)
#     return copy_G
# copy_G = gen_copy_G()  # Creates global copy_G


final_list = []


def time_to_circle(loc):
    """Returns time to circle edge from current location"""
    return time(loc, circle_center) - round((74/10) * 32.5)


def find_neighbors(curr_node) -> None:
    """Find the neighbors of each POI with given time left and start point"""
    for key, value in POI_dict.items():
        if key == curr_node.name:
            pass
        else:
            if curr_node.time_left >= 90 + time_to_circle(key) + time(key, curr_node.name):
                neighbor = Node(key)
                neighbor.location = value
                neighbor.time_left = curr_node.time_left - (90 + time(key, curr_node.name))
                neighbor.prev = curr_node
                if curr_node.prev is not None:
                    neighbor.num_before = curr_node.num_before + 1
                curr_node.neighbors.append(neighbor)


def depth_first_search():
    """Uses depth-first search to traverse all nodes"""
    stack = [start_node]
    while stack:  # while stack is not empty
        curr_node = stack.pop()
        final_list.append(curr_node)
        find_neighbors(curr_node)
        for neighbor in curr_node.neighbors:
            stack.append(neighbor)


def gen_path() -> list:
    """Adds names of nodes in longest path to global path"""
    path = []
    max_visited = 0
    max_node = None

    for node in final_list:
        if node.num_before > max_visited:
            max_visited = node.num_before
            max_node = node
        print(repr(node))

    while max_node is not None:
        # if len(max_node.name) == 0:
        #     print("Node location:", max_node.location)
        path = [max_node.name] + path
        max_node = max_node.prev

    path.append("Circle")
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
# print(nx.dijkstra_path(G, "Lucky Landing", "Risky Reels"))










