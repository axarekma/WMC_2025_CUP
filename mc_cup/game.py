import random


def getRandom(res_dict, key):
    return random.choice(res_dict[key])


def sudden(player1, player2, lanes, start_index, score):
    lane_index = start_index
    while True:
        res = (
            getRandom(player1, lanes[lane_index]),
            getRandom(player2, lanes[lane_index]),
        )
        if res[0] < res[1]:
            score[0] = score[0] + 0.1
        if res[1] < res[0]:
            score[1] = score[1] + 0.1
        if res[0] != res[1]:
            return score

        lane_index = (lane_index + 1) % len(lanes)


def match(player1, player2, lanes, lane):
    start_index = lanes.index(lane)
    num_lanes = 0
    lanes_left = len(lanes)
    score = [0, 0]
    lane_index = start_index
    while True:
        res = (
            getRandom(player1, lanes[lane_index]),
            getRandom(player2, lanes[lane_index]),
        )
        if res[0] < res[1]:
            score[0] = score[0] + 1
        if res[1] < res[0]:
            score[1] = score[1] + 1
        num_lanes = num_lanes + 1
        lanes_left = lanes_left - 1

        if abs(score[1] - score[0]) > lanes_left:
            return score

        lane_index = (lane_index + 1) % len(lanes)
        if lanes_left == 0:
            return sudden(player1, player2, lanes, lane_index, score)


class Game:
    def __init__(self, p1, p2, lane, DATA, LANES):
        self.player1 = p1
        self.player2 = p2

        data_p1 = DATA[p1]
        data_p2 = DATA[p2]

        self.score = match(data_p1, data_p2, LANES, lane)

    @property
    def winner_V(self):
        # print(self.player1,self.player2,self.score)
        if self.score[0] > self.score[1]:
            print("1")
            return self.player1
        elif self.score[1] > self.score[0]:
            print("2")
            return self.player2
        else:
            print("Something went wrong")

    @property
    def winner(self):
        if self.score[0] > self.score[1]:
            return self.player1
        elif self.score[1] > self.score[0]:
            return self.player2
        else:
            print("Something went wrong")

    @property
    def loser(self):
        if self.score[0] > self.score[1]:
            return self.player2
        elif self.score[1] > self.score[0]:
            return self.player1
        else:
            print("Something went wrong")


class Game_lanelog:
    def __init__(self, p1, p2, lane, DATA, LANES, resfunc):
        self.player1 = p1
        self.player2 = p2

        data_p1 = DATA[p1]
        data_p2 = DATA[p2]

        self.score, self.lanelog = match_log(data_p1, data_p2, LANES, lane, resfunc)
