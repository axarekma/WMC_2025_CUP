from mc_cup import (
    BamseScraper,
    Cup16,
    Cup32,
    export32,
    export16,
)
from mc_cup.html_utils import build_result_page

from conf_2024 import URL, LANES, RANK_W, RANK_M

data = BamseScraper(URL)
cupW = Cup16(RANK_W, data, LANES)
# Set Results here
cupW.set("G1", (5, 1))
cupW.set("G2", (3, 4))
cupW.set("G3", (5.1, 5))
cupW.set("G4", (5, 3))
cupW.set("G5", (5, 2))
cupW.set("G6", (3, 5))
cupW.set("G7", (6, 2))
cupW.set("G8", (5, 1))

cupW.set("G9", (4.1, 4))
cupW.set("G10", (5, 3))
cupW.set("G11", (6, 3))
cupW.set("G12", (6, 4))

cupW.set("SF1", (5, 4))
cupW.set("SF2", (4, 7))
cupW.set("Bronze", (2, 2.1))
cupW.set("Final", (4, 3))

cupM = Cup32(RANK_M, data, LANES)
# Set Results here
cupM.set("G1", (5, 4))
cupM.set("G2", (6, 3))
cupM.set("G3", (4, 6))
cupM.set("G4", (3, 1))
cupM.set("G5", (3, 6))
cupM.set("G6", (5, 3))
cupM.set("G7", (4, 6))
cupM.set("G8", (3, 2))
cupM.set("G9", (6, 5))
cupM.set("G10", (1, 6))
cupM.set("G11", (6, 2))
cupM.set("G12", (7, 2))
cupM.set("G13", (4, 3))
cupM.set("G14", (6, 4))
cupM.set("G15", (4, 5))
cupM.set("G16", (5, 4))

cupM.set("G17", (6, 2))
cupM.set("G18", (3, 4))
cupM.set("G19", (3, 6))
cupM.set("G20", (3, 5))
cupM.set("G21", (1, 7))
cupM.set("G22", (2, 4))
cupM.set("G23", (7, 4))
cupM.set("G24", (5, 6))

cupM.set("QF1", (4.1, 4))
cupM.set("QF2", (5.1, 5))
cupM.set("QF3", (4, 1))
cupM.set("QF4", (2, 5))

cupM.set("SF1", (7, 2))
cupM.set("SF2", (6, 5))
cupM.set("Bronze", (6, 2))
cupM.set("Final", (5, 5.1))


cupW.run()
cupM.run()


table_W = export16(cupW)
table_M = export32(cupM)
build_result_page(
    "CUP 2024", "Placeholder posterior results of 2024", table_W, table_M, "index.html"
)
