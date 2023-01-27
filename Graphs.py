import seaborn as sns
import matplotlib.pyplot as plt
import argparse as ap
import json
import os
from os import path

def generate_graphs(in_file, scheduler):
    path_scheduler = 'Graphs/' + scheduler
    if not path.exists(path_scheduler):
        try:
            os.mkdir(path_scheduler)
        except OSError as error:
            print(error)
    y_axis_regression           = []
    y_axis_CDF                  = []
    x_axis_makespan_function    = []
    x_axis_makespan_reward      = []
    x_axis_slowdown_function    = []
    x_axis_slowdown_reward      = []
    with open (in_file, 'r') as file:
        data = json.load(file)
    data.sort(key=lambda k : k['starting_time'])
    for d in data:
        y_axis_regression.append(d['starting_time'])
        y_axis_CDF.append(data.index(d) / len(data))
        x_axis_makespan_function.append(d['makespan_function'])
        x_axis_makespan_reward.append(d['makespan_reward'])
        x_axis_slowdown_function.append(d['slowdown_function'])
        x_axis_slowdown_reward.append(d['slowdown_reward'])
    #CDF

    path_scheduler = 'Graphs/' + scheduler + '/'
    if not path.exists(path_scheduler):
        try:
            os.mkdir(path_scheduler)
        except OSError as error:
            print(error)

    x_axis_makespan_function.sort()
    # print(x_axis_makespan_function)
    regression = plt.scatter(x_axis_makespan_function, y_axis_CDF)
    name = path_scheduler + '_makespan_function_CDF.png'
    plt.savefig(name) 
    plt.clf()

    x_axis_makespan_reward.sort()
    # print(x_axis_makespan_reward)
    regression = plt.scatter(x_axis_makespan_reward, y_axis_CDF)
    name = path_scheduler + '_makespan_reward_CDF.png'
    plt.savefig(name) 
    plt.clf()

    x_axis_slowdown_function.sort()
    # print(x_axis_slowdown_function)
    regression = plt.scatter(x_axis_slowdown_function, y_axis_CDF)
    name = path_scheduler + '_slowdown_function_CDF.png'
    plt.savefig(name) 
    plt.clf()

    x_axis_slowdown_reward.sort()
    # print(x_axis_slowdown_reward)
    regression = plt.scatter(x_axis_slowdown_reward, y_axis_CDF)
    name = path_scheduler + '_slowdown_reward_CDF.png'
    plt.savefig(name) 
    plt.clf()


if __name__ == '__main__':
    parse = ap.ArgumentParser()
    parse.add_argument('in_file')
    parse.add_argument('scheduler')
    arg = parse.parse_args()

generate_graphs(arg.in_file, arg.scheduler)
