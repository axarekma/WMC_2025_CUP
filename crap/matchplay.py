from game import Game

class Cup_16:
    def __init__(self,rank,data,lanesA,lanesB):
        self.data = data
        self.lanes = lanesA+lanesB

        # helper lists for easier indexing (starting lanes from invitation)
        A = ['']+lanesA
        B = ['']+lanesB


        self.games = dict()
        self.games['G1'] = self.game(rank[1],rank[16],A[2])
        self.games['G2'] = self.game(rank[8],rank[9],A[3])
        self.games['G3'] = self.game(rank[5],rank[12],A[4])
        self.games['G4'] = self.game(rank[4],rank[13],A[5])
        self.games['G5'] = self.game(rank[3],rank[14],A[6])
        self.games['G6'] = self.game(rank[6],rank[11],A[7])
        self.games['G7'] = self.game(rank[7],rank[10],A[8])
        self.games['G8'] = self.game(rank[2],rank[15],A[9])
        #bo8
        self.games['G9'] = self.game(self.games['G1'].winner ,
                                self.games['G2'].winner,A[1])
        self.games['G10'] = self.game(self.games['G3'].winner ,
                                 self.games['G4'].winner,A[3])
        self.games['G11'] = self.game(self.games['G5'].winner ,
                                 self.games['G6'].winner,A[5])
        self.games['G12'] = self.game(self.games['G7'].winner ,
                                 self.games['G8'].winner,A[7])
        #bo4
        self.games['S1'] = self.game(self.games['G9'].winner ,
                                self.games['G10'].winner,B[1])
        self.games['S2'] = self.game(self.games['G11'].winner ,
                                self.games['G12'].winner,B[1])
        #bronze
        self.games['Bronze'] = self.game(self.games['S1'].loser ,
                                    self.games['S2'].loser,B[1])
        #bronze
        self.games['Final'] = self.game(self.games['S1'].winner ,
                                    self.games['S2'].winner,B[1])
    @property
    def winner(self):
        return self.games['Final'].winner
                
    @property
    def medals(self):
        return (self.games['Final'].winner,
               self.games['Final'].loser,
               self.games['Bronze'].winner)
    def game(self,p1,p2,k,MC = True):
        return Game(p1,p2,k,self.data,self.lanes,MC)

class Cup_32:
    def __init__(self,rank,data,lanesA,lanesB, mc_iter = 100):
        self.data = data
        self.lanes = lanesA+lanesB
        self.mc_iter = mc_iter

        # helper lists for easier indexing (starting lanes from invitation)
        A = ['']+lanesA
        B = ['']+lanesB

        self.games = dict()
        self.games['G1'] = self.game(rank[1],rank[32],A[2])
        self.games['G2'] = self.game(rank[16],rank[17],A[3])
        self.games['G3'] = self.game(rank[9],rank[24],A[4])
        self.games['G4'] = self.game(rank[8],rank[25],A[5])
        self.games['G5'] = self.game(rank[5],rank[28],A[6])
        self.games['G6'] = self.game(rank[12],rank[21],A[7])
        self.games['G7'] = self.game(rank[13],rank[20],A[8])
        self.games['G8'] = self.game(rank[4],rank[29],A[9])

        self.games['G9'] = self.game(rank[3],rank[30],B[1])
        self.games['G10'] = self.game(rank[14],rank[19],B[2])
        self.games['G11'] = self.game(rank[11],rank[22],B[3])
        self.games['G12'] = self.game(rank[6],rank[27],B[4])
        self.games['G13'] = self.game(rank[7],rank[26],B[5])
        self.games['G14'] = self.game(rank[10],rank[23],B[6])
        self.games['G15'] = self.game(rank[15],rank[18],B[7])
        self.games['G16'] = self.game(rank[2],rank[31],B[8])
        #bo8
        self.games['G17'] = self.game(self.games['G1'].winner ,
                                 self.games['G2'].winner,B[1])
        self.games['G18'] = self.game(self.games['G3'].winner ,
                                 self.games['G4'].winner,B[2])
        self.games['G19'] = self.game(self.games['G5'].winner ,
                                 self.games['G6'].winner,B[3])
        self.games['G20'] = self.game(self.games['G7'].winner ,
                                 self.games['G8'].winner,B[4])
        self.games['G21'] = self.game(self.games['G9'].winner ,
                                 self.games['G10'].winner,B[5])
        self.games['G22'] = self.game(self.games['G11'].winner ,
                                 self.games['G12'].winner,B[6])
        self.games['G23'] = self.game(self.games['G13'].winner ,
                                 self.games['G14'].winner,B[7])
        self.games['G24'] = self.game(self.games['G15'].winner ,
                                 self.games['G16'].winner,B[8])
        #bo8
        self.games['G25'] = self.game(self.games['G17'].winner ,
                                 self.games['G18'].winner,B[1])
        self.games['G26'] = self.game(self.games['G19'].winner ,
                                 self.games['G20'].winner,B[3])
        self.games['G27'] = self.game(self.games['G21'].winner ,
                                 self.games['G22'].winner,B[5])
        self.games['G28'] = self.game(self.games['G23'].winner ,
                                 self.games['G24'].winner,B[7])
        
        #bo4
        self.games['S1'] = self.game(self.games['G25'].winner ,
                                self.games['G26'].winner,B[1])
        self.games['S2'] = self.game(self.games['G27'].winner ,
                                self.games['G28'].winner,B[1])
        #bronze
        self.games['Bronze'] = self.game(self.games['S1'].loser ,
                                    self.games['S2'].loser,B[1])
        #bronze
        self.games['Final'] = self.game(self.games['S1'].winner ,
                                    self.games['S2'].winner,B[1])
                
    @property
    def winner(self):
        return self.games['Final'].winner
        
    @property
    def medals(self):
        return (self.games['Final'].winner,
               self.games['Final'].loser,
               self.games['Bronze'].winner)

    def game(self,p1,p2,k,MC = True):
        return Game(p1,p2,k,self.data,self.lanes,MC)

    
from tqdm.auto import trange
def gen_Cup_16(ranks,data,lanesA,lanesB,n_max):
    for n in trange(n_max):
        yield Cup_16(ranks,data,lanesA,lanesB)
        
def gen_Cup_32(ranks,data,lanesA,lanesB,n_max):
    for n in trange(n_max):
        yield Cup_32(ranks,data,lanesA,lanesB)