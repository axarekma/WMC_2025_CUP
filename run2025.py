from mc_cup import (
    BamseScraper,
    Cup16,
    Cup32,
    export32,
    export16,
)
from mc_cup.html_utils import build_result_page

from conf_2025 import URL, LANES, RANK_W, RANK_M

mc_iter = 100000

data = BamseScraper(URL)
cupW = Cup16(RANK_W, data, LANES, mc_iter=mc_iter)
# Set Results here
cupW.set("G1", (5,7))
cupW.set("G2", (7,3))
cupW.set("G3", (2, 5))
cupW.set("G4", (4, 2))
cupW.set("G5", (6, 5))
cupW.set("G6", (2, 7))
cupW.set("G7", (3, 6))
cupW.set("G8", (4, 5))

cupW.set("G9", (0,4))
cupW.set("G10", (4.1,4))
cupW.set("G11", (6, 0))
cupW.set("G12", (1,4))

# cupW.set("SF1", (5, 4))
# cupW.set("SF2", (4, 7))
# cupW.set("Bronze", (2, 2.1))
# cupW.set("Final", (4, 3))

cupM = Cup32(RANK_M, data, LANES,mc_iter=mc_iter)
# Set Results here
cupM.set("G1", (5,3))
cupM.set("G2", (5, 3))
cupM.set("G3", (4, 2))
cupM.set("G4", (3, 5))
cupM.set("G5", (5,3))
cupM.set("G6", (6,2))
cupM.set("G7", (5,1))
cupM.set("G8", (3,6))
cupM.set("G9", (4,4.1))
cupM.set("G10", (4,6))
cupM.set("G11", (5, 2))
cupM.set("G12", (5,7))
cupM.set("G13", (6,0))
cupM.set("G14", (4.1,4))
cupM.set("G15", (6,3))
cupM.set("G16", (4,7))

cupM.set("G17", (2,5))
cupM.set("G18", (3, 3.1))
cupM.set("G19", (0,3))
cupM.set("G20", (4, 3))
cupM.set("G21", (7, 2))
cupM.set("G22", (7, 3))
cupM.set("G23", (4, 1))
cupM.set("G24", (5, 3))

cupM.set("QF1", (4,2))
cupM.set("QF2", (5,1))
cupM.set("QF3", (0,7))
cupM.set("QF4", (6,4))

# cupM.set("SF1", (7, 2))
# cupM.set("SF2", (6, 5))
# cupM.set("Bronze", (6, 2))
# cupM.set("Final", (5, 5.1))


cupW.run()
cupM.run()


table_W = export16(cupW)
table_M = export32(cupM)
build_result_page("CUP 2025", "Matchplay Prediction 2025", table_W, table_M, "index.html")
