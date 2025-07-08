URL = "https://minigolf-live.com/turnier1405a/"

LANES_F = [1, 4, 6, 8, 10, 12, 13, 15, 17]
LANES_E = [1, 3, 4, 5, 7, 13, 14, 16, 17]


LANES = {
    **{f"A{i+1}": f"F{lane}" for i, lane in enumerate(LANES_F)},
    **{f"B{i+1}": f"E{lane}" for i, lane in enumerate(LANES_E)},
}


RANK_W = {
    1: "Sarah Schumacher",
    2: "Vanessa Peuker",
    3: "Stefanie Blendermann",
    4: "Marielle Svensson",
    5: "Karin Olsson",
    6: "Anna Bandera",
    7: "Julia Sjöberg",
    8: "Alva Kvarnström",
    9: "Jasmin Bothmann",
    10: "Lucie Indráková",
    11: "Martina Saletta",
    12: "Mia Vuorihovi",
    13: "Martina Maderová",
    14: "Kristyna Palánová",
    15: "Mirva Juhola",
    16: "Silvia Bandera",
}

RANK_M = {
    1: "Yannick Müller",
    2: "Kenny Marc Schmeckenbecher",
    3: "Martin Ječný",
    4: "Alexander Princis",
    5: "Fredrik Persson",
    6: "Marvin Hauri",
    7: "Lauro Klöckener",
    8: "Sebastian Piekorz",
    9: "Karel jr. Molnár",
    10: "Amir El Quachani",
    11: "Tobias Schwarz",
    12: "Daniel Moser",
    13: "Erik Nilsson",
    14: "Marián Straško",
    15: "Marco Broggi",
    16: "Beat Wartenweiler",
    17: "Lukas Neumann",
    18: "Andreas Schneider",
    19: "Marek Smejkal",
    20: "Daniel Brtevník",
    21: "Ondřej Škaloud",
    22: "Simon Junker",
    23: "Sebastian Heine",
    24: "Erik Fause Hovind",
    25: "Zdeněk Majkus",
    26: "Aapo Siurola",
    27: "Julian Weibold",
    28: "Maxime Bugnion",
    29: "Kevin Feuchtl",
    30: "Marcus I Andersson",
    31: "Youri Bottenberg",
    32: "Paolo Porta",
}
