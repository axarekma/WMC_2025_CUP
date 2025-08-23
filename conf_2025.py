URL = "https://www.minigolf-live.com/turnier1504a/"

LANES_C = [1,2,5,6,9,10,14,15,17]
LANES_E = [4,5,6,8,9,11,16,17,18]


LANES = {
    **{f"A{i+1}": f"C{lane}" for i, lane in enumerate(LANES_C)},
    **{f"B{i+1}": f"E{lane}" for i, lane in enumerate(LANES_E)},
}


RANK_W = {
    1: "Nicole Birkelbach",
    2: "Lara Jehle",
    3: "Claudia Schuster",
    4: "Karin Heschl",
    5: "Maja Eigenmann",
    6: "Vanessa Peuker",
    7: "Jasmin Bothmann",
    8: "Anna Bandera",
    9: "Marielle Svensson",
    10: "Julia Sjöberg",
    11: "Mia Vuorihovi",
    12: "Sarah Schumacher",
    13: "Birgit Wagenhofer",
    14: "Johanna Lindoff",
    15: "Martina Saletta",
    16: "Silvia Bandera",
}

RANK_M = {
    1: "Tobias Schwarz",
    2: "Marián Straško",
    3: "Rikard Lindqvist",
    4: "Beat Wartenweiler",
    5: "Ondřej Škaloud",
    6: "Sebastian Piekorz",
    7: "Dennis Kapke",
    8: "Lauro Klöckener",
    9: "Maxime Bugnion",
    10: "Tristan Kleiner",
    11: "Paolo Porta",
    12: "Lukas Neumann",
    13: "Thomas Lottermoser",
    14: "Simon Junker",
    15: "Marek Smejkal",
    16: "Peter Eriksson",
    17: "Yannick Müller",
    18: "Manfred Lindmayr",
    19: "Angelo Friedli",
    20: "Lars Anderegg",
    21: "Marcus Ljungblad",
    22: "Matteo Diotti",
    23: "Valerio Marcoaldi",
    24: "Daniel Brtevník",
    25: "Christian Gobetz",
    26: "Ulf Kristiansson",
    27: "Marco Broggi",
    28: "Erik Nilsson",
    29: "Marko Nuotio",
    30: "Zeno Folkertsma",
    31: "Daniel Moser",
    32: "Jan Kadlec",
    # 32: "Martin Skoupý",
    # 32: "Zdeněk Majkus",
    # 35: "Johan Rydberg",
    # 32: "Jan Egbert Hooijsma",
}
