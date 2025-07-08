from matchfuncs import match
from matchfuncs import match_mean
from matchfuncs import match_log

class Game:
    def __init__(self, p1,p2,lane,DATA,LANES,MC = True):
        self.player1 = p1
        self.player2 = p2
        #load pickled darta
        #print('loading data for ',p1, player_id[p1],p2,player_id[p2])
        
        #OLD
        #with open('data/'+str(player_id[p1])+'.pickle', 'rb') as fp:
        #    data_p1 = pickle.load(fp)
        #with open('data/'+str(player_id[p2])+'.pickle', 'rb') as fp:
        #    data_p2 = pickle.load(fp)
        data_p1 = DATA[p1]
        data_p2 = DATA[p2]

        #run match
        if MC:
            self.score = match(data_p1,data_p2,LANES, lane)
        else:
            self.score = match_mean(data_p1,data_p2,LANES, lane)
        # print(p1,p2,self.score,self.winner)
        #print('w',self.winner,'l',self.loser)
    
    @property   
    def winner_V(self):
        #print(self.player1,self.player2,self.score)
        if (self.score[0]>self.score[1]):
            print('1')
            return self.player1
        elif (self.score[1]>self.score[0]):
            print('2')
            return self.player2
        else:
            print('Something went wrong')
            
    @property   
    def winner(self):
        if (self.score[0]>self.score[1]):
            return self.player1
        elif (self.score[1]>self.score[0]):
            return self.player2
        else:
            print('Something went wrong')
            
    @property 
    def loser(self):
        if (self.score[0]>self.score[1]):
            return self.player2
        elif (self.score[1]>self.score[0]):
            return self.player1
        else:
            print('Something went wrong')
    



class Game_lanelog:
    def __init__(self, p1,p2,lane,DATA,LANES,resfunc):
        self.player1 = p1
        self.player2 = p2

        data_p1 = DATA[p1]
        data_p2 = DATA[p2]
        
        self.score,self.lanelog = match_log(
            data_p1,data_p2,LANES, lane,resfunc)


    