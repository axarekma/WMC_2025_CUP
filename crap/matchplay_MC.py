from game import Game
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import matplotlib.colors as colors
import matplotlib as mpl


def getResultsRange(res):
    L = 0
    for p in res:
        L = max(L, p[0])
        L = max(L, p[1])
    return L + 1


class CupResult:
    def __init__(self, player1, player2, score):
        self.player1 = player1
        self.player2 = player2
        self.score = score
        self.winner = player1 if score[0] > score[1] else player2

    def result(self):
        return self.score


def rint(x):
    return np.round(x).astype(int)


class MCResult:
    def __init__(self, player1, player2, lane, data, lanes, n_iter):
        self.player1 = player1
        self.player2 = player2

        self.results = [
            tuple(Game(player1, player2, lane, data, lanes, MC=True).score)
            for el in range(n_iter)
        ]
        winner1 = [el[0] > el[1] for el in self.results]
        winner2 = [el[0] < el[1] for el in self.results]
        if np.sum(winner2) > np.sum(winner1):
            self.winner = player2
            self.loser = player1
            self.percentage = np.sum(winner2) / n_iter
        else:
            self.winner = player1
            self.loser = player2
            self.percentage = np.sum(winner1) / n_iter

    def result(self):
        res_score = [a[:2] for a in self.results]
        moderes = Counter(res_score).most_common(1)[0][0]
        p1, p2 = self.percentages()
        return (f"{moderes[0]} ({p1})", f"{moderes[1]} ({p2})")

    def percentages(self):
        n = len(self.results)
        p1 = int(round(100 * sum(r[0] > r[1] for r in self.results) / n))
        p2 = int(round(100 * sum(r[1] > r[0] for r in self.results) / n))
        return p1, p2

    def save_heatmap(self, name):
        size_x = max(p[0] for p in self.results) + 1
        size_y = max(p[1] for p in self.results) + 1
        heatmap = np.zeros((size_x, size_y), dtype=int)
        for p in self.results:
            heatmap[p[0], p[1]] = heatmap[p[0], p[1]] + 1
        heatmap = rint(100 * heatmap / len(self.results))
        heatmap_loworigin = np.flipud(heatmap.transpose())

        sns.heatmap(heatmap_loworigin, annot=True, fmt="d", cmap="viridis", cbar=False)
        plt.xlabel(self.player1)
        plt.ylabel(self.player2)

        plt.xticks(np.arange(size_x) + 0.5, np.arange(size_x))
        plt.yticks(np.arange(size_y) + 0.5, np.arange(size_y - 1, -1, -1))
        plt.title("Expected outcome of 100 games")
        if name is None:
            return
        plt.savefig(f"fig/{name}", bbox_inches="tight")
        plt.close()


# Format: (gametag, (source, value), (source, value), lane)
ROUNDS_16 = [
    ("G1", ("rank", 1), ("rank", 16), "A2"),
    ("G2", ("rank", 8), ("rank", 9), "A3"),
    ("G3", ("rank", 5), ("rank", 12), "A4"),
    ("G4", ("rank", 4), ("rank", 13), "A5"),
    ("G5", ("rank", 3), ("rank", 14), "A6"),
    ("G6", ("rank", 6), ("rank", 11), "A7"),
    ("G7", ("rank", 7), ("rank", 10), "A8"),
    ("G8", ("rank", 2), ("rank", 15), "A9"),
    ("G9", ("winner", "G1"), ("winner", "G2"), "A1"),
    ("G10", ("winner", "G3"), ("winner", "G4"), "A3"),
    ("G11", ("winner", "G5"), ("winner", "G6"), "A5"),
    ("G12", ("winner", "G7"), ("winner", "G8"), "A7"),
    ("SF1", ("winner", "G9"), ("winner", "G10"), "B1"),
    ("SF2", ("winner", "G11"), ("winner", "G12"), "B1"),
    ("Bronze", ("loser", "SF1"), ("loser", "SF2"), "B1"),
    ("Final", ("winner", "SF1"), ("winner", "SF2"), "B1"),
]
ROUNDS_32 = [
    ("G1", ("rank", 1), ("rank", 32), "A2"),
    ("G2", ("rank", 16), ("rank", 17), "A3"),
    ("G3", ("rank", 9), ("rank", 24), "A4"),
    ("G4", ("rank", 8), ("rank", 25), "A5"),
    ("G5", ("rank", 5), ("rank", 28), "A6"),
    ("G6", ("rank", 12), ("rank", 21), "A7"),
    ("G7", ("rank", 13), ("rank", 20), "A8"),
    ("G8", ("rank", 4), ("rank", 29), "A9"),
    ("G9", ("rank", 3), ("rank", 30), "B1"),
    ("G10", ("rank", 14), ("rank", 19), "B2"),
    ("G11", ("rank", 11), ("rank", 22), "B3"),
    ("G12", ("rank", 6), ("rank", 27), "B4"),
    ("G13", ("rank", 7), ("rank", 26), "B5"),
    ("G14", ("rank", 10), ("rank", 23), "B6"),
    ("G15", ("rank", 15), ("rank", 18), "B7"),
    ("G16", ("rank", 2), ("rank", 31), "B8"),
    ("G17", ("winner", "G1"), ("winner", "G2"), "B1"),
    ("G18", ("winner", "G3"), ("winner", "G4"), "B2"),
    ("G19", ("winner", "G5"), ("winner", "G6"), "B3"),
    ("G20", ("winner", "G7"), ("winner", "G8"), "B4"),
    ("G21", ("winner", "G9"), ("winner", "G10"), "B5"),
    ("G22", ("winner", "G11"), ("winner", "G12"), "B6"),
    ("G23", ("winner", "G13"), ("winner", "G14"), "B7"),
    ("G24", ("winner", "G15"), ("winner", "G16"), "B8"),
    ("QF1", ("winner", "G17"), ("winner", "G18"), "B1"),
    ("QF2", ("winner", "G19"), ("winner", "G20"), "B3"),
    ("QF3", ("winner", "G21"), ("winner", "G22"), "B5"),
    ("QF4", ("winner", "G23"), ("winner", "G24"), "B7"),
    ("SF1", ("winner", "QF1"), ("winner", "QF2"), "B1"),
    ("SF2", ("winner", "QF3"), ("winner", "QF4"), "B1"),
    ("Bronze", ("loser", "SF1"), ("loser", "SF2"), "B1"),
    ("Final", ("winner", "SF1"), ("winner", "SF2"), "B1"),
]


class Cup:
    def __init__(self, rank, data, lanes, bracket, mc_iter=1000):
        """
        rank: dict[int, str]
        lanes: dict[str, str] maps A and B lanes to the corresponding lane code
        rounds: list[dict[str, tuple]] where each dict is a round of games
        """
        self.rank = rank
        self.data = data
        self.lanes = lanes
        self.bracket = bracket
        self.mc_iter = mc_iter
        self.games = {}

    def set(self, game, result):
        self.games[game] = result

    def get_player(self, source, arg):
        if source == "rank":
            return self.rank[arg]
        elif source == "winner":
            return self.games[arg].winner
        elif source == "loser":
            return self.games[arg].loser
        else:
            raise ValueError(f"Unknown player type: {source}")

    def run(self):
        lanelist = list(self.lanes.values())
        for gametag, p1_ref, p2_ref, lane in self.bracket:
            p1 = self.get_player(*p1_ref)
            p2 = self.get_player(*p2_ref)
            print(p1, p2, self.lanes[lane])
            self.games[gametag] = MCResult(
                p1,
                p2,
                self.lanes[lane],
                self.data,
                lanelist,
                self.mc_iter,
            )
            self.games[gametag].save_heatmap(gametag)

    @property
    def winner(self):
        return self.games["Final"].winner

    @property
    def medals(self):
        return (
            self.games["Final"].winner,
            self.games["Final"].loser,
            self.games["Bronze"].winner,
        )


class Cup_16:
    def __init__(self, rank, data, lanesA, lanesB, mc_iter=100):
        self.data = data
        self.lanes = lanesA + lanesB
        self.mc_iter = mc_iter
        self.rank = rank

        # helper lists for easier indexing (starting lanes from invitation)
        self.A = [""] + lanesA
        self.B = [""] + lanesB
        self.games = dict()

    def set(self, game, result):
        self.games[game] = result

    def run(self):
        GPAR = {
            "G1": (self.rank[1], self.rank[16], self.A[2]),
            "G2": (self.rank[8], self.rank[9], self.A[3]),
            "G3": (self.rank[5], self.rank[12], self.A[4]),
            "G4": (self.rank[4], self.rank[13], self.A[5]),
            "G5": (self.rank[3], self.rank[14], self.A[6]),
            "G6": (self.rank[6], self.rank[11], self.A[7]),
            "G7": (self.rank[7], self.rank[10], self.A[8]),
            "G8": (self.rank[2], self.rank[15], self.A[9]),
        }
        for key, par in GPAR.items():
            self.games[key] = self.games.get(key, self.game(*par))

        GPAR = {
            "G9": (self.games["G1"].winner, self.games["G2"].winner, self.A[1]),
            "G10": (self.games["G3"].winner, self.games["G4"].winner, self.A[3]),
            "G11": (self.games["G5"].winner, self.games["G6"].winner, self.A[5]),
            "G12": (self.games["G7"].winner, self.games["G8"].winner, self.A[7]),
        }
        for key, par in GPAR.items():
            self.games[key] = self.games.get(key, self.game(*par))

        GPAR = {
            "S1": (self.games["G9"].winner, self.games["G10"].winner, self.B[1]),
            "S2": (self.games["G11"].winner, self.games["G12"].winner, self.B[1]),
        }
        for key, par in GPAR.items():
            self.games[key] = self.games.get(key, self.game(*par))

        GPAR = {
            "Bronze": (self.games["S1"].loser, self.games["S2"].loser, self.B[1]),
            "Final": (self.games["S1"].winner, self.games["S2"].winner, self.B[1]),
        }
        for key, par in GPAR.items():
            self.games[key] = self.games.get(key, self.game(*par))

    @property
    def winner(self):
        return self.games["Final"].winner

    @property
    def medals(self):
        return (
            self.games["Final"].winner,
            self.games["Final"].loser,
            self.games["Bronze"].winner,
        )

    def game(self, player1, player2, lane, MC=True):
        return MCResult(player1, player2, lane, self.data, self.lanes, self.mc_iter)


class Cup_32:
    def __init__(self, rank, data, lanesA, lanesB, mc_iter=100):
        self.data = data
        self.lanes = lanesA + lanesB
        self.mc_iter = mc_iter
        self.rank = rank

        # helper lists for easier indexing (starting lanes from invitation)
        self.A = [""] + lanesA
        self.B = [""] + lanesB
        self.games = dict()

    def set(self, game, result):
        self.games[game] = result

    def run(self):
        GPAR = {
            "G1": (self.rank[1], self.rank[32], self.A[2]),
            "G2": (self.rank[16], self.rank[17], self.A[3]),
            "G3": (self.rank[9], self.rank[24], self.A[4]),
            "G4": (self.rank[8], self.rank[25], self.A[5]),
            "G5": (self.rank[5], self.rank[28], self.A[6]),
            "G6": (self.rank[12], self.rank[21], self.A[7]),
            "G7": (self.rank[13], self.rank[20], self.A[8]),
            "G8": (self.rank[4], self.rank[29], self.A[9]),
            "G9": (self.rank[3], self.rank[30], self.B[1]),
            "G10": (self.rank[14], self.rank[19], self.B[2]),
            "G11": (self.rank[11], self.rank[22], self.B[3]),
            "G12": (self.rank[6], self.rank[27], self.B[4]),
            "G13": (self.rank[7], self.rank[26], self.B[5]),
            "G14": (self.rank[10], self.rank[23], self.B[6]),
            "G15": (self.rank[15], self.rank[18], self.B[7]),
            "G16": (self.rank[2], self.rank[31], self.B[8]),
        }
        for key, par in GPAR.items():
            self.games[key] = self.games.get(key, self.game(*par))

        GPAR = {
            "G17": (self.games["G1"].winner, self.games["G2"].winner, self.B[1]),
            "G18": (self.games["G3"].winner, self.games["G4"].winner, self.B[2]),
            "G19": (self.games["G5"].winner, self.games["G6"].winner, self.B[3]),
            "G20": (self.games["G7"].winner, self.games["G8"].winner, self.B[4]),
            "G21": (self.games["G9"].winner, self.games["G10"].winner, self.B[5]),
            "G22": (self.games["G11"].winner, self.games["G12"].winner, self.B[6]),
            "G23": (self.games["G13"].winner, self.games["G14"].winner, self.B[7]),
            "G24": (self.games["G15"].winner, self.games["G16"].winner, self.B[8]),
        }
        for key, par in GPAR.items():
            self.games[key] = self.games.get(key, self.game(*par))

        GPAR = {
            "QF1": (self.games["G17"].winner, self.games["G18"].winner, self.B[1]),
            "QF2": (self.games["G19"].winner, self.games["G20"].winner, self.B[3]),
            "QF3": (self.games["G21"].winner, self.games["G22"].winner, self.B[5]),
            "QF4": (self.games["G23"].winner, self.games["G24"].winner, self.B[7]),
        }
        for key, par in GPAR.items():
            self.games[key] = self.games.get(key, self.game(*par))

        GPAR = {
            "SF1": (self.games["QF1"].winner, self.games["QF2"].winner, self.B[1]),
            "SF2": (self.games["QF3"].winner, self.games["QF4"].winner, self.B[1]),
        }
        for key, par in GPAR.items():
            self.games[key] = self.games.get(key, self.game(*par))

        GPAR = {
            "Bronze": (self.games["SF1"].loser, self.games["SF2"].loser, self.B[1]),
            "Final": (self.games["SF1"].winner, self.games["SF2"].winner, self.B[1]),
        }
        for key, par in GPAR.items():
            self.games[key] = self.games.get(key, self.game(*par))

    @property
    def winner(self):
        return self.games["Final"].winner

    @property
    def medals(self):
        return (
            self.games["Final"].winner,
            self.games["Final"].loser,
            self.games["Bronze"].winner,
        )

    def game(self, player1, player2, lane):
        return MC_Game(player1, player2, lane, self.data, self.lanes, self.mc_iter)


def gen_Cup_16(ranks, data, lanes, n_max):
    for n in range(n_max):
        yield Cup_16(ranks, data, lanes)


def gen_Cup_32(ranks, data, lanes, n_max):
    for n in range(n_max):
        yield Cup_32(ranks, data, lanes)
