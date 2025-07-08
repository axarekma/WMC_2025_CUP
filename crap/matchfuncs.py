import random
import numpy as np


def getRandom(res_dict, key):
    return random.choice(res_dict[key])


def getMean(res_dict, key):
    return np.mean(res_dict[key])


def sudden(player1, player2, lanes, start_index, score):
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
            return sudden(player1, player2, lanes, lane_index, score) + ["SD"]


def gen_match(player1, player2, lanes, start_index, n_max):
    for n in range(n_max):
        yield match(player1, player2, lanes, start_index)


def sudden_mean(player1, player2, lanes, start_index, score):
    lane_index = start_index
    while True:
        res = (getMean(player1, lanes[lane_index]), getMean(player2, lanes[lane_index]))
        if res[0] < res[1]:
            score[0] = score[0] + 1
        if res[1] < res[0]:
            score[1] = score[1] + 1
        if res[0] != res[1]:
            return score

        lane_index = (lane_index + 1) % len(lanes)


def match_mean(player1, player2, lanes, lane):
    start_index = lanes.index(lane)
    num_lanes = 0
    lanes_left = len(lanes)
    score = [0, 0]
    lane_index = start_index
    while True:
        res = (getMean(player1, lanes[lane_index]), getMean(player2, lanes[lane_index]))
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
            return sudden_mean(player1, player2, lanes, lane_index, score) + ["SD"]


def sudden_log(player1, player2, lanes, start_index, score, resfunc):
    lane_index = start_index
    while True:
        res = (resfunc(player1, lanes[lane_index]), resfunc(player2, lanes[lane_index]))
        if res[0] < res[1]:
            score[0] = score[0] + 1
            score_lanes[lane_index] = score_lanes[lane_index] + 1
        if res[1] < res[0]:
            score[1] = score[1] + 1
            score_lanes[lane_index] = score_lanes[lane_index] - 1
        if res[0] != res[1]:
            return score, score_lanes

        lane_index = (lane_index + 1) % len(lanes)


def match_log(player1, player2, lanes, lane, resfunc):
    start_index = lanes.index(lane)
    num_lanes = 0
    lanes_left = len(lanes)
    score = [0, 0]

    score_lanes = [0] * len(lanes)

    lane_index = start_index
    while True:
        res = (resfunc(player1, lanes[lane_index]), resfunc(player2, lanes[lane_index]))
        if res[0] < res[1]:
            score[0] = score[0] + 1
            score_lanes[lane_index] = score_lanes[lane_index] + 1
        if res[1] < res[0]:
            score[1] = score[1] + 1
            score_lanes[lane_index] = score_lanes[lane_index] - 1
        num_lanes = num_lanes + 1
        lanes_left = lanes_left - 1

        if abs(score[1] - score[0]) > lanes_left:
            return score, score_lanes

        lane_index = (lane_index + 1) % len(lanes)
        if lanes_left == 0:
            return (
                sudden(player1, player2, lanes, lane_index, score) + ["SD"],
                score_lanes,
            )
